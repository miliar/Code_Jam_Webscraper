#include <iostream>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int _t = 0; _t < t; _t++) {
		string s;
		int k;
		cin >> s >> k;
		int ans = 0;
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '-') {
				if (i + k > s.length()) {
					ans = -1;
					break;
				}
				ans++;
				for (int j = i; j < i + k; j++) {
					s[j] = (s[j] == '-') ? '+' : '-';
				}
			}
		}
		
		cout << "Case #" << (_t + 1) << ": ";
		if (ans == -1) {
			cout << "IMPOSSIBLE";
		} else {
			cout << ans;
		}
		
		cout << endl;
	}
	return 0;
}
