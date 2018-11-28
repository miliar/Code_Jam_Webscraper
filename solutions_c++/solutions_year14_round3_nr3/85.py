#include <iostream>
#include <map>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>

using namespace std;

int n, m, k;
int f[22][22];
int o[22][22];
int ans;
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

void bf(int x, int y) {
	if (x < 0 || x >= n || y < 0 || y >= m)
		return;

	if (o[x][y])
		return;
	if (f[x][y] == 1) {
		o[x][y] = -1;
		return;
	} else {
		o[x][y] = 1;
	}
	for (int i = 0; i < 4; i++) {
		bf(x + dx[i], y + dy[i]);
	}
}

void dfs(int x, int y) {
	if (x >= n) {
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++) {
				o[i][j] = 0;
			}
		for (int i = 0; i < n; i++) {
			bf(i, 0);
			bf(i, m - 1);
		}
		for (int j = 0; j < m; j++) {
			bf(0, j);
			bf(n - 1, j);
		}
		int tmp = 0;
		int t = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (o[i][j] != 1) {
					tmp++;
				}
				t += f[i][j];
			}
		}

		if (tmp >= k)
			ans = min(ans, t);
		return;
	}
	int nx = x;
	int ny = y + 1;
	if (ny == m) {
		nx++;
		ny = 0;
	}
	f[x][y] = 0;
	dfs(nx, ny);
	f[x][y] = 1;
	dfs(nx, ny);
}

void work() {
	cin >> n >> m >> k;
	ans = 1000;
	dfs(0, 0);
	cout << ans << endl;
}

int main() {
	//ios::sync_with_stdio(false);
	freopen("G:/1.in", "r", stdin);
	freopen("G:/1.out", "w", stdout);

	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		work();
	}
	return 0;
}

