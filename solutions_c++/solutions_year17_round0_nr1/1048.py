#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		string s; int n; int ans = 0;
		cin >> s >> n;
		for (int i = 0; i <= (int)s.size()-n; i++) {
			if (s[i] == '-') {
				for (int j = i; j < i+n; j++) {
					if (s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
				ans++;
			}
		}
		bool impos = false;
		for (int i = 0; i < (int)s.size(); i++) {
			if (s[i] == '-') {
				impos = true;
				break;
			}
		}
		if (impos) {
			cout << "Case #" << tt << ": IMPOSSIBLE\n";
		} else {
			cout << "Case #" << tt << ": " << ans << "\n";
		}
	}
}