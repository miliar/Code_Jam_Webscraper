#include<bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	freopen("prelim-d.in", "r", stdin);
	freopen("prelim-d.res", "w", stdout);

	int t;
	cin >> t;

	for (int i = 1; i <= t; i++) {
		int k, c, s;
		cin >> k >> c >> s;

		cout << "Case #" << i << ": ";

		for (int j = 1; j <= k; j++) {
			cout << j;
			if (j != k) { cout << " "; }
		}

		cout << endl;
	}
}
