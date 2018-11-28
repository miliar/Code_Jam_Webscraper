#include <iostream>
#include <cmath>
#include <gmpxx.h>
using namespace std;

mpz_class power (int base, int n) {
	mpz_class result = 1;
	for (; n > 0; n--) result *= base;
	return result;
}

int main() {
	int T, N, J;
	mpz_class divisor [9];
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> N;
		cin >> J;
		mpz_class jam = power(2,N-1) + 1;

		cout << "Case #" << t << ":\n";
		for (int j = 0; j < J;) {
			mpz_class jamdigit [N];
			mpz_class tempjam = jam;
			for (int i = N-1; i >= 0; i--) {
				jamdigit[i] = tempjam/power(2,i);
				tempjam = tempjam%power(2,i);
			}

			int base = 2;
			while ( base  <= 10 ) {
				mpz_class n = 0;
				for (int i = 0; i < N; i++) n += jamdigit[i]*power(base,i);
				mpz_class d = 3;
				mpz_class dmax;
				dmax = 42; //Give up if it looks like divisors are too large
				for (; d <= dmax; d++) {
					if (n%d == 0) {
						divisor[base-2] = d;
						break;
					}
				}

				if (d <= dmax) base++;
				else break;
			}

			if (base == 11) {
				for (int i = N-1; i >= 0; i--) cout << jamdigit[i];
				for (int i = 0; i < 9; i++) cout << ' ' << divisor [i];
				cout << '\n';
				j++;
			}

			jam += 2;
		}
	}
}
