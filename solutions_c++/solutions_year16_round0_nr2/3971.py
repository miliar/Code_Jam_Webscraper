#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int k = 1; k <= t; ++k) {
		string s;
		cin >> s;
		int ans = 0;
		int plus[1000];
		int minus[1000];
		for (int j = 0; j < 1000; ++j) {
			plus[j] = 0;
			minus[j] = 0;
		}
		plus[0] = (s[0] != '+');
		minus[0] = (s[0] != '-');				

		for (int j = 1; j < s.length(); ++j) {
			if (s[j] == '+') {
				plus[j] = plus[j-1];
				minus[j] = 1 + plus[j-1];			
			}

			if (s[j] == '-') {
				minus[j] = minus[j-1];
				plus[j] = 1 + minus[j-1];
			}			
		}
		ans = plus[s.length() - 1];
		cout << "Case #" << k << ": " << ans << endl;
	}
}
