#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cmath>
#include <string>
#include <cstring>
#include <queue>
#include <vector>
#include <set>
#include <deque>
#include <map>
#include <functional>
#include <numeric>
#include <sstream>
#include <assert.h>

typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int uint;

#define PI 3.1415926535897932384626433832795
#define sqr(x) ((x)*(x))

using namespace std;

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, 1, -1};

int getDir(char x) {
	if (x == '^') return 0;
	if (x == 'v') return 1;
	if (x == '>') return 2;
	if (x == '<') return 3;
	assert(false);
}

int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
	
	int T;
	cin >> T;
	int __it = 0;
	while (T--) {
		int n, m;
		cin >> n >> m;
		vector<string> s(n);
		for (int i= 0; i < n; ++i) {
			cin >> s[i];
		}

		int ans = 0, fail = 0;
		for (int i = 0; i < n && !fail; ++i)
			for (int j = 0; j < m; ++j) if (s[i][j] != '.') {
				int dir = getDir(s[i][j]);

				int x = i + dx[dir], y = j + dy[dir];
				while (x < n && y < m && x >= 0 && y >= 0 && s[x][y] == '.') {
					x += dx[dir];
					y += dy[dir];
				}
				if (!(x < n && y < m && x >= 0 && y >= 0)) {					
					++ans;
					fail = 1;
					for (int d = 0; d < 4; ++d) if (d != dir) {
						int x = i + dx[d], y = j + dy[d];
						while (x < n && y < m && x >= 0 && y >= 0 && s[x][y] == '.') {
							x += dx[d];
							y += dy[d];
						}
						if (x < n && y < m && x >= 0 && y >= 0)	{
							fail = 0;
							break;
						}
					}
				}
				if (fail) break;
			}


		++__it;	
		cout << "Case #" << __it << ": ";
		if (fail) {
			cout << "IMPOSSIBLE" << endl;
		} else
			cout << ans << endl;
	}   
    
    return 0;
}
