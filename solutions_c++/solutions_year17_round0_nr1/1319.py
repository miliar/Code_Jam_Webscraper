#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;

	for (int test = 1; test <= tests; test++) {
		string s;
		int k;
		cin >> s >> k;
		int flips = 0;
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '-') {
				flips++;
				if (i + k > s.length()) {
					flips = -1;
					break;
				}
				for (int j = i; j < i + k; j++) {
					s[j] = ((s[j] == '-') ? '+' : '-');
				}
			}
		}
		cout << "Case #" << test << ": ";
		if (flips == -1) cout << "IMPOSSIBLE";
		else cout << flips;
		cout << endl;
	}
}