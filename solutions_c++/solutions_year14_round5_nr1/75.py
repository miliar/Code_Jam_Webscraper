#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <algorithm>
#include <cstdint>
#include <cmath>
#include <iostream>
using namespace std;
const int maxn = 1000001;
uint64_t a[maxn];
uint64_t sum;
int n, p, q, r, s;

void init() {
	scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
	sum = 0;
	for (int i = 0; i < n; i++) {
		a[i] = (uint64_t)i * (uint64_t)p;
		a[i] += (uint64_t)q;
		a[i] %= (uint64_t)r;
		a[i] += (uint64_t)s;
		sum += a[i];
	}
	return;
}

bool valid(uint64_t k) {
	int cur = 0;
	for (int i = 0; i < 3; i++) {
		uint64_t tsum = 0;
		while (true) {
			if (cur >= n) {
				break;
			}
			if ((tsum + a[cur]) > k) {
				break;
			}
			tsum += a[cur];
			cur++;
		}
		if (cur >= n) {
			return true;
		}
	}
	return false;
} 

double calc() {
	uint64_t l = 0LL;
	uint64_t r = 1152921504606846976LL;
	while (true) {
		if (l >= r - 1) {
			break;
		}
		uint64_t m = (l + r) >> 1;
		if (valid(m)) {
			r = m;
		} else {
			l = m;
		}
	}
	return ((double)(sum - r)) / ((double)sum);
}

int main() {
	int tcase;
	scanf("%d", &tcase);
	for (int i = 1; i <= tcase; i++) {
		init();
		printf("Case #%d: %.10lf\n", i, calc());
	}
	return 0;
}