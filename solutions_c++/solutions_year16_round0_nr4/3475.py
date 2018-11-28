#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << test << ":";
		if (k == 1 || c == 1) {
			if (s >= k) {
				for (int i = 1; i <= k; ++i) {
					cout << " " << i;
				}
				cout << endl;
			} else {
				cout << "IMPOSSIBLE" << endl;
			}
		} else if (s >= k - 1) {
			for (int i = 2; i <= k; ++i) {
				cout << " " << i;
			}
			cout << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	}
}
