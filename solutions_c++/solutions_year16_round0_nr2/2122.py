#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int case_n = 1; case_n <= T; ++case_n) {
		cout << "Case #" << case_n << ": ";
		string s;
		cin >> s;
		s = s + '+';
		int ans = 0;
		for (int i = 1; i < s.length(); ++i) {
			if (s[i] != s[i - 1])
				++ans;
		}
		cout << ans << endl;
	}
	return 0;
}