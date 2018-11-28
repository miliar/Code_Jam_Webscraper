#include <bits/stdc++.h> 
using namespace std;
int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	cin >> t;
	for (int tst = 1; tst <= t; ++tst) {
		string s;
		cin >> s >> s;
		int ans = 0, curr = 0;
		for (int i = 0; i < s.size(); ++i) {
			ans += max(0, i - curr);
			curr += s[i] - '0' + max(0, i - curr);
		}
		cout << "Case #" << tst << ": " << ans << '\n';
	}
}
