#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
using namespace std;
int dp[110];

void solve()
{
    int T,kcase = 1;
    cin>>T;
    while(T--)
    {
        memset(dp,0,sizeof dp);
        string s;
        cin>>s;
        int len = s.length();
        for(int i = 0; i < len; ++i)
        {
            if(i == 0)
            {
                dp[i] += (s[i] == '-');
            }
            else
            {
                if(s[i] == '-' && s[i - 1] == '+')
                    dp[i] = dp[i - 1] + 2;
                else dp[i] = dp[i - 1];
            }
        }
        printf("Case #%d: ",kcase++);
        printf("%d\n",dp[len - 1]);
    }
}

int main() {
    //freopen("in","r",stdin);
    //freopen("A.out","w",stdout);
    solve();
    return 0;
}
