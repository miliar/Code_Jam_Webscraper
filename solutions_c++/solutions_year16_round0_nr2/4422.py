#include <iostream>
#include <cstdio>
#include <string>
using namespace std;


int main() {

	freopen("B-large.in", "r", stdin);
	freopen("sol.out", "w", stdout);

	int T; cin >> T;
	for (int test = 1; test <= T; test++) {
		string s; cin >> s;
		int sz = s.length();
		int ans = 0;
		for (int i = sz - 1; i >= 0;i--) {
			if (s[i] == '+') continue;
			for (int j = 0; j <= i; j++)
				s[j] = s[j] == '+'? '-' : '+';
			++ans;
		}
		cout << "Case #" << test << ": " << ans << endl;
	}
}