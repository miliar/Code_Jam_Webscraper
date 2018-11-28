#include <bits/stdc++.h>
using namespace std;

int main () {
	int t; cin >> t;
	for (int T = 1; T <= t; ++T) {
		int ans = 0;
		int n; cin >> n;
		string s; cin >> s;
		int t = 0;
		for (int i = 0; i < s.size(); ++i) {
			int tmp = max(0, i - t);
			t += tmp + s[i] - '0';
			ans += tmp;
		}
		cout << "Case #" << T << ": " << ans << "\n"; 
	}
	return 0;
}
