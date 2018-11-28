#include <bits/stdc++.h>
using namespace std;

bool dfs(int k, vector<vector<int>> &a, vector<int> &ord, int used) {
	if (k == ord.size()) return true;
	bool result = true;
	bool one = false;

	for (int i = 0; i < ord.size(); i++) {
		if (a[ord[k]][i] && (~used >> i & 1)) {
			one = true;
			result &= dfs(k + 1, a, ord, used | 1 << i);
		}
	}
	if (!one) return false;
	return result;
}

void solve() {
	int n;
	cin >> n;

	vector<string> g(n);
	for (int i = 0; i < n; i++) cin >> g[i];

	vector<vector<int>> a(n, vector<int>(n));
	for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) a[i][j] = g[i][j] - '0';

	int ans = 1e9;
	for (int ii = 0; ii < 1 << (n * n); ii++) {
		vector<vector<int>> b(n, vector<int>(n));
		int diff = 0;
		bool bad = false;
		for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) {
			if (ii & 1 << (i * n + j)) b[i][j] = 1;
			else {
				if (a[i][j] == 1) bad = true;
			}
			diff += b[i][j] - a[i][j];
		}
		if (bad) continue;

		vector<int> ord(n);
		for (int i = 0; i < n; i++) ord[i] = i;

		bool ok = true;
		do {
			ok &= dfs(0, b, ord, 0);
		} while (next_permutation(ord.begin(), ord.end()));

		
		if (ok) ans = min(ans, diff);
	}
	cout << ans << endl;
}

int main() {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
		solve();
	}
}