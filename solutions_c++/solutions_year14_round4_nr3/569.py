#include <bits/stdc++.h>

using namespace std;

#define int long long

#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define sqr(x) ((x)*(x))

typedef long long ll;
typedef pair <int, int> pie;

const int maxN = 2000 + 10;

int adj[4][2] = { {0, -1}, {-1, 0}, {0, 1}, {1, 0} };

int w, h, b;
int a[maxN][maxN];
int flag[maxN][maxN];

bool dfs (int x, int y, int D) {
	a[x][y] = 1;
	if (y == h - 1) {
		return true;
	}
	for (int i = 1; i < 4; i++) {
		int nD = (D + i) % 4;
		int xx = x + adj[nD][0];
		int yy = y + adj[nD][1];
		if (xx < 0 || xx >= w || yy < 0 || yy >= h || a[xx][yy]) continue;
		if (dfs (xx, yy, (nD + 2) % 4)) return true;
	}
	return false;
}

int solve() {
	memset (a, 0, sizeof a);

	cin >> w >> h >> b;
	for (int i = 0; i < b; i++) {
		int x0, y0, x1, y1;
		cin >> x0 >> y0 >> x1 >> y1;
		for (int i = x0; i <= x1; i++)
			for (int j = y0; j <= y1; j++)
				a[i][j] = 1;
	}
	int res = 0;
	for (int i = 0; i < w; i++)
		if (!a[i][0]) res += dfs (i, 0, 0);
	return res;
}

main() {
	ios::sync_with_stdio (false);

	int tests; cin >> tests;
	for (int o = 1; o <= tests; o++) {
		int res = solve();
		cout << "Case #" << o << ": " << res << endl; 
	}

	return 0;
}
