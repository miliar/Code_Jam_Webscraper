#include <bits/stdc++.h>
using namespace std;

int k;

int solve(string &s) {
	int res = 0;
	for(int i = 0; i < s.size(); i++) {
		if(i + k - 1 < s.size()) {
			if(s[i] == '-') {
				res++;
				for(int j = 0; j < k; j++) {
					s[i + j] = "+-"[s[i + j] == '+'];
				}
			}
		} else break;
	}
	for(auto &c: s) if(c == '-') return -1;
	return res;
}

int main() {
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int tc = 1; tc <= t; tc++) {
		cout << "Case #" << tc << ": ";
		string s;
		cin >> s >> k;
		int res = solve(s);
		if(res == -1) cout << "IMPOSSIBLE\n";
		else cout << res << '\n';
	}
	return 0;
}
