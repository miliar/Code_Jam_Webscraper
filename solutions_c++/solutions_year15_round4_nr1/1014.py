#include <stdio.h>
#include <string.h>

char s[110][110];

int dx[] = {0, 1, 0, -1},
	dy[] = {1, 0, -1, 0};

int n, m;
const int INF = 1000000000;

bool valid(int x, int y) {
	return x >= 0 && x < n && y >= 0 && y < m;
}

int check(int x, int y) {
	int v = 0;
	for (int i = 0; i < 4; i++) {
		int xx = x + dx[i];
		int yy = y + dy[i];
		//printf("(%d, %d)\n", xx, yy);
		while (valid(xx, yy)) {
			if (s[xx][yy] != '.') {
				v |= (1 << i);
				break;
			}
			xx += dx[i];
			yy += dy[i];
		}
	}
	return v;
}

int b[256];

int main() {
	int cas;
	scanf("%d", &cas);
	b['>'] = 1 << 0;
	b['v'] = 1 << 1;
	b['^'] = 1 << 3;
	b['<'] = 1 << 2;
	for (int re = 1; re <= cas; re++) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++) {
			scanf("%s", s[i]);
		}
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (s[i][j] == '.') continue;
				int v = check(i, j);
				//printf("(%d, %d)\n", i, j);
				//printf("%d %d\n", v, b[s[i][j]]);
				if (v == 0) {
					cnt = INF;
				} else if (!(v & b[s[i][j]])) {
					cnt++;
				}
			}
		}
		if (cnt < INF) {
			printf("Case #%d: %d\n", re, cnt);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", re);
		}
	}
}