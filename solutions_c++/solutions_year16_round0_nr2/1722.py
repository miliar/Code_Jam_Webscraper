#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	int t; cin >> t;
	for (int a0 = 0; a0 < t; ++a0) {
		string s; cin >> s;
		int len = s.size(), ans = 0;

		for (int i = len - 1; i >= 0; --i) {
			if (s[i] == '+') continue;
			ans++;
			for (int j = 0; j <= i; ++j) {
				if (s[j] == '+') s[j] = '-';
				else s[j] = '+';
			}
		}

		cout << "Case #" << (a0 + 1) << ": " << ans << endl;
	}
	return 0;
}