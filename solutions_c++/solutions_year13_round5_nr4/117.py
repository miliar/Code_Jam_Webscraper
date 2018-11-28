#include <cstdio>
double dp[1 << 20];
char s[21];
int main()
{
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; ++ cas)
	{
		scanf("%s", s);
		int now = 0, n = 0;
		for (; s[n]; ++ n)
			if (s[n] == 'X')
				now |= 1 << n;
		int full = 1 << n;
		for (int i = 0; i < full; ++ i)
			dp[i] = 0;
		for (int i = full - 2; i >= 0; -- i)
		{
			if ((i & now) == now)
			{
				for (int j = 0; j < n; ++ j)
					for (int k = j, cost = 0; ; k = (k + 1) % n, ++ cost)
						if (((i >> k) & 1)== 0)
						{
							dp[i] += (dp[i | 1 << k] + n - cost) / n;
							break;
						}
			}
		}
		printf("Case #%d: %.10f\n", cas, dp[now]);
	}
	return 0;
}
