#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, -1, 0, 1};
int Test, n, m;
char g[200][200];

bool check_in(int x, int y)
{
	return 0 <= x && x < n && 0 <= y && y < m;
}


bool find(int x, int y, int dir)
{
	while (true) {
		x += dx[dir];
		y += dy[dir];
		if (!check_in(x, y)) return false;
		if (g[x][y] != '.') return true;
	}
	return true;
}

int main(int argc, char **argv)
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &Test);
	for (int Case = 1; Case <= Test; Case ++) {
		scanf("%d%d", &n, &m);
		memset(g, 0, sizeof(g));
		for (int i = 0; i < n; i ++) {
			scanf("%s", g[i]);
		}
		int ans = 0;
		bool ans_impossible = false;
		for (int i = 0; i < n; i ++) {
			for (int j = 0; j < m; j ++) {
				if (g[i][j] != '.') {
					int dir = -1;
					if (g[i][j] == '^') dir = 0;
					if (g[i][j] == '<') dir = 1;
					if (g[i][j] == 'v') dir = 2;
					if (g[i][j] == '>') dir = 3;
					if (find(i, j, dir)) continue;
					ans ++;
					bool flag = false;
					for (int k = 0; k < 4; k ++) {
						if (find(i, j, k)) {
							flag = true;
							break;
						}
					}
					if (!flag) ans_impossible = true;
				}
			}
		}
		printf("Case #%d: ", Case);
		if (ans_impossible) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", ans);
		}
	}
	return 0;
}
