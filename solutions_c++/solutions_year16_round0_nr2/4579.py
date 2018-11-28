#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
char s[105];
int dp[105];
int main()
{
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    int t;
    cin >> t;
    int cas = 1;
    while(t--)
    {
        scanf("%s", s);
        int ans = 0;
        int len = strlen(s);
        memset(dp, 0, sizeof(dp));
        dp[0] = s[0] == '-' ? 1 : 0;
        for(int i = 1; i < len; i++)
        {
            if(s[i] == '-' && s[i - 1] == '+')
                dp[i] = dp[i - 1] + 2;
            else
                dp[i] = dp[i - 1];
        }
        printf("Case #%d: %d\n", cas++, dp[len - 1]);
    }
}
