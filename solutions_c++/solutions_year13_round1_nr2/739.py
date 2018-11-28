#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;
#define maxn 10001
int v[maxn];
int dp[2][100];
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int T,E,R,N;
	scanf("%d",&T);
	for(int csT = 1; csT <= T; csT++)
	{
		scanf("%d%d%d",&E,&R,&N);
		for(int i = 0; i < N; i++)
			scanf("%d",&v[i]);
		memset(dp,-1,sizeof(dp));
		dp[0][E] = 0;
		int dir = 0;
		int left;
		for(int i = 0; i < N; i++)
		{
			for(int j = 0; j <= E; j++)
			{
				if(dp[dir][j] != -1)
				{
					for(int k = 0; k <= j; k++)
					{
						left = min(E,j - k + R);
						dp[1-dir][left] = max(dp[1-dir][left],dp[dir][j] + k * v[i]);	
					}
				}
			}
			for(int j = 0; j <= E; j++)
			{
				dp[1-dir][j] = max(dp[1-dir][j],dp[dir][j]);
			}
			dir = 1-dir;
		}
		int ans = 0;
		for(int i = 0; i <= E; i++)
		{
			ans = max(ans,dp[dir][i]);
		} 
		printf("Case #%d: %d\n",csT,ans);
	}
	return 0;
}
