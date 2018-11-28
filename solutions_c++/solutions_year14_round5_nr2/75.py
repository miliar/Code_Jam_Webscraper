#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <algorithm>
#include <cstdint>
#include <cmath>
#include <iostream>
using namespace std;
const int maxn = 101;
const int maxh = 201;
const int maxt = 501;
int p, q, n;
int h[maxn], g[maxn];
int f[maxn][maxh][1001];

void init() {
	scanf("%d%d%d", &p, &q, &n);
	for (int i = 0; i < n; i++) {
		scanf("%d%d", &h[i], &g[i]);
	}
}

int dp() {
	memset(f, 0xff, sizeof(f));
	f[0][0][1] = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < h[i]; j++) {
			for (int t = maxt - 1; t >= 0; t--) {
				if (f[i][j][t] < 0) {
					continue;
				}
				if (t != 0) {
					if ((h[i] - j - p) > 0) {
						f[i][j + p][t - 1] = max(f[i][j + p][t - 1], f[i][j][t]);
					} else {
						f[i + 1][0][t - 1] = max(f[i + 1][0][t - 1], f[i][j][t] + g[i]);
					}
				}
				if (t != maxt) {
					if ((h[i] - j - q) > 0) {
						f[i][j + q][t + 1] = max(f[i][j + q][t + 1], f[i][j][t]);
					} else {
						f[i + 1][0][t + 1] = max(f[i + 1][0][t + 1], f[i][j][t]);
					}
				}
				//	printf("%d %d %d %d\n",i, j, t, f[1][1][0]);
			}
		}
	}
	int ans = 0;
	for (int t = 0; t <= maxt; t++) {
		ans = max(ans, f[n][0][t]);
	}
	return ans;
}

int main() {
	int tcase;
	scanf("%d", &tcase);
	for (int i = 1; i <= tcase; i++) {
		init();
		printf("Case #%d: %d\n", i, dp());
	}
	return 0;
}