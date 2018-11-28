#include <algorithm>
#include <assert.h>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

uint64_t gcd(uint64_t a, uint64_t b) {
	if (a < b)
		a ^= b ^= a ^= b;
	while (b != 0) {
		a = a % b;
		if (a == 0)
			return b;
		b = b % a;
	}
	return a;
}

uint64_t ilog2(uint64_t n) {
	uint64_t r = 0;
	while (n & -2) {
		n >>= 1;
		r++;
	}
	return r;
}

int main() {
	int64_t tt;
	cin >> tt;
	for (int64_t ti=1; ti<=tt; ti++) {
		char s[30];
		cin >> s;
		int i=0;
		while (s[i] != '/') i++;
		s[i] = 0;
		int n = atoi(s);
		int d = atoi(s+(i+1));
		int v = gcd(n, d);
		n /= v;
		d /= v;
		cout << "Case #" << ti << ": ";
		if (d & (d-1)) {
			cout << "impossible";
		} else {
			cout << (ilog2(d) - ilog2(n));
		}
		cout << endl;
	}
}
