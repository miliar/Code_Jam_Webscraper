#include <bits/stdc++.h>
using namespace std;
char G[105][105];
int DX[4] = {0, 1, 0, -1};
int DY[4] = {1, 0, -1, 0};
int R, C;
int DIRS[256];
bool gooff(int y, int x, int dir) {
	for (;;) {
		y += DY[dir];
		x += DX[dir];
		if (y >= R || x >= C || y < 0 || x < 0) return true;
		if (G[y][x] != '.') return false;
	}
}
int main() {
	DIRS['^'] = 2;
	DIRS['>'] = 1;
	DIRS['<'] = 3;
	DIRS['v'] = 0;
	int TC;
	scanf("%d", &TC);
	for (int cn = 1; cn <= TC; ++cn) {
		int ans = 0;
		scanf("%d%d", &R, &C);
		for (int i = 0; i < R; ++i)
			scanf("%s", G[i]);
		bool impossible = false;
		for (int i = 0; i < R; ++i)
			for (int j = 0; j < C; ++j) {
				// Check if go off the grid
				if (G[i][j] == '.') continue;
				if (gooff(i, j, DIRS[G[i][j]])) ++ans;
				bool good = false;
				for (int d = 0; d < 4; ++d)
					if (!gooff(i, j, d)) good = true;
				if (!good) {
					impossible = true;
					break;
				}
			}
		printf("Case #%d: ", cn);
		if (impossible) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
}

