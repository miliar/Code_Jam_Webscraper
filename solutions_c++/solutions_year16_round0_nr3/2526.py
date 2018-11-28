#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <utility>
#include <bitset>
using namespace std;

vector<pair<int, vector<long long>>> jamcoin;

long long transform(int base, int bitmask) {
	long long number = 1;
	long long exp = base;
	for (int i = 0; i < 14; i++, exp *= base) {
		if (bitmask & (1 << i)) {
			number += exp;
		}
	}
	number += exp;
	return number;
}

long long getDiv(long long number) {
	long long bound = min(number, 1000LL);
	long long divisor;
	for (divisor = 2; divisor < bound; divisor++) {
		if (number % divisor == 0) {
			return divisor;
		}
	}
	return -1;
}

void checkJamCoin(int bitmask) {
	vector<long long> divisors;
	for (int base = 2; base <= 10; base++) {
		long long number = transform(base, bitmask); // to decimal

		long long divisor = getDiv(number);

		if (divisor > 0) {
			divisors.push_back(divisor);
		}
		else {
			return;
		}
	}
	jamcoin.push_back(make_pair(bitmask, divisors));
}

int main() {
	int dummy;
	cin >> dummy >> dummy >> dummy;

	for (int i = 0; i < (1 << 14); i++) {
		if (jamcoin.size() == 50) {
			//puts("ok");
			break;
		}
		checkJamCoin(i);
	}

	printf("Case #1:\n");
	for (int i = 0; i < jamcoin.size(); i++) {
		int bitmask = jamcoin[i].first;
		bitmask |= (1 << 14);
		bitmask <<= 1;
		bitmask |= 1;

		cout << bitset<16>(bitmask) << ' ';
		for (int j = 0; j < jamcoin[i].second.size(); j++) {
			printf("%lld ", jamcoin[i].second[j]);
		}
		puts("");
	}

	return 0;
}