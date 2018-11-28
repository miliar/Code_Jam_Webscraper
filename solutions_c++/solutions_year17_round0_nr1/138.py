#include <iostream>
#include <vector>

using namespace std;

void solve(int test) {
	cout << "Case #" << test << ": ";

	string s;
	cin >> s;
	int n = s.length();
	int k;
	cin >> k;
	vector<int> dif(n+1);

	dif[0] = (s[0] == '+');
	for (int i = 1; i < n; ++i) {
		dif[i] = (s[i] == s[i-1]);
		// cout << dif[i];
	}

	int ans = 0;
	for (int i = 0; i < n; ++i) {
		if (dif[i] == 0) {
			++ans;
			if (i + k <= n) {
				dif[i + k] ^= 1;
			} else {
				cout << "IMPOSSIBLE\n";
				return ;
			}
		}
	}

	cout << ans << "\n";
}

int main() {
	int tests;
	cin >> tests;

	for (int k = 1; k <= tests; ++k) {
		solve(k);
	}
}