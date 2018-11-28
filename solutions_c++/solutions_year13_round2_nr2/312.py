#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;
#define maxn 2000
double dp[maxn][maxn];
int GetLeveL(int X,int Y)
{
	return (abs(X) + abs(Y)) / 2;
}
int GetNum(int lv)
{
	return lv * lv * 2 - lv;
}
int main()
{
	freopen("B-large.in","r",stdin);

	freopen("B-large.out","w",stdout);
	double ans;
	int T,X,Y,N;
	scanf("%d",&T);
	for(int csT = 1; csT <= T; csT++)
	{
		scanf("%d",&N);
		scanf("%d%d",&X, &Y);
		int lv = GetLeveL(X,Y) + 1;
		if(GetNum(lv) <= N)
		{
			ans = 1.0;
		}
		else if(GetNum(lv-1) >= N)
		{
			ans = 0.0;
		}else
		{
			if(Y == (lv - 1) * 2)
				ans = 0.0;
			else
			{
				ans = 0.0;
				int leftN = N - GetNum(lv - 1);
				dp[0][0] = 1.0;
				for(int i = 1; i <= leftN; i++)
				{
					for(int j = 0; j <= 2 * lv - 2 && i - j >= 0; j++)
					{
						dp[j][i-j] = 0.0;
						if(i - j > 2 * lv - 2)
							continue;
						if(i - j - 1 >= 0)
						{
							if(j == 2 * lv - 2)
								dp[j][i-j] += dp[j][i-1-j];
							else
								dp[j][i-j] += dp[j][i-1-j] * 0.5;
						}

						if(j - 1 >= 0)
						{
							if(i - j == lv * 2 - 2)
								dp[j][i-j] += dp[j-1][i-j];
							else
								dp[j][i-j] += dp[j-1][i-j]*0.5;
						}
						if(j >= Y + 1 && i == leftN)
							ans += dp[j][i-j];
					}
					
				}
			}
		}
		printf("Case #%d: %.8lf\n",csT,ans);
	}
	return 0;
}
