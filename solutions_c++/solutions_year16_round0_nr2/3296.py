/*/**/

#include <bits/stdc++.h>

using namespace std;

set < int > s;

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; tt++) {
		string s;
		cin >> s;
		int ans = 0;
		for(int i = 1; i < s.size(); i++) {
			if(s[i] != s[i - 1]) {
				ans++;
			}
		}
		if(s[s.size() - 1] == '-') {
			ans++;
		}
		cout << "Case #" << tt << ": " << ans << endl;
	}
	return 0;
}
