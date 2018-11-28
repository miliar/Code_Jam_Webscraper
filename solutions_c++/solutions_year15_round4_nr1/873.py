#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
#include <map>

using namespace std;

const int MAXN = 105;
int T, R, C;

string grid[MAXN];
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
map<char, int> mp;

inline bool valid(int x, int y) {return (x >= 0 && y >= 0 && x < R && y < C);}

inline int solve(int x, int y, int orig = -1) {
	int dir = orig;
	if (orig == -1) {
		dir = mp[grid[x][y]];
	}

	int x_walk = x + dx[dir];
	int y_walk = y + dy[dir];
	while (valid(x_walk, y_walk)) {
		if (grid[x_walk][y_walk] != '.') {
			return 0;
		}
		x_walk += dx[dir];
		y_walk += dy[dir];
	}

	if (orig == -1) {
		for(int d = 0 ; d < 4 ; d++) {
			if (d == dir) {continue;}
			if (solve(x, y, d) >= 0) {
				return 1;
			}
		}
		return -1;
	}	else {
		return -1;
	}
}

int main() {
	mp['^'] = 0;
	mp['v'] = 1;
	mp['<'] = 2;
	mp['>'] = 3;

	cin >> T;
	for(int t = 1 ; t <= T ; t++) {
		cin >> R >> C;
		for(int i = 0 ; i < R ; i++) {
			cin >> grid[i];
		}
		int ans = 0;
		bool impos = false;
		for(int i = 0 ; i < R ; i++) {
			for(int j = 0 ; j < C ; j++) {
				if (grid[i][j] != '.') {
					int ret = solve(i, j);
					if (ret == -1) {
						impos = true;
					}
					ans += ret;
				}
			}
		}
		if (impos) {
			printf("Case #%d: IMPOSSIBLE\n", t);
		}	else {
			printf("Case #%d: %d\n", t, ans);
		}
	}	
	return 0;
}
