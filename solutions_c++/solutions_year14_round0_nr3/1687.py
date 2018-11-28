#include <stdio.h>
#include <string.h>

int r, c, m;
char s[10][10];
bool v[10][10];
int cnt;

void click(int x0, int y0)
{
	v[x0][y0] = true;
	++cnt;
	for (int dx = -1; dx <= 1; ++dx) {
		for (int dy = -1; dy <= 1; ++dy) {
			int x = x0 + dx, y = y0 + dy;
			if (x < 0 || x >= r || y < 0 || y >= c) continue;
			if (s[x][y] == '*') return;
		}
	}
	for (int dx = -1; dx <= 1; ++dx) {
		for (int dy = -1; dy <= 1; ++dy) {
			int x = x0 + dx, y = y0 + dy;
			if (x < 0 || x >= r || y < 0 || y >= c) continue;
			if (!v[x][y]) click(x, y);
		}
	}
}

bool check()
{
	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j) {
			if (s[i][j] == '.') {
				memset(v, 0, sizeof(v));
				cnt = 0;
				click(i, j);
				if (cnt == r * c - m) {
					s[i][j] = 'c';
					return true;
				}
			}
		}
	}
	return false;
}

bool dfs(int x, int y, int z)
{
	if (z == m) return check();
	if (x == r) return false;
	int x0 = x, y0 = y;
	if (++y == c) ++x, y = 0;
	s[x0][y0] = '*';
	if (dfs(x, y, z + 1)) return true;
	s[x0][y0] = '.';
	return dfs(x, y, z);
}

void init()
{
	scanf("%d%d%d", &r, &c, &m);
	memset(s, '.', sizeof(s));
	for (int i = 0; i < r; ++i) s[i][c] = 0;
}

int main()
{
	int dat;
	scanf("%d", &dat);
	for (int cas = 1; cas <= dat; ++cas) {
		init();
		printf("Case #%d:\n", cas);
		if (dfs(0, 0, 0)) {
			for (int i = 0; i < r; ++i) puts(s[i]);
		} else {
			puts("Impossible");
		}
	}
}
