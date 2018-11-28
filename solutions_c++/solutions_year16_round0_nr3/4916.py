#include <iostream>
#include <fstream>
#include <unordered_map>
#include <bitset>
#include <bits/stdc++.h>

using namespace std;

#define MAX_N 14
#define MAX_PRIME 2051000

long long myPrimes[MAX_PRIME];

void SieveOfEratosthenes(long long n) {

	// Create a boolean array "prime[0..n]" and initialize
	// all entries it as true. A value in prime[i] will
	// finally be false if i is Not a prime, else true.

	int prime[n/(sizeof(int)*4)];
	memset(prime, 0, sizeof(prime));

 	for (long long p=2; p*p<=n; p++) {
		// If prime[p] is not changed, then it is a prime

		int bindex = p / (8 * sizeof(int) );
		int b = p % (8 * sizeof(int) );
		int result = prime[bindex] & (1<<b);

		if (result == 0) {
			// Update all multiples of p
			for (long long i=p*2; i<=n; i += p) {
				bindex = i / (8 * sizeof(int) );
				b = i % (8 * sizeof(int) );
				prime[bindex] |= 1<<b;
			}
		}
	}
 
	// Print all prime numbers
	long long cp = 0;
	for (long long p=2; p<=n; p++) {
		int bindex = p / (8 * sizeof(int) );
		int b = p % (8 * sizeof(int) );
		int result = prime[bindex] & (1<<b);

	   	if (result == 0) {
			myPrimes[cp++] = p;
	   	}
	}
	//cout << "total prime: " << cp << endl;
	//cout << "last primes: " << myPrimes[cp-1] << " " << myPrimes[cp] << endl;
}

bool isPrime(long long n, long long *divisor) {

	long long limit = (long long)sqrt(n);

	for (int i = 0; myPrimes[i] <= limit; i++) {
		if (n % myPrimes[i] == 0) {
			*divisor = myPrimes[i];
			return false;
		}
	}
	*divisor = 0;
	return true;
}

int main () {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	
	long long N, J;
	int caseNo, c = 1;

	scanf("%d", &caseNo);

	SieveOfEratosthenes((long long)sqrt(1111111111111111));
	long long divisors[11];

	while (c <= caseNo) {

		printf("Case #%d:\n", c);
		cin >> N;
		cin >> J;

		long long count = 0;
		long long bitSeq = 0;

		while (count < J) {
			long long divisor = 0;
	
			bitset<MAX_N> mySet(bitSeq);
			string myNumber("1" + mySet.to_string().substr(MAX_N-N+2) + "1");

			char * ptr;
			for (int base = 2; base <= 10; base++) {
				long long parsed = strtoll(myNumber.c_str(), &ptr, base);
				if (isPrime(parsed, &divisor)) {

					break;
				} else {
					divisors[base] = divisor;
				}
			}

			if (divisor != 0) {
				cout << myNumber << " ";
				for (int i = 2; i < 10; i++) {
					cout << divisors[i] << " ";
				}
				cout << divisors[10] << endl;
				
				count++;
			}
			bitSeq++;
		}
		
		c++;
	}

	return 0;
}