#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

const int N = 200 + 5;

double a[N];
vector<double> b;
double f[N][N][N], g[N][N][N];
int testCases, n, m;

int main() {
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		scanf("%d%d", &n, &m);
		int t = m;
		m >>= 1;
		for (int i = 0; i < n; ++i) {
			scanf("%lf", &a[i]);
		}
		sort(a, a + n);
		memset(f, 0, sizeof f);
		f[0][0][0] = 1.0;
		for (int i = 0; i < t; ++i) {
			for (int j = 0; j <= m; ++j) {
				for (int k = 0; k <= m; ++k) {
					if (f[i][j][k] == 0.0) {
						continue;
					}
					if (j < m) {
						f[i + 1][j + 1][k] += f[i][j][k] * a[i];
					}
					if (k < m) {
						f[i + 1][j][k + 1] += f[i][j][k] * (1 - a[i]);
					}
				}
			}
		}
		memset(g, 0, sizeof g);
		g[0][0][0] = 1.0;
		for (int i = 0; i < t; ++i) {
			for (int j = 0; j <= m; ++j) {
				for (int k = 0; k <= m; ++k) {
					if (g[i][j][k] == 0.0) {
						continue;
					}
					if (j < m) {
						g[i + 1][j + 1][k] += g[i][j][k] * a[n - 1 - i];
					}
					if (k < m) {
						g[i + 1][j][k + 1] += g[i][j][k] * (1 - a[n - 1 - i]);
					}
				}
			}
		}
		double ans = 0.0;
		for (int l = 0; l <= t; ++l) {
			int r = t - l;
			double tmp = 0.0;
			for (int i = 0; i <= m; ++i) {
				for (int j = 0; j <= m; ++j) {
					tmp += f[l][i][j] * g[r][m - i][m - j];
				}
			}
			ans = max(ans, tmp);
		}
		printf("Case #%d: %.10f\n", _, ans);
	}
	return 0;
}
