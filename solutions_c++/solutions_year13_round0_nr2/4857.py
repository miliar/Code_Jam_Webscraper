#include <climits>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int tn, n, m, h[111][111], r[111], c[111];
	cin >> tn;
	for (int t = 1; t <= tn; ++ t) {
		cin >> n >> m;
		for (int i = 0; i < n; ++ i) r[i] = INT_MIN;
		for (int j = 0; j < m; ++ j) c[j] = INT_MIN;
		for (int i = 0; i < n; ++ i) {
			for (int j = 0; j < m; ++ j) {
				cin >> h[i][j];
				r[i] = max(r[i], h[i][j]);
				c[j] = max(c[j], h[i][j]);
			}
		}
		bool ok = true;
		for (int i = 0; i < n; ++ i)
			for (int j = 0; j < m; ++ j)
				ok = ok && h[i][j] == min(r[i], c[j]);
		cout << "Case #" << t << ": " << (ok ? "YES" : "NO") << endl;
	}
	return 0;
}
