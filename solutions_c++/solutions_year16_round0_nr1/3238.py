#include <iostream>

using namespace std;
const int HIT = 1023;

int main() {
	int T;
	cin >> T;
	long digbit[10];
	long dig = 1L;
	long trace = 0;

	for (int i = 0; i < 10; ++i) {
		digbit[i] = dig;
		trace |= dig;
		dig <<= 1;
	}

	for (int i = 0; i < T; ++i) {
		int N;
		cin >> N;
		if (N == 0) {
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
			continue;
		}
		long digits = 0L;
		long number = 0;
		
		while (digits != HIT) {
			number += N;
			long n = number;
			while (n > 0) {
				int digit = n % 10;
				digits |= digbit[digit];
				n /= 10;
			}
		}
		cout << "Case #" << i+1 << ": " << number << endl;
	}

	return 0;
}
