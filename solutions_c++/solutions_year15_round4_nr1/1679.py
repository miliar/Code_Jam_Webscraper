#include <iostream>
#include <cassert>
using namespace std;

int dx[] = {-1,1,0,0}, dy[] = {0,0,-1,1};

int A[100][100];

void solve() {
	int m, n; cin >> m >> n;
	auto is_good = [=](int x, int y) { return 0 <= x && x < m && 0 <= y && y < n; };
	auto is_blank = [&](int x, int y) { return A[x][y] == -1; };
	auto goes_over_board = [&](int x, int y, int d) {
		assert (0 <= d && d < 4);
		x += dx[d];
		y += dy[d];
		if (!is_good(x,y)) return true;
		while (is_good(x,y)) {
			if (!is_blank(x,y)) return false;
			x += dx[d];
			y += dy[d];
		}
		return true;
	};
	for (int i = 0; i < m; ++i) {
		string s; cin >> s;
		assert (s.size() == n);
		for (int j = 0; j < n; ++j) {
			if (s[j] == '<') A[i][j] = 2;
			else if (s[j] == '>') A[i][j] = 3;
			else if (s[j] == 'v') A[i][j] = 1;
			else if (s[j] == '^') A[i][j] = 0;
			else if (s[j] == '.') A[i][j] = -1;
			else assert (false);
		}
	}
	int res = 0;
	for (int i = 0; i < m; ++i) for (int j = 0; j < n; ++j) {
		int d = A[i][j];
		if (d == -1) continue;
		if (!goes_over_board(i, j, d)) continue;
		++res;
		bool no_goes_over_board = true;
		for (int d = 0; d < 4; ++d) if (!goes_over_board(i,j,d)) no_goes_over_board = false;
		if (no_goes_over_board) {
			cout << "IMPOSSIBLE";
			return;
		}
	}
	cout << res;
}

int main() {
	// your code goes here
	int t; cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}