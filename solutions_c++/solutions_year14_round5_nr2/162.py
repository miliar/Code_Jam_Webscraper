#include <cstdio>
#include <cstring>
int f[101][1002], h[200], g[200];
void solve() {
	int p, q, n;
	scanf("%d%d%d", &p, &q, &n);
	for (int i = 0; i < n; i++)
		scanf("%d%d", &h[i], &g[i]);
	memset(f, 0xc0, sizeof f);
	f[0][1] = 0;
	for (int i = 0; i < n; i++) {
		int x = (h[i]+q-1)/q;
		int u = (h[i]-1)/q, t = (h[i]-q*u+p-1)/p;
		for (int j = 0; j <= 1001; j++)
			if (f[i][j] >= 0) {
				if (f[i][j] > f[i+1][j+x]) f[i+1][j+x] = f[i][j];
				if (j-t+u >= 0 && f[i][j]+g[i] > f[i+1][j-t+u])
					f[i+1][j-t+u] = f[i][j]+g[i];
			}
	}
	int ans = 0;
	for (int i = 0; i <= 1001; i++)
		if (f[n][i] > ans) ans = f[n][i];
	printf("%d\n", ans);
}
int main() {
	int T; scanf("%d", &T);
	for (int _ = 1; _ <= T; _++)
		printf("Case #%d: ", _), solve();
	return 0;
}
