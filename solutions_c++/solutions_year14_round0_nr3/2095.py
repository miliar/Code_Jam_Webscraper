#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cfloat>
#include <ctime>
#include <algorithm>
#include <functional>
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;

const int dx[] = {1, 1, -1, -1, 1, 0, -1, 0};
const int dy[] = {1, -1, 1, -1, 0, 1, 0, -1};
int T;
int R, C, M;
int mapn[128][128];
bool hashn[128][128];
int mode;

int check(int x, int y) {
	if (x < 1 || x > R || y < 1 || y > C) return 0;
	if (hashn[x][y]) return 0;
	if (mapn[x][y] == -1) return 0;

	hashn[x][y] = true;
	if (mapn[x][y] > 0) return 1;

	int ret = 1;
	for (int k = 0; k < 8; k++)
		ret += check(x + dx[k], y + dy[k]);
	return ret;
}

bool DFS(int cnt, int step) {
	if (cnt == 0 || step == R * C) {
		memset(hashn, 0, sizeof hashn);
		int cntp = 0;
		for (int i = 1; i <= R; i++)
			for (int j = 1; j <= C; j++)
				if (!mapn[i][j]) {
					if (check(i, j) != R * C - M) return false;
					else {
						mode = 1;
						return true;
					}
				} else if (mapn[i][j] > 0) cntp++;
		if (cntp == 1) {
			mode = 2;
			return true;
		}
		return false;
	}
	for (int i = step; i < R * C - cnt + 1; i++) {
		int x = i / C + 1;
		int y = i % C + 1;

		int back = mapn[x][y];
		mapn[x][y] = -1;
		for (int k = 0; k < 8; k++) {
			if (x + dx[k] < 1 || x + dx[k] > R || y + dy[k] < 1 || y + dy[k] > C) continue;
			if (mapn[x + dx[k]][y + dy[k]] == -1) continue;
			mapn[x + dx[k]][y + dy[k]]++;
		}

		if(DFS(cnt - 1, i + 1)) return true;

		mapn[x][y] = back;
		for (int k = 0; k < 8; k++) {
			if (x + dx[k] < 1 || x + dx[k] > R || y + dy[k] < 1 || y + dy[k] > C) continue;
			if (mapn[x + dx[k]][y + dy[k]] == -1) continue;
			mapn[x + dx[k]][y + dy[k]]--;
		}
	}
	return false;
}

int main() {
	scanf("%d", &T);
	for (int casen = 1; casen <= T; casen++) {
		printf("Case #%d:\n", casen);

		scanf("%d%d%d", &R, &C, &M);

		memset(mapn, 0, sizeof mapn);
		if (!DFS(M, 0)) puts("Impossible");
		else {
			bool c = false;
			for (int i = 1; i <= R; i++) {
				for (int j = 1; j <= C; j++) {
					if (mapn[i][j] == -1) putchar('*');
					else if ((mapn[i][j] == 0 && !c) || (mapn[i][j] > 0 && mode == 2)) {
						putchar('c');
						c = true;
					} else putchar('.');
				}
				puts("");
			}
		}
	}

	return 0;
}
