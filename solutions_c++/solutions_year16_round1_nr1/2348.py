#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen ("in.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tc = 1; tc <= t; tc++) {
		string s, ret = "";
		cin >> s;
		ret += s[0];
		for(int i = 1; i < s.length(); i++) {
			if(s[i] >= ret[0]) ret = s[i] + ret;
			else ret = ret + s[i];
		}
		cout << "Case #" << tc << ": " << ret << "\n";
	}
	return 0;
}