#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;
const int nmax = 100 + 18;
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};

char a[nmax][nmax];
int R, C, ans;

int trans(char c)
{
	if (c == '^') return 0;
	if (c == 'v') return 1;
	if (c == '<') return 2;
	if (c == '>') return 3;
}

int go(int d, int x, int y)
{
	while (1) {
		x += dx[d];
		y += dy[d];
		if (x <= 0 || x > R || y <= 0 || y > C) {
			return -1;
		}
		if (a[x][y] != '.') return 1;
	}
}

bool work() 
{
	for (int i = 1; i <= R; ++i)
		for (int j = 1; j <= C; ++j) 
			if (a[i][j] != '.') {
				int d = trans(a[i][j]), x = i, y = j;
				int k = go(d, i, j);
				bool ok = 0;
				if (k != -1) continue;
				for (int nd = 0; nd < 4; ++nd) if (nd != d) {
					k = go(nd, i, j);
					if (k != -1) {
						++ans;
						ok = 1;
						break;
					}
				}
				if (!ok) return 0;
			}
	return 1;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases) {
		ans = 0;
		scanf("%d%d", &R, &C);
		for (int i = 1; i <= R; ++i)
			scanf("%s", a[i] + 1);
		printf("Case #%d: ", cases);
		if (work())
			printf("%d\n", ans);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
