/*/**/

#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; tt++) {
		int k, c, kc;
		cin >> k >> c >> kc;
		cout << "Case #" << tt << ":";
		for(int i = 1; i <= k; i++) {
			cout << " " << i;
		}
		cout << endl;
	}
	return 0;
}

