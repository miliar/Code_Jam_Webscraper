#include <stdio.h>
#include <string.h>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

double dp[201][201];
double p[210];
double arr[210];

int getnum(int n)
{
    int ans=0;
    for (int i=0;i<30;i++)if(n&(1<<i))
    {
        arr[ans]=p[i+1];
        ans++;
    }
    return ans;
}

int main()
{
    int t;
    scanf("%d",&t);
    for (int ii=1;ii<=t;ii++)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        for (int i=0;i<201;i++)
            for (int j=0;j<201;j++)
                dp[i][j]=0;
        dp[0][0]=1;

        for (int i=1;i<=n;i++)
            scanf("%lf", &p[i]);

        double ans=0;
        for (int nn=1;nn<(1<<n);nn++)
        {
            int num = getnum(nn);
            if (num!=k)
                continue;
            memset(dp,0,sizeof(dp));
            dp[0][0]=1;
            for (int i=1;i<=k;i++)
            {
                for (int j=0;j<=i;j++)
                {
                    dp[i][j] = dp[i-1][j]*(1-arr[i-1]);
                    if (j)
                        dp[i][j]+=dp[i-1][j-1]*arr[i-1];
                }
            }
            ans=max(ans, dp[k][k/2]);
        }
        printf("Case #%d: ", ii);
        printf("%.12lf\n", ans);
    }
}
