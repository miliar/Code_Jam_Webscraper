#include <iostream>

using namespace std;

typedef long long number;

bool isJamCoin(int n, int digits[16], number factors[9]) {
	for (int i = 15; i >= 0; i--) {
		digits[i] = n & 1;
		n >>= 1;
	}

	// for (int i = 0; i < 16; i++) cout << digits[i];
	// cout << endl;

	int len = 0;
	for (int base = 2; base <= 10; ++base) {
		number x = 0;
		for (int i = 0; i < 16; ++i) {
			x = base * x + digits[i];
		}

		// cout << "base=" << base << " x=" << x << endl;

		bool prime = true;

		for (number f = 3; f * f <= x;  f += 2)  {
			if (x % f == 0) {
				prime = false;
				factors[len++] = f;
				break;
			}
		}

		if (prime) return false;		
	}

	return true;
}

int main() {
	cout << "Case #1:" << endl;
	number m = 32769;
	number M = 65536;
	for (number j = 0, n = m; n < M && j < 50; n += 2) {
		int digits[16];
		number factors[9];

		if (isJamCoin(n, digits, factors)) {
			for (int i = 0; i < 16; ++i) cout << digits[i];
			for (int i = 0; i < 9; ++i) cout << " " << factors[i];
			cout << endl;
			++j;
		}

		// cerr << n << endl;
	}

	return 0;
}