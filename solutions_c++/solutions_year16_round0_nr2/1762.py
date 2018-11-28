#include <string>
#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int compute_flips(string s) {
	int c[150];
	int num_flip = 0;
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == '+') c[i] = 1; else c[i] = 0;
	}

	for (int i = s.length()-1; i >= 0; i--) {
		if (c[i] == 0) {
			if (c[0] == 1) {
				for (int j = 0; j < s.length(); j++) {
					if (c[j] == 1) c[j] = 0; else break;
				}
				num_flip++;
			}

			reverse(c, c + i+1);
			for (int j = 0; j <= i; j++) {
				c[j] = 1 - c[j];
			}

			num_flip++;
		}
	}

	return num_flip;
}

int main() {
	string s;
	int tests, n;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> tests;

	for (int t = 1; t <= tests; t++) {
		cin >> s;

		printf("Case #%d: %d\n", t, compute_flips(s));
	}

	return 0;
}