#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <ctime>

#define inf 0x3f3f3f3f
#define Inf 0x3FFFFFFFFFFFFFFFLL
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define Rep(i, n) for (int i = 1; i <= (n); ++i)
#define clr(x, a) memset(x, (a), sizeof x)
using namespace std;
typedef long long ll;
int const N = 111;
char mp[N][N];
int const dir[4][2] = {
	-1, 0,
	0, 1,
	1, 0,
	0, -1
};
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a-large-ans.txt", "w", stdout);
	int T, ca = 1;
	scanf("%d", &T);
	while (T--) {
		int n, m;
		scanf("%d%d", &n, &m);
		rep(i, n) scanf(" %s", mp[i]);
		int ans = 0; bool valid = 1;
		rep(i, n) rep(j, m) {
			int d;
			if (mp[i][j] == '.') continue;
			if (mp[i][j] == '^') d = 0;
			else if (mp[i][j] == '>') d = 1;
			else if (mp[i][j] == 'v') d = 2;
			else d = 3;

			int x = i, y = j;
			bool ok = 0;
			while (1) {
				x += dir[d][0], y += dir[d][1];
				if (x >= 0 && x < n && y >= 0 && y < m) {
					if (mp[x][y] != '.') {
						ok = 1;
						break;
					}
				} else {
					break;
				}
			}
			if (!ok) {
				rep(k, 4) if (k != d) {
					x = i, y = j;
					while (1) {
						x += dir[k][0], y += dir[k][1];
						if (x >= 0 && x < n && y >= 0 && y < m) {
							if (mp[x][y] != '.') {
								ok = 1;
								break;
							}
						} else {
							break;
						}
					}
					if (ok) break;
				}
				if (ok) {
					++ans;
				} else {
					valid = 0;
					break;
				}
			}
		}
		if (!valid) printf("Case #%d: IMPOSSIBLE\n", ca++);
		else printf("Case #%d: %d\n", ca++, ans);
	}
	return 0;
}

