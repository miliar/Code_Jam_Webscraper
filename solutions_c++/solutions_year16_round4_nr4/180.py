#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

typedef vector<string> vs;

bool check(vs g, int mw, int mj) {
	int n = g.size();
	if (mw + 1 == (1 << n)) {
		return true;
	}

	for (int i = 0; i < n; ++i) if ((mw & (1 << i)) == 0) {
		int cj = (1 << n) - 1 - mj;
		for (int j = 0; j < n; ++j) if (cj & (1 << j))
			if (g[i][j] == '0') cj ^= 1 << j;

		if (cj == 0) 
			return false;

		for (int j = 0; j < n; ++j) if (cj & (1 << j))
		{
			if (check(g, mw + (1 << i), mj + (1 << j)) == false)
				return false;
		}
	}

	return true;
}

void solve() {
	int n;
	cin >> n;
	vs f(n); for (int i = 0; i < n; ++i) cin >> f[i];

	int res = n * n;

	for (int m = 0; m < (1 << (n*n)); ++m) {
		int cost = 0;
		vs g = f;
		for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) {
			int c = (i * n) + j;
			if (m & (1 << c)) {
				++cost;
				g[i][j] = '1';
			}
		}
		if (check(g, 0, 0))
			res = min(res, cost);
	}

	static int test_id;
	cout << "Case #" << ++test_id << ": " << res << endl;
	cerr << "Case #" << test_id << ": " << res << endl;
}

int main() {
	int t;
	cin >> t;
	while (t --> 0) solve();
	return 0;
}