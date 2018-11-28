#include <bits/stdc++.h>
using namespace std;

void solve() {
	string s;
	cin >> s;
	while (!s.empty() && s.back() == '+') {
		s.pop_back();
	}
	if (s.empty()) {
		cout << 0 << endl;
		return;
	}
	int ans = 1;
	for (int i = 1; i < s.size(); ++i) {
		if (s[i] != s[i - 1]) {
			ans++;
		}
	}
	cout << ans << endl;
	return;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		solve();
	}
}