#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int t, s_max;
	string s;
	cin >> t;
	int T = t;
	while (t-->0) {
		cin >> s_max >> s;
		int clapping = 0;
		int invite = 0;
		for (int i = 0; i <= s_max; i++) {
			s[i] -= '0';
			if (s[i]) {
				int _ = max(i - clapping, 0);
				invite += _;
				clapping += _ + s[i];
			}
		}
		cout << "Case #" << T - t << ": " << invite << "\n";
	}
	return 0;
}
