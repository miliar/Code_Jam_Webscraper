#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <cstdlib>
using namespace std;

typedef long long LL;

int n, m;
map<char, int> arrow_to;

char view[105][105];

const int dx[4] = {-1, 1, 0, 0};
const int dy[4] = {0, 0, -1, 1};


bool walk(int x, int y, int dir) {
	while (true) {
		x += dx[dir];
		y += dy[dir];
		if (x < 0 || x >= n || y < 0 || y >= m) {
			return false;
		}
		if (view[x][y] != '.') return  true;
	}
}


int main() {
	int T, cases = 0;
	scanf("%d", &T);
	arrow_to.clear();
	arrow_to['^'] = 0;
	arrow_to['v'] = 1;
	arrow_to['<'] = 2;
	arrow_to['>'] = 3;
	while (T--) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) {
			scanf("%s", view[i]);
		}
		int ans = 0;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if (view[i][j] != '.') {
					if (walk(i, j, arrow_to[view[i][j]])) {
						continue;
					}
					bool found = false;
					for (int k = 0; k < 4; ++k) {
						if (walk(i,j, k)) {
							found = true;
							++ans;
							break;
						}
					}
					if (!found) {
						ans = -1;
						break;
					}
				}
				if (ans == -1) break;
			}
		}
		printf("Case #%d: ", ++cases);
		if (ans == -1) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", ans);
		}
//		printf("Case #%d:\n", ++cases);
	}
	return 0;
}
