#include <bits/stdc++.h>

using namespace std;

void solve(int k, int c, int s) {
	cout << "1";
	for(int i = 2; i <= s; i++) {
		cout << " " << i;
	}

	cout << endl;
}

int main() {
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";

		int k, c, s;
		cin >> k >> c >> s;
		solve(k, c, s);
	}

	return 0;
}
