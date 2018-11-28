#include <bits/stdc++.h>
using namespace std;

int T;
int n, k;
double p[256];
double f[256][256];

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; ++test) {
		printf("Case #%d: ", test);
		scanf("%d%d", &n, &k);
		k /= 2;
		for (int i = 1; i <= n; ++i)
			scanf("%lf", p + i);
		sort(p + 1, p + 1 + n);
		double ans = 0;
		for (int cl = 0; cl <= k * 2; ++cl) {
			memset(f, 0, sizeof(f));
			f[0][0] = 1;
			for (int i = 0; i < cl; ++i)
				for (int j = 0; j <= n; ++j) {
					f[i + 1][j] += f[i][j] * (1 - p[i + 1]);
					f[i + 1][j + 1] += f[i][j] * p[i + 1];
				}
			for (int j = 0; j <= n; ++j)
				f[n - (2 * k - cl)][j] = f[cl][j];
			for (int i = n - (2 * k - cl); i < n; ++i)
				for (int j = 0; j <= n; ++j) {
					f[i + 1][j] += f[i][j] * (1 - p[i + 1]);
					f[i + 1][j + 1] += f[i][j] * p[i + 1];
				}
			if (f[n][k] > ans)
				ans = f[n][k];
		}
		printf("%.15f\n", ans);
	}
	return 0;
}