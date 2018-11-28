#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <iostream>
#include <cmath>

#include "int128.cpp"

using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pI;
typedef pair<string, int> pSI;
typedef pair<int, string> pIS;

#define FOR(i,n) for(int i=0, upTo##i=n; i<upTo##i; ++i)
#define REVFOR(i,n) for(int i=(n)-1; i>=0; --i)
#define FOR2(i,b,n) for(int i=b; i<(n); ++i)
#define REVFOR2(i,b,n) for(int i=(n)-1; i>=b; --i)
#define SC(i) scanf("%d", i)
#define ALL(C) (C).begin(), (C).end()
#define RALL(C) (C).rbegin(), (C).rend()
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define A first
#define B second


class Prime {
protected:
	vector<uint> primes;
	uint        high;
	void        sito(uint val);

public:
	Prime(uint upTo) : high(upTo) {
		sito(high);
	}

	int findDivisor(int128 &val) const;
};


void Prime::sito(uint val) {
	bool *table = new(nothrow) bool[val + 1];

	table[0] = false;
	table[1] = false;
	for (uint i = 2; i <= val; ++i) table[i] = true;

	primes.clear();
	for (uint i = 2; i <= val; ++i) {
		if (table[i]) {
			primes.push_back(i);

			for (uint k = i + i; k <= val; k += i) {
				table[k] = false;
			}
		}
	}
	primes.push_back(UINT_MAX);

	delete[] table;
}


int Prime::findDivisor(int128 &val) const {
	while (val.low % 2 == 0) {
		return 2;
	}

	uint upTo = static_cast<uint>(sqrt(static_cast<double>(val)) + 1e-7);
	if (upTo > 65536) upTo = 65536;
	uint primeIdx = 1;
	while (primes[primeIdx] <= upTo) {
		int128 r;
		div1(val, s64(primes[primeIdx]), &r);
		if (r == 0) {
			return primes[primeIdx];
		}
		else {
			++primeIdx;
		}
	}

	return 0;
}

Prime prime(65536);

void printb(int128 v) {
	if (v == 1)
		cout << '1';
	else {
		printb(v / u64(2));
		cout << v.low % 2;
	}
}

bool testV(int128 v, int len) {
	bool val[32];
	int128 v2 = v;
	for (int i = 0; i < len; ++i) {
		val[i] = (v.low % 2) != 0;
		v = v / u64(2);
	}

	int divisors[11];
	FOR2(sys, 2, 11) {
		int128 sysV = 0;
		int128 mul = 1;

		FOR(i, len) {
			if (val[i]) {
				sysV = sysV + mul;
			}
			mul = mul * sys;
		}

		int div = prime.findDivisor(sysV);
		if (div == 0)
			return false;

		divisors[sys] = div;
	}

	printb(v2);
	FOR2(sys, 2, 11) {
		cout << " " << divisors[sys];
	}

	cout << endl;
	return true;
}

void test(int n, int j) {
	int128 val = (s64(1) << (n - 1)) + 1;

	while (j != 0) {
		if (testV(val, n)) {
			--j;
		}
		val = val + u64(2);
	}
}

void start() {
	int t; cin >> t;
	FOR(_i, t) {
		int n, j;
		cin >> n >> j;

		printf("Case #%d:\n", _i + 1);
		test(n, j);
	}
}

int main(void) {
	start();

	return 0;
}
