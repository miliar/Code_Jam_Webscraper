#include <bits/stdc++.h>
using namespace std;

void solve() {
	string s;
	int k, c = 0;
	cin >> s >> k;
	for(int i = 0; i <= s.size() - k; ++i) {
		if(s[i] == '-') {
			for(int j = i; j < i + k; ++j) {
				s[j] = s[j] == '-' ? '+' : '-';
			}	
			++c;
		}
	}
	for(int i = s.size() - k + 1; i < s.size(); ++i) {
		if(s[i] == '-') {
			cout << " IMPOSSIBLE\n";
			return;
		}
	}
	cout << ' ' << c << '\n';
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ':';
		solve();
	}
	return 0;
}
