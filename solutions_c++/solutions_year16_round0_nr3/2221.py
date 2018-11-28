#include <iostream>
#include <bitset>
#include <cmath>
#include <vector>

using namespace std;

#define pb push_back
#define vi vector<int>
#define ull unsigned long long

vi primes;

void gen_primes(int to) {
	primes.pb(2);
	for(int n = 3; n <= to; n += 2) {
		bool prime = true;
		for(int j = 2; j*j <= n; j++) {
			if(n % j == 0) {
				prime = false;
				break;
			}
		}
		if(prime) {
			primes.pb(n);
		}
	}
}

ull repr(ull num, int base) {
	ull res = 0;
	ull fac = 1;
	while(num != 0) {
		res += fac * (num & 1);
		fac *= base;
		num >>= 1;
	}
	return res;
}

ull test(ull num) {
	for(int prime : primes) {
		if(prime*prime > num) {
			break;
		}
		if(num % prime == 0) {
			return prime;
		}
	}
	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int T, N, J;
	cin >> T >> N >> J;

	gen_primes(65536);

	ull mask = (1 << (N-1)) | 1;
	ull limit = exp2(N-2);
	
	cout << "Case #1:" << endl;

	int found = 0;
	for(ull i = 0; i < limit; i++) {
		vector<ull> factors;
		ull num = mask | (i << 1);
		for(int base = 2; base <= 10; base++) { 
			ull conv = repr(num, base);
			ull div = test(conv);
			if(div != 0) {
				factors.pb(div);
			} else {
				break;
			}
		}
		if(factors.size() == 9) {
			if(N == 32) {
				cout << bitset<32>(num);
			} else {
				cout << repr(num, 10);
			}
			for(ull factor : factors) {
				cout << " " << factor;
			}
			cout << endl;
			found += 1;
		}
		if(found == J) {
			break;
		}
	}

	return 0;
}
