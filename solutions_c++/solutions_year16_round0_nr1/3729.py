#include <iostream>
#include "stdlib.h"

using namespace std;

bool track_digits(int n) {
	static int dig[10] = { 0 };
	static int count = 0;

	if (n < 0) {
		memset(dig, 0, sizeof(dig));
		count = 0;
	}

	while (n > 0) {
		int d = n % 10;
		if (dig[d] == 0) {
			dig[d] = 1;
			count++;
		}
		n /= 10;
	}
	return (count == 10);
}

int main() {
	int cases;

	cin >> cases;

	for (int i = 0; i < cases; i++) {
		int n, n_orig;
		cin >> n;
		n_orig = n;
		if (n == 0) cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
		else {
			int count = track_digits(n);
			while (!count) {
				n += n_orig;
				count = track_digits(n);
			}
			cout << "Case #" << i + 1 << ": " << n << endl;
			track_digits(-1);
		}
	}

	return 0;
}