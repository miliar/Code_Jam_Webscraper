#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<math.h>
#include<limits.h>
using namespace std;

long long int n,m,k,mini,dp[1001][1001];

void dfs(long long int x,long long int y,long long int c)
{
	long long int i,j,cnt;
	if(c==k)
	{
            cnt=0;
            for(i=1;i<=n;i++)
            {
                             for(j=1;j<=m-1;j++)
                             {
                                                 if(dp[i][j]==1&&dp[i][j+1]==1)
                                                 cnt++;
                             }
            }
            for(j=1;j<=m;j++)
	        {
		                     for(i=1;i<=n-1;i++)
		                     {
			                                    if(dp[i][j]==1&&dp[i+1][j]==1)
                                                cnt++;
                               }
             }
	         if(cnt<mini)
	         mini=cnt;
	}
	if(c<k)
	{
		if(y<=m)
		{
			dp[x][y]=1;
			dfs(x,y+1,c+1);
			dp[x][y]=0;
			dfs(x,y+1,c);
		}
		else
		{
			if(x<n)
			{
				dp[x+1][1]=1;
				dfs(x+1,2,c+1);
				dp[x+1][1]=0;
				dfs(x+1,2,c);
			}
		}
	}
}
		

int main()
{
	freopen("B-small-attempt0 (2).in","r",stdin); freopen("gcjbout.txt","w",stdout);
	long long int t,T,i,j;
	scanf("%lld",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%lld %lld %lld",&n,&m,&k);
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			dp[i][j]=0;
		}
		mini=10000006;
		dfs(1,1,0);
		printf("Case #%lld: %lld\n",t,mini);
	}
	return 0;
}
	
