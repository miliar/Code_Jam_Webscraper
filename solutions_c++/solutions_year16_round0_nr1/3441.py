#include <iostream>
using namespace std;

int addNext(int n, bool *digits) {
	int newDigits = 0;

	do {
		int d = n % 10;
		newDigits += !digits[d];
		digits[d] = true;
		n /= 10;
	} while (n);

	return newDigits;
}

int main(void) {
	int T, N;
	bool digits[10];

	cin >> T;
	for (int testCase = 1; testCase <= T; testCase++) {
		int digitsSeen = 0;

		cin >> N;
		cout << "Case #" << testCase << ": ";

		if (N == 0) {
			cout << "INSOMNIA" << endl;
		} else {
			memset(digits, 0, sizeof(digits));

			for (int i = 1; ; i++) {
				digitsSeen += addNext(N * i, digits);

				if (digitsSeen == 10) {
					cout << N * i << endl;
					break;
				}
			}
		}
	}
}