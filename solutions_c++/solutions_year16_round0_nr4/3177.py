#include <bits/stdc++.h>

using namespace std;

int main() {
#ifdef ALEXEY
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
#endif
	int t, k, c, s; cin >> t;
	for (int i = 0; i < t; ++i) {
		cin >> k >> c >> s;
		cout << "Case #" << i + 1 << ": ";
		if (k > s) {
			cout << "IMPOSSIBLE" << endl;
			continue;	
		}
		for (int j = 1; j <= s; ++j) {
			cout << j << " ";
		} cout << endl;
	}
	return 0;
}
