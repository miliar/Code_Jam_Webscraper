#include <bits/stdc++.h>
using namespace std;

bool check(string s) {
	for (int i = 0; i < s.size(); i++)
		if (s[i] == '-') return false;

	return true;
}

int main(void) {
	int c; cin >> c;

	for (int t = 0; t < c; t++) {
		string s; cin >> s;

		int ans = 0;
		while (!check(s)) {
			int j = 0;
			if (s[0] == '-') {
				while (s[j] == '-'){
				   	s[j] = '+';
					j++;
				}
			} else {
				for (int i = 0; i < s.size(); i++) {
					if (s[i] == '-') {
						for (int j = i-1; j >= 0; j--) s[j] = '-';
						break;
					}
				}
			}
			ans++;
		}
	
		cout << "Case #" << t+1 << ": " << ans << endl;
	}
}
