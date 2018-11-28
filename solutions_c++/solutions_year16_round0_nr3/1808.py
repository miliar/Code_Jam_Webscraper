#include <iostream>
#include <vector>
#include <cmath>
#include <bitset>
#include <cstdlib>
#include "BigIntegerLibrary.hh"
#include <string>

// Using the Big Integer Library from https://mattmccutchen.net/bigint/

using namespace std;

vector<long> primes;
vector<bool> isPrime;

long long lowestDenominator(BigInteger n) {
	// DOn't spend too long finding it - if it's too large, just skip
	// this number and move to the next one
	for (long long i = 0; i < 1000; ++i) {
		if (n % primes[i] == 0) {
			return primes[i];
		}
	}
	return 0;
}

bool isNumPrime(BigInteger n) {
	if (n < isPrime.size()) return isPrime[n.toInt()];

	return (lowestDenominator(n) == 0);
}

BigInteger bigPow(BigInteger n, int p) {
	BigInteger ret = 1;
	for (int i = 0; i < p; ++i) {
		ret *= n;
	}
	return ret;
}

BigInteger convertToBase(BigInteger n, int base) {
	BigInteger ret = 0;
	long long raiseTo = 0;
	BigInteger b = base;
	while (n > 0) {
		ret += bigPow(b * ((n%10) % base), raiseTo);
		n /= 10;
		raiseTo++;
	}

	return ret;
}

void genPrimes (long long n) {
	isPrime = vector<bool>(n, true);
	for (int i = 2; i <= sqrt(n); ++i) {
		if (isPrime[i]) {
			for (long long j = i*i; j <= n; j += i) {
				isPrime[j] = false;
			}
		}
	}

	for (long long i = 2; i < isPrime.size(); ++i) {
		if (isPrime[i]) {
			primes.push_back(i);
		}
	}

	return;
}

BigInteger convertToBinary(BigInteger n) {
	string b = "";

	int digit = 32;
	while (digit >= 0) {
		if (n / bigPow(2, digit) == 1) {
			b += "1";
			n -= bigPow(2, digit);
		} else {
			b += "0";
		}
		digit--;
	}

	return stringToBigInteger(b);
}

bool isValidJam(BigInteger n) {
	if (isNumPrime(n)) return false;
	
	n = convertToBinary(n);

	for (long long base = 2; base <= 10; ++base) {
		BigInteger toBase = convertToBase(n, base);
		if (isNumPrime(toBase)) {
			return false;
		}
	}
	
	return true;
}

int main() {
	genPrimes(100000000);

	int numCases;
	cin >> numCases;
	for (int caseNum = 1; caseNum <= numCases; ++caseNum) {
		cout << "Case #" << caseNum << ":" << endl;
		int jamlength, jamnum;
		cin >> jamlength >> jamnum;
		int jamsfound = 0;
		
		BigInteger jam = bigPow(2, jamlength - 1) + 1;
		vector<BigInteger> jams;
		while (jamsfound < jamnum && jam < bigPow(2, jamlength)) {
			if (isValidJam(jam)) {
				jams.push_back(convertToBinary(jam));
				jamsfound++;
			}
			jam += 2;
		}

		for (int j = 0; j < jams.size(); ++j) {
			cout << jams[j] << " ";
			for (int p = 2; p <= 9; ++p) {
				cout << lowestDenominator(convertToBase(jams[j], p)) << " ";
			}
			cout << lowestDenominator(convertToBase(jams[j], 10)) << endl;
		}		
	}

	return 0;
}
