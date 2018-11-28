#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

const int LIM = 101;

int main() {
	int n_tests;
	cin >> n_tests;

	for (int test = 0; test < n_tests; ++test) {
		int n, m;
		cin >> n >> m;

		vector< vector<int> > a(n, vector<int>(m));
		set<int> s;

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				cin >> a[i][j];
				s.insert(a[i][j]);
			}
		}

		vector<int> c(s.begin(), s.end());
		reverse(c.begin(), c.end());

		vector< vector<int> > b(n, vector<int>(m, c[0]));

		bool possible = true;
		for (int k = 1; k < c.size() && possible; ++k) {
			for (int i = 0; i < n && possible; ++i) {
				for (int j = 0; j < m && possible; ++j) {
					if (a[i][j] != c[k]) {
						continue;
					}

					int row = 0;
					for (row = 0; row < n; ++row) {
						if (a[row][j] > c[k]) {
							break;
						}
					}
					if (row == n) {
						for (row = 0; row < n; ++row) {
							b[row][j] = c[k];
						}
						continue;
					}

					int col = 0;
					for (col = 0; col < m; ++col) {
						if (a[i][col] > c[k]) {
							break;
						}
					}
					if (col == m) {
						for (col = 0; col < m; ++col) {
							b[i][col] = c[k];
						}
						continue;
					}
					possible = false;
				}
			}
		}

		if (a != b) {
			possible = false;
		}

		string ans = possible ? "YES" : "NO";
		cout << "Case #" << test + 1 << ": " << ans << endl;
	}

	return 0;
}
