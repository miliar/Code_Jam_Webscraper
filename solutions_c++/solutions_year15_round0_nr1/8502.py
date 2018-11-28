#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int _, cas=1;
    scanf("%d", &_);
    while(_--) {
        int len;
        string s;
        cin >> len >> s;
        int ans=0, sum=0;
        for(int i=0; i<=len; i++) {
            if(sum < i) {
                ans += i-sum;
                sum = i;
            }
            sum += s[i]-'0';
        }
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}
