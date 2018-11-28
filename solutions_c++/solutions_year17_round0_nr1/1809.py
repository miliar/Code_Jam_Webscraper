#include <bits/stdc++.h>
using namespace std;
void solve() {
	string s;
	cin >> s;
	int k;
	cin >> k;
	int ans = 0;
	for (int i=0;i<=s.length()-k;i++) {
		if (s[i] == '-') {
			ans++;
			for (int j=0;j<k;j++) s[i+j] = s[i+j] == '-' ? '+' : '-';
		}
	}
	for (int i=0;i<s.length();i++) if (s[i] == '-') {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	cout << ans << endl;
	return;
}
int main() {
	int t;
	cin >> t;
	for (int i=0;i<t;i++) {
		cout << "Case #" << i+1 << ": ";
		solve();
	}
	return 0;
}