#include <iostream>
#include <cstring>
#include <cmath>

using namespace std;

static inline long long get_first_divisor(long long n)
{
	for (long long i = 2; i <= sqrt(n); ++i) {
		if (n % i == 0) {
			return i;
		}
	}

	return -1;
}

static inline bool is_coin_jam(char *snr, int *divisors)
{
	long long n = 0;

	for (int i = 0; i < 9; ++i) {
		n = strtoll(snr, NULL, (i+2));
		//cout << n << endl;
		divisors[i] = get_first_divisor(n);
		if (divisors[i] == -1) {
			return false;
		}
	}

	return true;
}

int main(int argc, char **argv)
{
	int t = 0, divisors[9];
	int counter = 0;
	int *ns = NULL, *js = NULL;
	char *snr = NULL;

	cin >> t;
	ns = new int[t];
	js = new int[t];

	for (int i = 0; i < t; ++i) {
		cin >> ns[i] >> js[i];
	}

	for (int i = 0; i < t; ++i) {
		cout << "Case #" << (i+1) << ":" << endl;

		counter = 0;
		snr = new char[ns[i]+1];

		for (int j = 0; (j < (1 << (ns[i]-2))) && (counter < js[i]); ++j) {
			memset(snr, 0, ns[i]+1);
			snr[0] = '1';
			snr[ns[i]-1] = '1';
			for (int k = 0; k < (ns[i]-2); ++k) {
				if (j & (1 << k)) {
					snr[(ns[i]-1)-k-1] = '1';
				}
				else {
					snr[(ns[i]-1)-k-1] = '0';
				}
			}

			if (is_coin_jam(snr, divisors)) {
				++counter;
				cout << snr;
				for (int k = 0; k < 9; ++k) {
					cout << " " << divisors[k];
				}
				cout << endl;
			}
		}
		delete snr;
	}

	delete ns;
	delete js;

	return 0;
}
