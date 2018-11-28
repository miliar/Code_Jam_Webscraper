#include <iostream>
#include <string>

using namespace std;

int main() {
	int t; cin >> t;
	for (int tt = 0; tt < t; ++tt) {
		string s; cin >> s;
		int result = 0;
		for (int i = s.length() - 1; i >= 0; --i) {
			if (s[i] == '-') {
				int k = 0;
				while (s[k] == '+') {
					s[k] = '-';
					++k;
				}
				if (k > 0) {
					++result;
				}
				reverse(s.begin(), s.begin() + i + 1);
				for (int j = 0; j <= i; ++j) {
					if (s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
				++result;
			}
		}
		cout << "Case #" << (tt + 1) << ": " << result << endl;
	}
	return 0;
}
