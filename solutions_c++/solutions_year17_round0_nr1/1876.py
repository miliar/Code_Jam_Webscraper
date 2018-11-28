#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		string s;
		int k;
		cin >> s >> k;

		size_t n = s.size();
		int cnt = 0;
		for (int i = 0; i < n - k + 1; ++i) {
			if (s[i] == '-') {
				++cnt;
				for (int j = i; j < i + k; ++j) {
					s[j] = (s[j] == '-' ? '+' : '-');
				}
			}
		}
		
		bool ok = true;
		for (int i = n - k + 1; i < n; ++i) {
			if (s[i] == '-') {
				ok = false;
				break;
			}
		}

		cout << "Case #" << test << ": ";
		if (ok) {
			cout << cnt;
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
}
