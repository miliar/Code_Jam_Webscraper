#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

long long div[11];
long long t,n,j;

long long findDiv(long long n) {
	for (long long i = 2; i*i <= n; i++) {
		if (n % i == 0) {
			return i;
		}
	}
	return 0;
}
/*
bool isPrime(long long p) {
	long long ps = primes.size();
	for (long long j = 0; j < ps; j++) {
		if (primes[j]*primes[j] <= p) {
			if (p % primes[j] == 0) {
				return false;
			}
		} else {
			return true;
		}
	}
	return true;
}

void primeList() {
	// Generate prime list
	for (long long i = 2; i <= 4294967297; i++) {
		if (isPrime(i)) {
			cout << i << endl;
			primes.push_back(i);
		}
	}
}
*/
long long baseConvert(long long bin, long long base) {
	long long retVal = 0, digit = 1;
	for (long long i = 0; i < n; i++) {
		if (bin & (1<<i)) retVal += digit;
		digit *= base;
	}
	return retVal;
}

bool isJamCoin(long long bin) {
	long long jc,dv;
	for (long long i = 2; i <= 10; i++) {
		jc = baseConvert(bin, i);
		//cout << jc << " ";
		dv = findDiv(jc);
		if(dv) div[i] = dv;
		else return false;
	}
	return true;
}

bool printJamCoin(long long bin) {
	for (long long i = n-1; i >= 0; i--) {
		if (bin & (1<<i)) printf("%d", 1);
		else printf("%d", 0);
	}
	for (long long i = 2; i <= 10; i++) {
		printf(" %d", div[i]);
	}
	printf("\n");
}

int main() {
	long long found = 0;

	cin >> t;
	for (long long tc=1; tc<=t; tc++) {
		cin >> n >> j;
		printf("Case #%d:\n", tc);
		long long start = (1 << (n-1)) + 1;
		for (long long i = start; i <= (1 << n)-1 && found < j; i+=(1<<1)) {
			if (isJamCoin(i)) {
				found++;
				printJamCoin(i);
			}
		}
	}
}