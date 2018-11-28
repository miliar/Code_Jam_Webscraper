#include <cstdio>
#include <cstring>
#include <algorithm>

using std::max;

const int MAXN = 210;

int h[MAXN], g[MAXN], f[MAXN][2012][2];

int n, my, tower, m;

inline int Need(int x) {
	int tmp = (x % tower == 0 ? tower : x % tower);
	return tmp / my - (tmp % my == 0);
}

inline int Can(int x) {
	return x / tower - (x % tower == 0);
}

int main(void) {
	 freopen("in", "r", stdin);
	 freopen("out", "w", stdout);
	int kase; scanf("%d", &kase); for (int _ = 1; _ <= kase; _++) {
		memset(f, 0, sizeof f); memset(g, 0, sizeof g); memset(h, 0, sizeof h);
		printf("Case #%d: ", _);
		scanf("%d%d%d", &my, &tower, &n); 
		for (int i = 1; i <= n; i++) scanf("%d%d", h + i, g + i); m += 10 * n;
		for (int i = n; i >= 1; i--) {
			for (int j = 0; j <= m; j++) {
				int tmp = (h[i] + my - 1) / my;
				if (tmp <= j) {
					f[i][j][0] = max(f[i][j][0], f[i + 1][j - tmp][0] + g[i]);
					f[i][j][1] = max(f[i][j][1], f[i + 1][j - tmp][1] + g[i]);
				}
				for (int k = 0; k <= j && k * my < h[i]; k++) {
					int res = h[i] - k * my;
					int need = Need(res);
					int can = Can(res);
					f[i][j][1] = max(f[i][j][1], f[i + 1][j - k + can + 1 - (can == 0)][0]);
					if (can > need) f[i][j][1] = max(f[i][j][1], f[i + 1][j - k + can - need - 1][1] + g[i]);
					f[i][j][0] = max(f[i][j][0], f[i + 1][j - k + can + 1][0]);
					if (can >= need) f[i][j][0] = max(f[i][j][0], f[i + 1][j - k + can - need][1] + g[i]);
				}
			}
		}
		printf("%d\n", f[1][0][0]);
	}
}

