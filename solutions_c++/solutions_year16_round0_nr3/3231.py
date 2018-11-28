#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

typedef long long Number;

Number toBase(Number n, int base) {
	Number ret = 0;
	Number power = 1;
	while (n > 0) {
		ret += (n & 1) * power;
		power *= base;
		n >>= 1;
	}
	ret += power;
	ret *= base; ret += 1;
	return ret;
}

void solve(int N, int J) {
	string jamcoin(N, '0');

	// ignore both 1's at the ends
	for (int i = (1 << (N - 2)) - 1; i >= 0 && J > 0; --i) {
		bool nonPrimeInAllBases = true;
		vector <Number> divisors;
		divisors.push_back(toBase(i, 10));

		for (int base = 2; base <= 10; ++base) {
			Number inCurrentBase = toBase(i, base);
			bool primeInCurrentBase = true;
			// printf("- %d in base %d is %d\n", i, base, inCurrentBase);
			for (Number divisor = 2; divisor * divisor <= inCurrentBase; ++divisor) {
				if (inCurrentBase % divisor == 0) {
					divisors.push_back(divisor);
					primeInCurrentBase = false;
					break;
				}
			}

			if (primeInCurrentBase) {
				nonPrimeInAllBases = false;
				break;
			}
		}

		if (nonPrimeInAllBases) {
			for (int i=0; i < divisors.size(); ++i) {
				if (i > 0) cout << " ";
				cout << divisors[i];
			} cout << endl;
			--J;
		}
	}

	assert(J == 0);
}

void solveSingleCase() {
	int N, J;
	cin >> N >> J;
	cout << endl;
	solve(N, J);
}

int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ":";
		solveSingleCase();
	}
	
	return 0;
}
