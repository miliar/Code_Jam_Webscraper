#include <cstdio>
int map[1002][1002];
int w, h, b, x1[1002], y1[1002], x2[1002], y2[1002], f[1002], u[1002];
int main() {
	int T; scanf("%d", &T);
	for (int _ = 1; _ <= T; _++) {
		printf("Case #%d: ", _);
		scanf("%d%d%d", &w, &h, &b);
		b += 2;
		x1[0] = y1[0] = x2[0] = 0, y2[0] = h;
		x1[1] = x2[1] = w, y1[1] = 0, y2[1] = h;
		map[0][1] = map[1][0] = w;
		for (int i = 2; i < b; i++) {
			scanf("%d%d%d%d", &x1[i], &y1[i], &x2[i], &y2[i]);
			x2[i]++, y2[i]++;
			for (int j = 0; j < i; j++) {
				int dx = 0, dy = 0;
				if (x2[j] < x1[i]) dx = x1[i] - x2[j];
				else if (x1[j] > x2[i]) dx = x1[j] - x2[i];
				else dx = 0;
				if (y2[j] < y1[i]) dy = y1[i] - y2[j];
				else if (y1[j] > y2[i]) dy = y1[j] - y2[i];
				else dy = 0;
				map[i][j] = map[j][i] = (dx > dy ? dx : dy);
			}
		}
		for (int i = 0; i < b; i++) u[i] = 0, f[i] = ~0U>>1;
		f[0] = 0;
		for (int i = 0; i < b; i++) {
			int min = ~0U>>1, minj = 0;
			for (int j = 0; j < b; j++)
				if (!u[j] && f[j] < min) min = f[j], minj = j;
			u[minj] = 1;
			for (int j = 0; j < b; j++)
				if (f[j] > f[minj] + map[minj][j])
					f[j] = f[minj] + map[minj][j];
		}
		printf("%d\n", f[1]);
	}
	return 0;
}
