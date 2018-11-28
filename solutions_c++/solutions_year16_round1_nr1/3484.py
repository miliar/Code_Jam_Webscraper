#include <iostream>
#include <string>

using namespace std;

int main() {
	int t, tc = 0;
	string s, ss;
	cin >> t;
	while (t--) {
		cin >> s;
		ss = s[0];
		for (int i = 1; i < s.length(); ++i) {
			if (ss[0] <= s[i]) {
				ss = s[i] + ss;
			} else {
				ss += s[i];
			}
		}
		cout << "Case #" << ++tc << ": " << ss << endl;
	}
	return 0;
}