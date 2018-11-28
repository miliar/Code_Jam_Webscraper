#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int N = 32;
int J = 500;

char S[50];
int primes[1000000];
int n_primes;
bool is_prime[1000000];

void preprocess() {
	n_primes = 0;
	
	memset(is_prime, true, sizeof(is_prime));

	primes[n_primes++] = 2;
	is_prime[2] = true;
	for (int i = 4; i < 1000000; i += 2) {
		is_prime[i] = false;
	} 
	for (int i = 3; i < 1000000; i += 2) {
		if (is_prime[i]) {
			primes[n_primes++] = i;
			for (int j = 2*i; j < 1000000; j += i) {
				is_prime[j] = false;
			}
		}
	}
}


int findDivisor(int base) {

	for (int i = 0; i < 1000; i++) {
		int divi = 0;
		for (int j = 0; S[j]; j++) {
			divi = divi * base + S[j] - '0';
			divi %= primes[i]; 
		}
		if (divi == 0) {
			return primes[i];
		}
	}
	return 0;
}

void process() {
	while (J > 0) {
		S[0] = S[N-1] = '1';
		S[N] = 0;
		for (int i = 1; i < N - 1; i++) {
			S[i] = rand() % 2 + '0';
		}
		bool maybe_prime = false;
		int divisors[11];
		for (int base = 2; base <= 10; base++) {
			int divisor = findDivisor(base);
			if (!divisor) {
				maybe_prime = true;
				break;
			} else {
				divisors[base] = divisor;
			} 
		}
		if (!maybe_prime) {
			printf("%s", S);
			for (int base = 2; base <= 10; base++) {
				printf(" %d", divisors[base]);
			}
			printf("\n");
			J--;
		}
	}
}

int main() {
	printf("Case #%d:\n", 1);
	preprocess();
	process();
	return 0;
}