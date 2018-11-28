#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
using namespace std;

int T;
int R, C, M;

int sx, sy;

const int MAX = 50;
char brd[MAX][MAX];
char buf[MAX][MAX];

int dx[] = { -1, 0, 1, -1, 1, -1, 0, 1 };
int dy[] = { -1, -1, -1, 0, 0, 1, 1, 1 };

#define POW(x) ((x)*(x))
int dist(int d, int x, int y, int a, int b)
{
	switch(d) {
	case 0:
		return POW(x-a)+POW(y-b);
	case 1:
		return abs(x-a)+abs(y-b);
	default:
		return max(abs(x-a), abs(y-b));
	}
}

bool check()
{
	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++)
			if (brd[i][j] == '.')
				return false;
	return true;
}

void rec(int x, int y)
{
	if (brd[y][x] != '.')
		return;

	int cnt = 0;
	for (int d = 0; d < 8; d++) {
		int nx = x+dx[d];
		int ny = y+dy[d];
		if (!(0 <= nx && nx < C)) continue;
		if (!(0 <= ny && ny < R)) continue;
		if (brd[ny][nx] == '*')
			cnt++;
	}
	brd[y][x] = '0'+cnt;
	if (cnt == 0) {
		for (int d = 0; d < 8; d++) {
			int nx = x+dx[d];
			int ny = y+dy[d];
			if (!(0 <= nx && nx < C)) continue;
			if (!(0 <= ny && ny < R)) continue;
			rec(nx, ny);
		}
	}
}

void paint()
{
	brd[sy][sx] = '.';
	rec(sx, sy);
	brd[sy][sx] = 'c';
}

bool sub(int d, int xx, int yy)
{
	sx = xx, sy = yy;
	memset(brd, '.', sizeof(brd));
	brd[sy][sx] = 'c';
	for (int m = 0; m < M; m++) {
		int md = 0;
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++)
				if (brd[i][j] == '.')
					md = max(md, dist(d, sx, sy, j, i));
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++)
				if (brd[i][j] == '.')
					if (md == dist(d, sx, sy, j, i)) {
						brd[i][j] = '*';
						goto NEXT;
					}
NEXT:;
	}
	paint();
	return check();
}

int main()
{
	cin >> T;
	for (int t = 0; t < T; t++) {
		cin >> R >> C >> M;
		int E = R*C-M;
		printf("Case #%d:\n", t+1);

		srand(time(NULL));
		memcpy(buf, brd, sizeof(brd));
		for (int d = 0; d < 3; d++)
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				memcpy(brd, buf, sizeof(brd));
				if (sub(d, j, i)) {
					for (int a = 0; a < R; a++) {
						for (int b = 0; b < C; b++) {
							char c = brd[a][b];
							putchar(isdigit(c)?'.':c);
						}
						putchar('\n');
					}
					goto NEXT;
				}
			}
		}
		printf("Impossible\n");
NEXT:;
	}
	return 0;
}
