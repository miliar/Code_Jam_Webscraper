#include <cstdio>

#define N (1 << 10)

int T, x, y, n, a[N], b[N], c[N], d[N], w[N][N];

int max(int a, int b) {
	return a < b ? b : a;
}

int dist(int a, int b, int c, int d) {
	if (c <= a && a <= d) return 0;
	if (c <= b && b <= d) return 0;
	if (a <= c && c <= b) return 0;
	if (a <= d && d <= b) return 0;
	if (a < c) return c - b;
	return a - d;
}

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d: ", r);
		scanf("%d%d%d", &x, &y, &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d%d%d%d", a + i, b + i, c + i, d + i);
			++c[i]; ++d[i];
		}
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				w[i][j] = max(dist(a[i], c[i], a[j], c[j]), dist(b[i], d[i], b[j], d[j]));
		for (int i = 0; i < n; ++i) {
			w[n][i] = w[i][n] = a[i];
			w[n + 1][i] = w[i][n + 1] = x - c[i];
		}
		w[n][n + 1] = w[n + 1][n] = x;
		n += 2;
		for (int k = 0; k < n; ++k)
			for (int i = 0; i < n; ++i)
				for (int j = 0; j < n; ++j)
					if (w[i][k] + w[k][j] < w[i][j])
						w[i][j] = w[i][k] + w[k][j];
		printf("%d\n", w[n - 2][n - 1]);
	}
	return 0;
}
