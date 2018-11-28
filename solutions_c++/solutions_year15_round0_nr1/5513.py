#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    int n;
    int i;
    int j;
    string s;
    int ans;
    int count;

    cin>>t;
    for(j = 1; j <= t; j++) {
        cin>>n>>s;
        ans = 0;
        count = 0;

        for(i = 0; i < s.size(); i++) {
            if(i > count) {
                ans = ans + (i - count);
                count = count + (i - count);
            }
           // cout<<count<<' '<<ans<<endl;
            count = count + (s[i] - '0');
        }
        printf("Case #%d: %d\n",j,ans);
    }
}
