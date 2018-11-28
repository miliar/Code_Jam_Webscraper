#include <stdio.h>

const int MAXR = 120, MAXC = 120;
int r, c;
char s[MAXR][MAXC];
const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};
int dir[128];
int ans;

void init()
{
	scanf("%d%d", &r, &c);
	for (int i = 0; i < r; ++i) scanf("%s", s[i]);
}

bool inrange(int x, int y)
{
	return x >= 0 && x < r && y >= 0 && y < c;
}

bool check(int x, int y, int d)
{
	x += dx[d], y += dy[d];
	while (inrange(x, y)) {
		if (s[x][y] != '.') return true;
		x += dx[d], y += dy[d];
	}
	return false;
}

int check(int x, int y)
{
	int d = dir[s[x][y]];
	if (check(x, y, d)) return 0;
	for (int i = 0; i < 4; ++i) {
		if (i != d && check(x, y, i)) return 1;
	}
	return -1;
}

bool solve()
{
	ans = 0;
	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j) {
			if (s[i][j] == '.') continue;
			int ret = check(i, j);
			if (ret < 0) return false;
			ans += ret;
		}
	}
	return true;
}

int main()
{
	dir['^'] = 0;
	dir['>'] = 1;
	dir['v'] = 2;
	dir['<'] = 3;
	int dat;
	scanf("%d", &dat);
	for (int cas = 1; cas <= dat; ++cas) {
		init();
		printf("Case #%d: ", cas);
		if (solve()) printf("%d\n", ans);
		else puts("IMPOSSIBLE");
	}
}
