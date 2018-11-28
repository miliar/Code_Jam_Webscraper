#include <cstdio>
#include <cstring>
#include <algorithm>

using std::max;

#define N 200
#define B 205

int T, n, m, a[N + 9];
double p[N + 9];
double f[N + 9][2 * N + 9];
double ans;

void dfs(int k, int s) {
	if (s == m) {
		memset(f, 0, sizeof f);
		f[0][B] = 1.0;
		for (int i = 1; i <= m; ++i) {
			for (int j = B - i; j <= B + i; ++j) {
				f[i][j] = f[i - 1][j - 1] * p[a[i]]
						+ f[i - 1][j + 1] * (1 - p[a[i]]);
			}
		}
		if (ans < f[m][B]) ans = f[m][B];
	}
	if (k == n) return;
	dfs(k + 1, s);
	a[s + 1] = k;
	dfs(k + 1, s + 1);
}

int main() {
	scanf("%d", &T);
	for (int tT = 1; tT <= T; ++tT) {
		printf("Case #%d: ", tT);
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) scanf("%lf", p + i);
		ans = 0;
		dfs(0, 0);
		printf("%.8f\n", ans);
	}
	return 0;
}

