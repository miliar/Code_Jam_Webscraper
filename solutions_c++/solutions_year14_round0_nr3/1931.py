#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
using namespace std;

const int dir[8][2] = { { 0, 1 } , { 1, 1 }, { 1, 0 }, { 1, -1 }, { 0, -1 }, { -1, -1 }, { -1, 0 }, { -1, 1 } };
const int MAXN = 10;

struct Node {
	int x, y;
	Node() {}
	Node(int _x, int _y) {
		x = _x; y = _y;
	}
};
Node q[MAXN*MAXN];

int head, tail;

struct Record {
	int st;
	int px, py;
} rec[MAXN][MAXN][MAXN*MAXN];
int f[MAXN][MAXN][MAXN*MAXN];

int g[MAXN][MAXN], adj[MAXN][MAXN], vis[MAXN][MAXN], mark[MAXN][MAXN];

int n, m;
int st;

void checkState(int egg) {
	if (n * m - egg == 1) {
		for (int sx = 0; sx < n; sx ++)
			for (int sy = 0; sy < m; sy ++) {
				if (g[sx][sy] == 0) {
					Record ans;
					ans.st = st; ans.px = sx; ans.py = sy;
					rec[n][m][egg] = ans;
					f[n][m][egg] = 1;
					return;
				}
			}
		return;
	}
	int mark_area = 0;
	int sx = -1, sy = -1;
	for (int x = 0; x < n; x ++) {
		for (int y = 0; y < m; y ++) {
			if (adj[x][y] == 0) {
				sx = x; sy = y;
				break;
			}
		}
	}
	if (sx == -1 || sy == -1) return;

	head = 0; tail = 0;
	tail++;
	q[tail].x = sx; q[tail].y = sy;
	vis[sx][sy] = 1;

	while (head < tail) {
		head++;
		int cx = q[head].x, cy = q[head].y;

		if (!mark[cx][cy]) {
			mark[cx][cy] = 1;
			mark_area ++;
		}

		for (int di = 0; di < 8; di ++) {
			int tx = cx + dir[di][0];
			int ty = cy + dir[di][1];
			if (tx < 0 || tx >= n || ty < 0 || ty >= m) continue;

			//Not empty, ban!!
			if (g[tx][ty] == 1) continue;

			if (!mark[tx][ty]) {
				mark[tx][ty] = 1;
				mark_area ++;
			}

			if (adj[tx][ty] == 0 && !vis[tx][ty]) {
				tail++;
				q[tail].x = tx; q[tail].y = ty;
				vis[tx][ty] = 1;
			}
		}
	}

	if (mark_area == n*m - egg) {
		Record ans;
		ans.st = st; ans.px = sx; ans.py = sy;
		rec[n][m][egg] = ans;
		f[n][m][egg] = 1;
	}
}

int getAdjCount(int x, int y) {
	if (g[x][y] == 1) {
		return -1;
	}
	int ct = 0;
	for (int di = 0; di < 8; di ++) {
		int tx = x + dir[di][0];
		int ty = y + dir[di][1];
		if (tx < 0 || tx >= n || ty < 0 || ty >= m) continue;
		ct += g[tx][ty];
	}
	return ct;
}

void init() {
	memset(f, 0, sizeof(f));
	for (n = 1; n <= 5; n ++) {
		for (m = 1; m <= 5; m ++) {
			for (st = 0; st < (1<<(n*m)); st ++) {
				int ct = 0;
				for (int x = 0; x < n; x ++) {
					for (int y = 0; y < m; y ++) {
						int id = x * m + y;
						if ((st&(1<<id)) > 0) {
							ct ++;
							g[x][y] = 1;
						} else {
							g[x][y] = 0;
						}
					}
				}

				if (f[n][m][ct]) continue;
				for (int x = 0; x < n; x ++)
					for (int y = 0; y < m; y ++) {
						mark[x][y] = 0;
						vis[x][y] = 0;
						adj[x][y] = getAdjCount(x, y);
					}
				checkState(ct);
			}
			/*
			for (int tot = 0; tot <= (n*m); tot ++) {
			    printf("%d %d %d : %d\n", n, m, tot, f[n][m][tot]);
			}
			*/
		}
	}
}

void work() {
	int T;
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti ++) {
		int n, m, egg;
		scanf("%d%d%d", &n, &m, &egg);
		printf("Case #%d:\n", ti);
		if (f[n][m][egg]) {
			int rec_st = rec[n][m][egg].st;
			int rec_sx = rec[n][m][egg].px;
			int rec_sy = rec[n][m][egg].py;
			for (int x = 0; x < n; x ++) {
				for (int y = 0; y < m; y ++) {
					int id = x * m + y;
					if (x == rec_sx && y == rec_sy)
						printf("c");
					else
						printf("%c", (rec_st & (1<<id))>0 ? '*' : '.');
				}
				printf("\n");
			}
		} else {
			printf("Impossible\n");
		}
	}
}
int main() {
    freopen("C-small.in","r",stdin);
    freopen("C-small.out","w",stdout);
    init();
    work();
    return 0;
}
