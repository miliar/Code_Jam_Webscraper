#include <bits/stdc++.h>
using namespace std;

#define SZ(x) ((int)(x).size())

int n, m;
bool vis[4][4];
bool grid[4][4];
bool shape[4][4];
int di[] = {0, 0, 1, -1};
int dj[] = {1, -1, 0, 0};
vector<vector<vector<int>>> shapes =
{
		{},
		{{1}},
		{{3, 17}},
		{{7, 273}, {19, 35, 49, 50}},
		{{15, 4369}, {23, 71, 113, 116, 275, 547, 785, 802},
				{39, 114, 305, 562}, {51}, {54, 99, 306, 561}}
};
void toShape(int msk) {
	memset(shape, 0, sizeof shape);
	for (int b = 0; b < 16; ++b) {
		if ((msk >> b) & 1) {
			int i = b / 4;
			int j = b % 4;
			shape[i][j] = 1;
		}
	}
}
bool toGrid(int si, int sj) {
	memset(grid, 0, sizeof grid);
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			if (shape[i][j]) {
				int ti = si + i;
				int tj = sj + j;
				if (ti >= n || tj >= m) {
					return false;
				}
				grid[ti][tj] = shape[i][j];
			}
		}
	}
	return true;
}
int dfs(int i, int j) {
	if (i < 0 || i >= n || j < 0 || j >= m || vis[i][j] || grid[i][j]) {
		return 0;
	}
	int ret = 1;
	vis[i][j] = true;
	for (int d = 0; d < 4; ++d) {
		int ti = i + di[d];
		int tj = j + dj[d];
		ret += dfs(ti, tj);
	}
	return ret;
}
bool connected(int x) {
	bool ret = true;
	memset(vis, 0, sizeof vis);
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (grid[i][j] == 0 && vis[i][j] == 0) {
				ret &= ((dfs(i, j) % x) == 0);
			}
		}
	}
	return ret;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);
	freopen("D-small-attempt0.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	int id = 0;
	while (t--) {
		int x;
		bool good = false;
		cin >> x >> n >> m;
		for (int k = 0; k < SZ(shapes[x]) && good == false; ++k) {
			good = true;
			for (int l = 0; l < SZ(shapes[x][k]); ++l) {
				toShape(shapes[x][k][l]);
				for (int i = 0; i < n; ++i) {
					for (int j = 0; j < m; ++j) {
						if (toGrid(i, j)) {
							if (connected(x)) {
								good = false;
							}
						}
					}
				}
			}
		}
		cout << "Case #" << ++id << ": ";
		if (good) {
			cout << "RICHARD\n";
		} else {
			cout << "GABRIEL\n";
		}
	}
	return 0;
}
