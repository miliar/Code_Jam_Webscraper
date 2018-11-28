#include <bits/stdc++.h>
#define LL long long
using namespace std;

const int maxn = 100 + 10;

int dp[2][maxn];
char s[maxn];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cas=0,n;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s",s+1);
        memset(dp,0x3f3f3f3f,sizeof dp);
        if (s[1]=='+') {dp[0][1] = 0; dp[1][1] = 1;}
        else {dp[0][1] = 1; dp[1][1]=0;}
        n=strlen(s+1);
        for (int i=2;i<=n;i++)
        {
            if (s[i] == '+')
            {
                dp[0][i] = min(dp[0][i-1],min(dp[1][i-1]+2, dp[0][i]));
                dp[1][i] = min(dp[1][i-1]+2,min(dp[0][i-1]+1, dp[1][i]));
            }
            else
            {
                dp[1][i] = min(dp[1][i-1],min(dp[0][i-1]+2, dp[1][i]));
                dp[0][i] = min(dp[0][i-1]+2,min(dp[1][i-1]+1, dp[0][i]));
            }
        }
        printf("Case #%d: %d\n",++cas,min(dp[0][n] , dp[1][n]+1));
    }
    return 0;
}
