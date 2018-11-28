#include <iostream>
#include <string>

using namespace std;

int main() {
	int t;
	cin >> t;

	for (int c = 1; c <= t; c++) {
		string s;
		cin >> s;

		char cur = s[0];
		int numFlips = 0;
		for (int i = 1; i < s.length(); i++) {
			if (s[i] != cur) {
				numFlips++;
				cur = s[i];
			}
		}

		if (s[s.length() - 1] == '-') {
			numFlips++;
		}

		cout << "Case #" << c << ": " << numFlips << endl;
	}
}