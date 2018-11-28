#include <iostream>
#include <string>
#include <set>
#include <algorithm>


using namespace std;

const int N = 1050;
int w, h, b;
int a[N][N];
int x0[N], x1[N], y0[N], y1[N];
int d[N], v[N];

int abs(int x) { return x > 0 ? x : -x; }

int edge(int x, int y, int l, int r, int yy) {
	if (l <= x && x <= r) return abs(yy - y);
	return 1e9;
}

int dis(int x, int y, int j) {
	int tmp = 1e9;

	tmp = min(tmp, max(abs(x - x0[j]), abs(y - y0[j])));
	tmp = min(tmp, max(abs(x - x0[j]), abs(y - y1[j])));
	tmp = min(tmp, max(abs(x - x1[j]), abs(y - y0[j])));
	tmp = min(tmp, max(abs(x - x1[j]), abs(y - y1[j])));

	tmp = min(tmp, edge(x, y, x0[j], x1[j], y1[j]));
	tmp = min(tmp, edge(x, y, x0[j], x1[j], y0[j]));
	tmp = min(tmp, edge(y, x, y0[j], y1[j], x1[j]));
	tmp = min(tmp, edge(y, x, y0[j], y1[j], x0[j]));

	return tmp - 1;
}

void solve() {
	cin >> w >> h >> b;
	int m = b + 1;
	int n = b;
	for (int i = 0; i < b; i++) {
		cin >> x0[i] >> y0[i] >> x1[i] >> y1[i];
		a[i][n] = a[n][i] = x0[i];
		a[i][m] = a[m][i] = w - 1 - x1[i];
	}
	for (int i = 0; i < b; i++)
	for (int j = 0; j < b; j++) {
		a[i][j] = 1e9;
		a[i][j] = min(a[i][j], dis(x0[i], y0[i], j));
		a[i][j] = min(a[i][j], dis(x0[i], y1[i], j));
		a[i][j] = min(a[i][j], dis(x1[i], y0[i], j));
		a[i][j] = min(a[i][j], dis(x1[i], y1[i], j));
		a[i][j] = min(a[i][j], dis(x0[j], y0[j], i));
		a[i][j] = min(a[i][j], dis(x0[j], y1[j], i));
		a[i][j] = min(a[i][j], dis(x1[j], y0[j], i));
		a[i][j] = min(a[i][j], dis(x1[j], y1[j], i));
	}
	a[n][m] = a[m][n] = w;

	for (int i = 0; i <= m; i++) d[i] = 1e9, v[i] = 0;
	d[n] = 0;
	for (int i = 0; i <= m && !v[m]; i++) {
		int k, l = 1e9;
		for (int j = 0; j <= m; j++)
		if (!v[j] && l > d[j])
			k = j, l = d[j];
		v[k] = 1;
		for (int j = 0; j <= m; j++)
		if (!v[j] && d[j] > d[k] + a[k][j])
			d[j] = d[k] + a[k][j];
	}
	cout << d[m] ;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		cerr << "Case #" << t << ": ";
		solve();
		cout << endl;
		cerr << "Done" << endl;
	}
}