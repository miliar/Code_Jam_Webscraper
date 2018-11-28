#include <bits/stdc++.h>
using namespace std;
const int MAXL = 111;
const int MAXNODE = 111 * 111;
const int dx[4] = { -1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};

struct point {
	int x, y;
} p[MAXNODE];

int r, c, n, m, ne, id[MAXL][MAXL];
string mp[MAXL];

int ind[MAXNODE], outd[MAXNODE];

int getDir(char ch) {
	if (ch == '^') return 0;
	if (ch == '>') return 1;
	if (ch == 'v') return 2;
	return 3;
}

inline bool valid(int x, int y) {
	if (x < 0 || x >= r || y < 0 || y >= c) return false;
	return true;
}

void solve(int ca) {
	cout << "Case #" << ca << ": ";
	cin >> r >> c;
	for (int i = 0; i < r; i++) cin >> mp[i];
	n = 0;
	for (int i = 0; i < r; i++) for (int j = 0; j < c; j++) if (mp[i][j] != '.') {
				p[n].x = i;
				p[n].y = j;
				id[i][j] = n;
				n++;
			}
	if (n == 0) {
		puts("0");
		return ;
	}
	memset(ind, 0, sizeof(ind));
	memset(outd, 0, sizeof(outd));
	for (int i = 0; i < r; i++) for (int j = 0; j < c; j++) if (mp[i][j] != '.') {
				int dir = getDir(mp[i][j]), x = i, y = j;
				while (valid(x + dx[dir], y + dy[dir]) && mp[x + dx[dir]][y + dy[dir]] == '.') {
					x += dx[dir];
					y += dy[dir];
				}
				if (valid(x + dx[dir], y + dy[dir])) {
					ind[id[x + dx[dir]][y + dy[dir]]]++;
					outd[id[i][j]]++;
				}
			}
	int res = 0;
	for (int i = 0; i < n; i++) if (ind[i] == 0 && outd[i] == 0) {
			bool found = false;
			for (int j = 0; j < 4; j++) {
				int x = p[i].x, y = p[i].y;
				while (valid(x + dx[j], y + dy[j]) && mp[x + dx[j]][y + dy[j]] == '.') {
					x += dx[j];
					y += dy[j];
				}
				if (valid(x + dx[j], y + dy[j])) {
					found = true;
					break;
				}
			}
			if (!found) {
				cout << "IMPOSSIBLE" << endl;
				return ;
			}
			res++;
		}
	for (int i = 0; i < n; i++) if (outd[i] == 0 && ind[i] != 0) res++;
	cout << res << endl;
}

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) solve(i + 1);
	return 0;
}