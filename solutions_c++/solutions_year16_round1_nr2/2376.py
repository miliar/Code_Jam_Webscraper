#include <bits/stdc++.h>
using namespace std;

template<class T> ostream &operator <<(ostream &os, const vector<T> &v) { for (T x : v) os << x << " "; return os; }

int n;
vector<vector<int>> a;
int b[50][50];

bool dfs(int k, int row, int col, bool skipped) {
	if (k == 2 * n - 1) {
		bool ok = true;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (i + 1 < n && b[i][j] >= b[i + 1][j]) ok = false;
				if (j + 1 < n && b[i][j] >= b[i][j + 1]) ok = false;
			}
		}
		return ok;
	}

	if (row < n) {
		bool ok = true;
		for (int j = 0; j < col; j++) {
			if (a[k][j] != b[row][j] && b[row][j] != 0) {
				ok = false;
			}
		}
		if (ok) {
			for (int j = 0; j < n; j++) {
				b[row][j] = a[k][j];
			}
			for (int j = 0; j < n; j++) {
				if (row > 0) {
					if (b[row - 1][j] >= b[row][j]) ok = false;
				}
			}
			if (ok) {
				if (dfs(k + 1, row + 1, col, skipped)) return true;
			}
		}
	}

	if (col < n) {
		bool ok = true;
		for (int i = 0; i < row; i++) {
			if (a[k][i] != b[i][col] && b[i][col] != 0) {
				ok = false;
			}
		}
		if (ok) {
			for (int i = 0; i < n; i++) {
				b[i][col] = a[k][i];
			}
			for (int i = 0; i < n; i++) {
				if (col > 0) {
					if (b[i][col - 1] >= b[i][col]) ok = false;
				}
			}
			if (ok) {
				if (dfs(k + 1, row, col + 1, skipped)) return true;
			}
		}
	}

	if (!skipped) {
		for (int j = col; j < n; j++) {
			b[row][j] = 0;
		}
		if (dfs(k, row + 1, col, true)) return true;

		for (int i = row; i < n; i++) {
			b[i][col] = 0;
		}
		if (dfs(k, row, col + 1, true)) return true;
	}

	return false;
}

void solve() {
	cin >> n;

	a.assign(n * 2 - 1, vector<int>(n));
	for (int i = 0; i < n * 2 - 1; i++) {
		for (int j = 0; j < n; j++) {
			cin >> a[i][j];
		}
	}

	sort(a.begin(), a.end(), [](vector<int> l, vector<int> r) {
		return lexicographical_compare(l.begin(), l.end(), r.begin(), r.end());
	});

	memset(b, 0, sizeof(b));
	dfs(0, 0, 0, false);

	map<vector<int>, int> mp;
	for (int i = 0; i < n * 2 - 1; i++) {
		mp[a[i]]++;
	}
	
	for (int i = 0; i < n; i++) {
		vector<int> x, y;
		for (int j = 0; j < n; j++) {
			x.push_back(b[i][j]);
			y.push_back(b[j][i]);
		}
		mp[x]--;
		mp[y]--;
	}

	vector<int> ans;
	for (auto kv : mp) {
		if (kv.second == -1) ans = kv.first;
	}

	cout << ans << endl;
}

int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
}