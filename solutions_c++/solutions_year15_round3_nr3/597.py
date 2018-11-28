#include <stdio.h>
#include <algorithm>
#include <memory.h>
#include <iostream>
#include <string>
using namespace std;
int t, i, j, c,d,v, dp[30][50], ans, k, val[10], mn;

bool check(int b)
{
	for (int a = 1; a <= v; a++)
		if (!dp[b][a])
			return false;
	return true;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("s_out.out", "w", stdout);
	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		memset(dp, 0, sizeof(dp));
		scanf("%d%d%d", &c, &d, &v);
		for (j = 0; j < d; j++)
			scanf("%d", val + j);
		dp[0][val[0]]++;
		for (j = 1; j < d; j++)
		{
			dp[j][val[j]]++;
			for (k = 0; k <= v; k++)
			{
				if (dp[j - 1][k]||(val[j]<=k && dp[j-1][k-val[j]]))
				{

					dp[j][k]=1;
				}
			}
		}
		ans = 0;
		j--;
		while (!check(j))
		{
			for (k = 1; k <= v; k++)
			{
				if (!dp[j][k])
					break;
			}
			
			j++;
			val[j] = k;
			dp[j][val[j]] = 1;
			for (k = 0; k <= v; k++)
			{
				if (dp[j - 1][k] || (val[j]<k && dp[j - 1][k - val[j]]))
				{

					dp[j][k] = 1;
				}
			}
			ans++;
		}




		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}