#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <list>
#include <iomanip>
#include <stack>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <ctime>

#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair
#define forn(i,n) for(int i = 0; i < int(n); ++i)
#define sz(a) int(a.size())

using namespace std;

typedef long long li;
typedef long double ld;

const int INF = 1e9;
const ld EPS = 1e-9;

typedef pair<int, int> pt;
#define sqr(x) ((x) * (x))
#define ft first
#define sc second
#define x first
#define y second

int n, m;
const int N = 105;
char c[N][N];

bool read() {
	cin >> n >> m;
	forn (i, n)
		forn (j, m)
		cin >> c[i][j];
	return false;
}

string p = ">v<^";
int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

bool used[N][N];
int fd[N][N];


bool go(int x, int y, int &d, int &lx, int &ly) {
	used[x][y] = true;
	fd[x][y] = d;
	
	if (c[x][y] != '.') {
		d = p.find(c[x][y]);
		lx = x, ly = y;
	}

	int nx = x + dx[d], ny = y + dy[d];
	if (nx < 0 || ny < 0 || nx == n || ny == m) {
		return true;
	}

	if (used[nx][ny])
		return false;
	
	return go(nx, ny, d, lx, ly);
}

int ans = 0;

bool used0[N][N];
bool used1[N][N];

bool go0(int x, int y, int &d) {
	used0[x][y] = true;
	
	if (c[x][y] != '.') {
		d = p.find(c[x][y]);
	}

	int nx = x + dx[d], ny = y + dy[d];
	if (nx < 0 || ny < 0 || nx == n || ny == m) {
		return true;
	}

	if (used0[nx][ny])
		return false;
	
	return go0(nx, ny, d);
}

bool cheap(int x, int y) {
	forn (i, n)
		forn (j, m)
			used0[i][j] = false;
	
	int lx = x, ly = y;
	int d = p.find(c[x][y]);
	
	return !go0(x, y, d);
}

bool ok(int x, int y, bool can = true) {
	forn (i, n)
		forn (j, m)
		used[i][j] = false;

	int lx = x, ly = y;
	int d = p.find(c[x][y]);
	
	if (go(x, y, d, lx, ly)) {
		if (lx == x && ly == y) {
			if (can)
			forn (i, 4) {
				c[x][y] = p[i];
				if (cheap(x, y)) {
					ans++;
					return true;
				}
			}
			if (can)
			forn (i, 4) {
				c[x][y] = p[i];
				if (ok(x, y, false)) {
					ans++;
					return true;
				}
			}
			return false;
		}
		ans++;
		c[lx][ly] = p[(fd[lx][ly] + 2) & 3];
		return true;
	} else
		return true;
}

void solve() {
	ans = 0;
	bool res = true;
	forn (i, n)
		forn (j, m) {
			if (c[i][j] != '.') {
				res &= ok(i, j);
			}
	}
	if (res)
		cout << ans << endl;
	else
		cout << "IMPOSSIBLE" << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	
	int t;
	cin >> t;
	forn (i, t) {
		read();
		cout << "Case #" << i + 1 << ": ";
		solve();
		cerr << i + 1 << endl;
	}
    
    return 0;
}