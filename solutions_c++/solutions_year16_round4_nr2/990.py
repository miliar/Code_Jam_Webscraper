#include<cstdio>
#include<cstring>
#include<algorithm>
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;

int n, k;
int num[20], cnt;
double p[20];
double dp[20][10];
double ans;

void dfs(int no)
{
    if(cnt - 1 == k)
    {
        dp[0][0] = 1;
        for(int i = 1; i <= k; i ++)
        {
            int max1 = min(i, k / 2);
            for(int j = max1; j >= 0; j --)
            {
                if(j > 0)
                {
                    dp[i][j] = dp[i - 1][j - 1] * p[num[i]] + dp[i - 1][j] * (1 - p[num[i]]);
                }
                else
                {
                    dp[i][j] = dp[i - 1][j] * (1 - p[num[i]]);
                }
                //printf("%d %d %lf\n",i,j,dp[i][j]);
            }
        }
        ans = max(ans, dp[k][k / 2]);
        return;
    }
    if(k - cnt > n - no) return;
    for(int i = no; i < n; i ++)
    {
        num[cnt++] = i;
        dfs(i + 1);
        cnt --;
    }
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int ii = 1; ii <= t; ii ++)
	{
	    scanf("%d%d",&n,&k);
	    for(int i = 0; i < n; i ++)
        {
            scanf("%lf",&p[i]);
        }
        mem(dp,0);
        ans = 0;
        cnt = 1;
        dfs(0);
        printf("Case #%d: %lf\n",ii,ans);
	}
	return 0;
}
