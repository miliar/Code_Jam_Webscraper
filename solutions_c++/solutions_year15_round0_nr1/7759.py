#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    for(int test = 1;test <= t;test++) {
        int n;
        cin >> n;
        string str;
        cin >> str;
        int ans = 0;
        int k=0;
        for(int i=0;i<=n;i++) {
            if(k >= i) k += str[i]-'0';
            else {ans += (i-k); k = i+str[i]-'0';}
        }
        cout << "Case #" << test << ": " << ans << endl;
    }
}
