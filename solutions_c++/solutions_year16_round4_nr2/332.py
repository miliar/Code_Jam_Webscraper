#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;

#define Clear(a, b) memset(a, b, sizeof a)

typedef long long i64;
typedef double db;

const int N = 2e2 + 10;

int n, m;
db p[N], f[N][N], g[N][N], ans;

int main() {

	int tc;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; ++t) {
		printf("Case #%d: ", t);
		scanf("%d %d", &n, &m);
		for (int i = 1; i <= n; ++i)
			scanf("%lf", &p[i]);
		sort(p + 1, p + n + 1);
		Clear(f, 0);
		f[0][0] = 1;
		for (int i = 0; i < m; ++i)
			for (int j = 0; j <= i; ++j) {
				f[i + 1][j] += f[i][j] * (1 - p[i + 1]);
				f[i + 1][j + 1] += f[i][j] * p[i + 1];
			}
		reverse(p + 1, p + n + 1);
		Clear(g, 0);
		g[0][0] = 1;
		for (int i = 0; i < m; ++i)
			for (int j = 0; j <= i; ++j) {
				g[i + 1][j] += g[i][j] * (1 - p[i + 1]);
				g[i + 1][j + 1] += g[i][j] * p[i + 1];
			}
		ans = 0;
		for (int i = 0; i <= m; ++i) {
			int j = m - i;
			db sum = 0;
			for (int k = 0; k <= m / 2; ++k)
				sum += f[i][k] * g[j][m / 2 - k];
			ans = max(ans, sum); 
		}
		printf("%.10f\n", ans);
	}

	return 0;
}
