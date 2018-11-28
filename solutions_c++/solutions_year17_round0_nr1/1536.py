#include <bits/stdc++.h>
using namespace std;

void solve() {
	string s;
	int k;
	cin >> s >> k;

	int ans = 0;
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '+') {
			continue;
		}
		if (i+k-1 >= s.size()) {
			cout << "IMPOSSIBLE";
			return;
		}
		ans++;
		for (int j = i; j < i+k; j++) {
			s[j] = (s[j] == '-' ? '+' : '-');
		}
	}
	cout << ans;
}

int main() {
	int n; cin >> n;
	for (int i = 0; i < n; i++) {
		cout << "Case #" << (i+1) << ": ";
		solve();
		cout << endl;
	}
	return 0;
}

