#include <iostream>
using namespace std;

int solve(char *s) {
	int flips = 0;

	for (int i = strlen(s) - 1; i >= 0; i--) {
		if (s[i] == (flips % 2 ? '+' : '-')) {
			flips++;
		}
	}

	return flips;
}

int main(void) {
	int T;
	char S[101];

	cin >> T;
	for (int testCase = 1; testCase <= T; testCase++) {
		cin >> S;

		cout << "Case #" << testCase << ": " << solve(S) << endl;;
	}
}