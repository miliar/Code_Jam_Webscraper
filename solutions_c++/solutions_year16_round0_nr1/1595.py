
#include <iostream>

using namespace std;

int SLEEP = (1 << 10) - 1;


void addd(int &dig, long long num) {
	while (num > 0) {
		dig |= 1 << (num % 10);
		num /= 10;
	}
}


int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		long long N;
		cin >> N;

		if (N == 0) {
			cout << "INSOMNIA" << endl;
		} else {
			long long c = N;
			int digits = 0;
			addd(digits, c);
			while (SLEEP & digits != SLEEP) {
				c += N;
				addd(digits, c);
			}
			cout << c << endl;
		}
	}
	return 0;
}

