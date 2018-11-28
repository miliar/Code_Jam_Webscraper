#include <bits/stdc++.h>
using namespace std;
int main() {
	int _;
	cin >> _;
	for(int __ = 0; __ < _;) {
		cout << "Case #" << ++__ << ": ";
		string s;
		cin >> s;
		s += "+";
		int ans = 0;
		for(int i = 1; i < (int)s.size(); i++) ans += (s[i-1] != s[i]);
		cout << ans << "\n";
	}
	return 0;
}
