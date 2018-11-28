#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int tc;
	string s;
	cin >> tc;

	for(int i=1; i<=tc; i++) {
		cin >> s;

		int ha = 0;
		int sa = 0;
		bool sad = true;
		int ans = 0;
		for(int j=0; j<s.length(); j++) {
			if(j == 0 && s[j] == '+') sad = false;
			if(s.length() == 1 && s[j] == '-') {
				ans++;
			}
			else if(s[j] == '+' && s[j-1] == '-') {
				if(sad) {
					ans++;
					sad = false;
				}
			}
			else if(s[j] == '-' && s[j-1] == '+') {
				ans += 2;
				sad = false;
			}

			if(s[j] == '+') ha++;
			if(s[j] == '-') sa++;
		}


		if(sa == s.length()) {
			cout << "Case #" << i << ": 1" << endl;
		}
		else if(ha == s.length()) {
			cout << "Case #" << i << ": 0" << endl;
		}
		else {
			cout << "Case #" << i << ": " << ans << endl;
		}
	}

	return 0;
}