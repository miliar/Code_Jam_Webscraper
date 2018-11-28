#include <iostream>
using namespace std;

int t, T, s;

int main() {
	cin >> T;
	for (t = 0; t < T; t ++) {
		cin >> s;
		char c;
		int n = 0;
		int p = 0;
		int total = 0;
		for (int i = 0; i <= s; i ++) {
			cin >> c;
			p = c - '0';
			if (i > n) {
				n = i;
			}
			n += p;
			total += p;
		}
		cout << "Case #" << t + 1 << ": " << n - total << endl;
	}
	return 0;
}