#include <iostream>


using namespace std;

long long modpow(long long x, long long n, int mod) {
    long long P = 1;
             
    while(n) {
        if(n & 1) P = P * x % mod;
         
        n >>= 1;
        x = x * x % mod;
    }
     
    return P;
}

int primes[5] = {2, 3, 5, 7, 11};

int main() {
	int T;
	cin >> T;
	for(int caso=1; caso<=T; caso++) {
		int N, J;
		cin >> N >> J;

		cout << "Case #" << caso << ":" << endl;
		
		int sz = min(14, N-2), cnt = 0;
		for(int mask = 0; mask < (1<<sz) && cnt < J; mask++) {
			bool valid = 1;
			int divisors[11];
			for(int base=2; base<=10; base++) {
				int divisor = -1;
				for(int i=0; i<5; i++) {
					long long r = 1 + modpow(base, N-1, primes[i]);

					for(int j=0; j<sz; j++)
						if(mask & (1<<j))
							r = (r + modpow(base, j + 1, primes[i])) % primes[i];

					if(r == 0) {
						divisor = primes[i];
						break;
					}
				}
				if(divisor == -1) valid = 0;
				else divisors[base] = divisor;
			}
			if(valid) {
				cout << "1" << string(N - 2 - sz, '0');
				for(int i=sz-1; i>=0; i--)
					cout << ((mask & (1<<i)) ? "1" : "0");
				cout << "1";

				for(int base=2; base<=10; base++)
					cout << " " << divisors[base];
				cout << endl;
				cnt++;
			}
		}
	}
	return 0;
}