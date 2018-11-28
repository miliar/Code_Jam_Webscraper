#include <bits/stdc++.h>
using namespace std;

int main() {
	int t , kase = 0;
	cin >> t;
	for( ; t--; ) {
		string s;
		int n;
		cin >> s >> n;

		int cnt = 0;
		for(int i = 0; i < s.length() - n + 1; i++) {
			if(s[i] == '-') {
				for(int j = i; j < i + n; j++) {
					s[j] = s[j] == '+' ? '-' : '+';
				}
				cnt++;
			}
		}

		int ok = 1;
		for(int i = 0; i < s.length(); i++) {
			if(s[i] == '-') {
				ok = 0;
			}
		}

		cout << "Case #" << ++kase << ": ";
		if(ok) cout << cnt << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}