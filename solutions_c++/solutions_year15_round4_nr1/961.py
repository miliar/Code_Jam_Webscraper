#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <queue>
#include <vector>
#include <string>
#include <functional>
using namespace std;

int T, R, C;
int ans, test;
char G[128][128];
const char dir[] = {'<', '>', '^', 'v'};

bool walk(int x, int y, char dir, int ox, int oy) {
	if (x >= R || x < 0 || y >= C || y < 0) return false;
	if ((x != ox || y != oy) && G[x][y] != '.') return true;

	if (dir == '<') return walk(x, y - 1, dir, ox, oy);
	if (dir == '>') return walk(x, y + 1, dir, ox, oy);
	if (dir == 'v') return walk(x + 1, y, dir, ox, oy);
	if (dir == '^') return walk(x - 1, y, dir, ox, oy);
	return false;
}

bool go(int x,int y) {
	if (walk(x, y, G[x][y], x, y)) return true;

	ans++;
	for (int i = 0; i < 4; i++) {
		if (G[x][y] != dir[i])
			if (walk(x, y, dir[i], x, y)) return true;
	}

	return false;
}

int main() {
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &R, &C);
		for (int i = 0; i < R; i++) {
			scanf("%s", G[i]);
		}

		bool flag = true;
		ans = 0;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++){
				if (G[i][j] != '.') 
					if (!go(i,j)) {
						flag = false;
						break;
					}
			}
		}

		if (!flag) {
			printf("Case #%d: IMPOSSIBLE\n", ++test);
		} else {
			printf("Case #%d: %d\n", ++test, ans);
		}



	}

	return 0;
}
