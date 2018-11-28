#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
using namespace std;

int num_case, n, k;
double a[300], now[300], f[300][300], ans;

void calc()
{
	for (int i = 0; i <= k; i++)
		for (int j = 0; j <= k; j++)
			f[i][j] = 0;
	f[0][0] = 1;
	for (int i = 0; i < k; i++)
		for (int j = 0; j <= i; j++)
		{
			f[i + 1][j] += now[i + 1] * f[i][j];
			f[i + 1][j + 1] += (1 - now[i + 1]) * f[i][j];
		}
	ans = max(ans, f[k][k / 2]);
}

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &num_case);
	for (int icase = 1; icase <= num_case; icase++)
	{
		scanf("%d %d", &n, &k);
		for (int i = 1; i <= n; i++)
			scanf("%lf", &a[i]);
		ans = 0;
		sort(a + 1, a + 1 + n);
		for (int i = 0; i <= k; i++)
		{
			for (int j = 1; j <= i; j++)
				now[j] = a[j];
			for (int j = i + 1; j <= k; j++)
				now[j] = a[n - k + j];
			calc();
		}
		printf("Case #%d: %.10lf\n", icase, ans);
	}
	return 0;
}
