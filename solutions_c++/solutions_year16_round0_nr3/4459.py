#include <iostream>
#include <vector>
#include <math.h>
#include <bitset>
#include <algorithm>
#include <string>
#include <cstdint>
#include <stdint.h>

using namespace std;

#define ul int64_t

constexpr int64_t ipow(int64_t base, int exp, int64_t result = 1) {
  return exp < 1 ? result : ipow(base*base, exp/2, (exp % 2) ? result*base : result);
}

string getBits(ul n, ul l) {
	string out;
	for(ul i = 0;i < l;i++) {
		out += to_string(n & 0x1);
		n  >>= 1;
	}
	reverse(out.begin(), out.end());
	return out;
}

ul getBase(ul n, ul b, ul l) {
	ul out = 0;
	for(ul i = 0;i < l;i++) {
		if(n & (1 << i)) {
			out += ipow(b, i);
		}
	}
	return out;
}

ul getDivisor(ul n) {
	for(ul i = 2;i < sqrt(n) + 1;i++) {
		if((n % i) == 0) {
			return i;
		}
	}
	return 0;
}

void solve(ul n, ul j) {
	int count = 0;
	ul i = (1 << (n - 1)) | 0x1;
	for(;i < (1 << n) && j > 0;i += 0x2) {
		vector<ul> divs;
		for(ul l = 2;l < 11;l++) {
			ul k = getBase(i, l, n);
			ul d = getDivisor(k);
			if(d) {
				divs.emplace_back(d);
			} else {
				break;
			}
		}
		if(divs.size() == 9) {
			cout << getBits(i, n);
			for(ul k : divs) {
				cout << " " << k;
			}
			cout << endl;
			j--;
			count += 1;
		}
	}
}

int main()
{
	int t, n, j;
	cin >> t;
	for(int i = 1;i <= t;i++) {
		cin >> n >> j;
		cout << "Case #" << i << ":" << endl;
		solve(n, j);
	}
	return 0;
}
