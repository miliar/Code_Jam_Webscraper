#include <iostream>
#include <stdio.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<ctype.h>
using namespace std;
#define MAXN 10000
int dp[1010][1010];
int a[1010];
int f(int x)
{
    return x/2+x%2;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    int cas=1;
    int n;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        memset(dp,0x3f,sizeof(dp));
        for(int i=1;i<=n;i++)
        {
            scanf("%d",a+i);
        }
        memset(dp[0],0,sizeof(dp[0]));
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=1000;j++)
            {
                dp[i][j]=dp[i][j-1];
                dp[i][j]=min(dp[i][j],dp[i-1][j]+(a[i]-1)/j);
            }
        }
        int ans=10000000;
        for(int j=0;j<=1000;j++)
        {
            ans=min(ans,dp[n][j]+j);
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
