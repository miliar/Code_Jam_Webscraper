#include <iostream>
#include <cstdio>
using namespace std;
int t, n, m, g;
double p[220];
double f[2][220];
int main() {
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++) {
			scanf("%lf", &p[i]);
		}
		sort(p, p + n);
		double ans = 0;
		for (int i = 0; i <= m; i++) {
			memset(f, 0, sizeof f);
			g = 0;
			f[g][0] = 1;
			for (int ii = 0; ii < i; ii++) {
				memset(f[1 - g], 0, sizeof f[g]);
				for (int j = 0; j <= m; j++) {
					f[1 - g][j + 1] += f[g][j] * p[ii];
					f[1 - g][j] += f[g][j] * (1 - p[ii]);
				}
				g = 1 - g;
			}
			for (int ii = n - 1; ii >= n - (m - i); ii--) {
				memset(f[1 - g], 0, sizeof f[g]);
				for (int j = 0; j <= m; j++) {
					f[1 - g][j + 1] += f[g][j] * p[ii];
					f[1 - g][j] += f[g][j] * (1 - p[ii]);
				}
				g = 1 - g;
			}
			ans = max(ans, f[g][m / 2]);
		}
		printf("Case #%d: %.9f\n", tt, ans);
	}
}