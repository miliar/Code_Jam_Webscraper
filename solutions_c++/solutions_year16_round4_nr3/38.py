#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

const int N = 100 + 5;
const int DX[] = {-1, 1, 1, -1};
const int DY[] = {1, 1, -1 ,-1};

int n, m;
int love[N << 2];
char ret[N][N];
int vis[N][N];
pair<int, int> start, goal;

pair<int, int> getPosition(int id, int which)
{
	if (id < m) return make_pair(0, id + which);
	if (id < m + n) return make_pair(id - m + which, m);
	if (id < m + n + m) return make_pair(n, m - (id - (n + m) + which));
	return make_pair(n - (id - (m + n + m) + which), 0);
}

int can(int sx, int sy, int tx, int ty, int d)
{
	if (tx < 0 || tx > n) return false;
	if (ty < 0 || ty > m) return false;
	int bx = min(sx, tx), by = min(sy, ty);
	if (ret[bx][by] != '*') {
		if (ret[bx][by] == '\\') return d % 2 == 1;
		return d % 2 == 0;
	} else {
		if (d % 2 == 1) ret[bx][by] = '\\';
		else ret[bx][by] = '/';
	}
	return true;
}

bool dfs(int x, int y, int dir)
{
	if (x == goal.first && y == goal.second) return true;
	if (vis[x][y]) return false;
	vis[x][y] = true;
	//cout << "!! dfs " << x << ' ' << y << ' ' << dir << endl;
	for(int i = -1; i <= 1; ++ i) {
		int nd = (dir + i + 4) % 4;
		if (can(x, y, x + DX[nd], y + DY[nd], nd)) {
			if (dfs(x + DX[nd], y + DY[nd], nd)) return true;
		}
	}
	return false;
}

bool connect(int u, int v)
{
	start = getPosition(u, 0), goal = getPosition(v, 1);
	//cout << start.first << ' ' << start.second << ' ' << goal.first << ' ' << goal.second << endl;
	int dir;
	if (u < m) dir = 1;
	else if (u < m + n) dir = 2;
	else if (u < m + n + m) dir = 3;
	else dir = 0;
	memset(vis, 0, sizeof vis);
	return dfs(start.first, start.second, dir);
}

bool checkOK()
{
	for(int i = 0; i < n; ++ i) {
		for(int j = 0; j < m; ++ j) {
			if (ret[i][j] == '*') ret[i][j] = '/';
		}
	}
	for(int i = 0; i < (n + m) * 2; ++ i) {
	}
	return true;
}

void solve()
{
	cin >> n >> m;
	for(int i = 0; i < n; ++ i) {
		for(int j = 0; j < m; ++ j) {
			ret[i][j] = '*';
		}
		ret[i][m] = 0;
	}
	for(int i = 0; i < (n + m) * 2; i += 2) {
		int u, v;
		scanf("%d%d", &u, &v);
		--u, --v;
		love[u] = v; love[v] = u;
	}
	vector<int> vec;
	for(int i = 0; i < (n + m) * 2; i ++) {
		vec.push_back(i);
	}
	for( ; vec.size(); ) {
		int x = -1, y = -1;
		for(int i = 0; i < vec.size(); ++ i) {
			int u = vec[i];
			int v = vec[(i + 1) % vec.size()];
			if (love[u] == v) {
				x = u;
				y = v;
				break;
			}
		}
		if (x < 0) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
		if (!connect(x, y)) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
		for(int i = 0; i < vec.size(); ++ i) {
			if (vec[i] == x) {
				vec.erase(vec.begin() + i); break; 
			}
		}
		for(int i = 0; i < vec.size(); ++ i) {
			if (vec[i] == y) {
				vec.erase(vec.begin() + i); break; 
			}
		}
	}
	if (checkOK()) {
		for(int i = 0; i < n; ++ i) {
			cout << ret[i] << endl;
		}
	} else {
		cout << "IMPOSSIBLE" << endl;
	}
}

int main()
{
	//freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out", "w", stdout);
	//freopen("C-small-attempt1.in", "r", stdin); freopen("C-small-attempt1.out", "w", stdout);
	//freopen("C-small-attempt2.in", "r", stdin); freopen("C-small-attempt2.out", "w", stdout);
	freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);
	int test_case;
	cin >> test_case;
	for(int i = 0; i < test_case; ++ i) {
		printf("Case #%d:\n", i + 1);
		cerr << "Start: " << i << endl;
		solve();
	}
	return 0;
}
