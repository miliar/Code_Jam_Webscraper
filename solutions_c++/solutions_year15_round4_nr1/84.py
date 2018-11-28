#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vb> vvb;
typedef vector<vs> vvs;
typedef vector<vl> vvl;

int inf = 0x3f3f3f3f;
double eps = 10e-10;
ll mod = 1000000007ll;

#define rep(k, a, b) for (int k = (a); k < int(b); k++)
#define sz(a) int(a.size())
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define x first
#define y second
#define mi(r, c, v) vvi(r, vi(c, v))
#define rrep(k, a, b) for (int k = (a); k >= int(b); k--)
#define irep(k, a) for (auto& k : (a))
#define md(r, c, v) vvd(r, vd(c, v))
#define mb(r, c, v) vvb(r, vb(c, v))
#define ms(r, c, v) vvs(r, vs(c, v))
#define ml(r, c, v) vvl(r, vl(c, v))
#define mc(r, c, v) vs(r, string(c, v))
#define add(i, j) ((i) + (j)) % mod
#define mul(i, j) ((i) * (j)) % mod
#define bits(n) int(__builtin_popcount(n))

vi dx = { 1, 0, -1, 0 };
vi dy = { 0, 1, 0, -1 };
int r, c;

bool check(vs& grid, int x, int y, int dir) {
	int curx = x + dx[dir], cury = y + dy[dir];
	while (curx >= 0 && curx < r && cury >= 0 && cury < c) {
		if (grid[curx][cury] != '.')
			return true;
		curx += dx[dir];
		cury += dy[dir];
	}
	return false;
}

int main() {
	int T;
	cin >> T;
	rep(X, 0, T) {
		cin >> r >> c;
		vs grid = mc(r, c, '.');
		int change = 0;
		bool poss = true;

		rep(i, 0, r) {
			rep(j, 0, c)
				cin >> grid[i][j];
		}
		rep(i, 0, r) {
			rep(j, 0, c) {
				if (grid[i][j] == '^' && !check(grid, i, j, 2)) {
					if (check(grid, i, j, 0) || check(grid, i, j, 1) || check(grid, i, j, 3))
						change++;
					else {
						poss = false;
						goto endloop;
					}
				} else if (grid[i][j] == 'v' && !check(grid, i, j, 0)) {
					if (check(grid, i, j, 1) || check(grid, i, j, 2) || check(grid, i, j, 3))
						change++;
					else {
						poss = false;
						goto endloop;
					}
				} else if (grid[i][j] == '>' && !check(grid, i, j, 1)) {
					if (check(grid, i, j, 0) || check(grid, i, j, 2) || check(grid, i, j, 3))
						change++;
					else {
						poss = false;
						goto endloop;
					}
				} else if (grid[i][j] == '<' && !check(grid, i, j, 3)) {
					if (check(grid, i, j, 0) || check(grid, i, j, 1) || check(grid, i, j, 2))
						change++;
					else {
						poss = false;
						goto endloop;
					}
				}
			}
		}
	endloop:;

		if (!poss)
			printf("Case #%d: IMPOSSIBLE\n", X + 1);
		else
			printf("Case #%d: %d\n", X + 1, change);
	}
}
