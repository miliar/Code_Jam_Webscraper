#include <bits/stdc++.h>
using namespace std;

int solve() {
	string s;
	int k, ans = 0;
	cin >> s >> k;
	for(int i = 0; i <= s.length()-k; i++) if(s[i] == '-') {
		ans++;
		for(int j = i; j < i+k; j++) {
			if(s[j] == '-') s[j] = '+';
			else s[j] = '-';
		}
	}
	for(int i = 0; i < s.length(); i++) if(s[i] == '-') return -1;
	return ans;
}

int main() {
	freopen("out.txt", "w", stdout);
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		int res = solve();
		cout << "Case #" << i << ": ";
		if(res >= 0) cout << res << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
}
