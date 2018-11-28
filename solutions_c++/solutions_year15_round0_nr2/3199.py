#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
#define maxn 1100
int pre[maxn];

int dp[maxn][maxn];

int gao(int n,int k)
{
    int x=n/k;
    if((n%k)!=0)
        x=x+1;
    return x;
}

int main()
{
    int T;
    scanf("%d",&T);
    int casen=0,i,m,n,j,k;
    while(T--)
    {
        m=0;
        scanf("%d",&n);
	for(i=0;i<n;i++)
	{
	    scanf("%d", pre+i);
	    m=max(m, pre[i]);
	}
        for(i=0;i<m;i++)
            dp[0][i]=0;
        for(i=1;i<=n;i++)
            dp[i][0]=max(dp[i-1][0], pre[i-1]);
        for(i=1;i<=n;i++)
        {
           for(j=1;j<m;j++)
           {
               dp[i][j]=m;
               for(k=j;k>=0;k--)
               {
                   int temp = gao(pre[i-1], j-k+1);
                   int dppre = dp[i-1][k];
                   dp[i][j]=min(dp[i][j], max(dppre, temp));
                   if(temp<dppre)
                       break;
               }
           }
        }
        int ans=m;
        for(i=0;i<m;i++)
           ans=min(ans, dp[n][i]+i);
	printf("Case #%d: %d\n",++casen, ans);
    }
    return 0;
}
