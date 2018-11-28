#include <stdio.h>
#include <string.h>
#include <algorithm>
using std::max;

double p[210];
int indx[210];
double dp[201][201];

int main()
{
	int t;
	memset(dp, 0, sizeof(dp));
	dp[0][0] = 1;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	scanf("%d", &t);
	for (int cases = 1; cases <= t; cases++)
	{
		int n, k;
		scanf("%d%d", &n, &k);
		for (int i = 1; i <= n; i++)
			scanf("%lf", &p[i]);

		double ret = 0;
		for (int nn = 1; nn<(1 << n); nn++)
		{
			int num1s = 0;
			for (int i = 0; i<n; i++)if (nn&(1 << i))
			{
				indx[num1s] = i + 1;
				num1s++;
			}
			if (num1s == k)
			{
				for (int i = 1; i <= k; i++)
				for (int j = 0; j <= i; j++)
					dp[i][j] = dp[i - 1][j] * (1 - p[indx[i - 1]]) + (j>0 ? dp[i - 1][j - 1] * p[indx[i - 1]] : 0);
				ret = max(ret, dp[k][k / 2]);
			}
		}
		printf("Case #%d: %.8lf\n", cases, ret);
	}
}
