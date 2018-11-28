#include <iostream>
using namespace std;

int atoix(char c) {
	return (int) (c - '0');
}

int main() {
	int T, sm;
	string str;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		cout << "Case #" << test << ": ";
		cin >> sm >> str;
		long long p = 0;
		long long ans = 0;
		for (int i = 0; i <= sm; ++i) {
			if (i > p) {
				ans += (i - p);
				p += (i - p);
			}
			p += atoix(str[i]);
		}
		cout << ans << "\n";
	}
	return 0;
}