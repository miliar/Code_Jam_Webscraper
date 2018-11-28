#include <bits/stdc++.h>
using namespace std;

int main() {
	int t; cin >> t;
	for (int k = 1; k <= t; k++) {

		string s; cin >> s;

		int ans = 0;
		for (int i = 1; i < s.size(); i++) {
			if (s[i-1] != s[i]) {
				ans++;
			}
		}
		if (s.back() != '+') {
			ans++;
		}

		cout << "Case #" << k << ": " << ans << endl;
	}
	return 0;
}

