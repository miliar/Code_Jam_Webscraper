#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int N = 111;

int n, m;
char map[N][N];
int glo_i, glo_j;

bool go(int x, int y, char dir) {
	if (x < 1 || x > n || y < 1 || y > m) {
		return true;
	}
	if ((x != glo_i || y != glo_j) && map[x][y] != '.') {
		return false;
	}

	if (dir == '^') {
		return go(x - 1, y, dir);
	} else if (dir == 'v') {
		return go(x + 1, y, dir);
	} else if (dir == '<') {
		return go(x, y - 1, dir);
	} else {
		return go(x, y + 1, dir);
	}
}

int main() {
	int test;
	scanf("%d", &test);
	while (test--) {
		scanf("%d %d", &n, &m);
		for (int i = 1; i <= n; i++) {
			scanf("%s", map[i] + 1);
		}

		bool poss = true;
		int answer = 0;
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				if (map[i][j] == '.') {
					continue;
				}
				glo_i = i;
				glo_j = j;
				if (go(i, j, map[i][j])) {
					answer++;
					if (go(i, j, '^') && go(i, j, 'v') && go(i, j, '<') && go(i, j, '>')) {
						poss = false;
					}
				}
			}
		}
		static int testCount = 0;
		printf("Case #%d: ", ++testCount);
		if (poss) {
			printf("%d\n", answer);
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}