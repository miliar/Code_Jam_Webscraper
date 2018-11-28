#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int dp[110][1100];
int h[110];
int g[110];
int main()
{
    int ti;scanf("%d",&ti);
    for(int ca=1;ca<=ti;ca++)
    {
        memset(dp,-1,sizeof(dp));
        dp[0][1]=0;
        int p,q,n;scanf("%d%d%d",&p,&q,&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d%d",h+i,g+i);
        }
        for(int i=0;i<=n;i++)
        {
            int d = (h[i]-1)/q;
            int l = h[i]-d*q;
            int D = (l-1)/p+1;
            //printf("%d %d\n",d,D);
            for(int has=0;has<1100;has++)if(dp[i][has]>=0)
            {
                //printf("%d %d %d\n",i,has,dp[i][has]);
                int f = D-d;
                if(has-f>=0)
                {
                    dp[i+1][has-f] = max(dp[i+1][has-f], dp[i][has] + g[i]);
                }
                dp[i+1][has+d+1] = max(dp[i+1][has+d+1], dp[i][has]);
            }
        }
        int ret=0;
        for(int has=0;has<1100;has++)
        {
            ret = max(ret, dp[n][has]);
        }
        printf("Case #%d: %d\n",ca,ret);
    }
}
