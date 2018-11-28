#include <iostream>
#include <cstdint>
#include <functional>
using namespace std;

static uint64_t n, n2;

uint64_t legjobb(uint64_t x)
{
	uint64_t t = n2 - 1 - x;
	uint64_t e = 0;
	uint64_t ret = 0;
	for (uint64_t i = 0, j = (n2>>1); i < n; i++, j>>= 1) {
		uint64_t m = 1 + e;
		if (e + m <= t) {
			e += m;
		} else {
			ret += j;
		}
	}
	return ret;
}

uint64_t legrosszabb(uint64_t x)
{
	uint64_t t = x;
	uint64_t e = 0;
	uint64_t ret = 0;
	for (uint64_t i = 0, j = (n2>>1); i < n; i++, j>>= 1) {
		uint64_t m = 1 + e;
		if (e + m <= t) {
			e += m;
			ret += j;
		} else {
//			ret += j;
		}
	}
	return ret;
}

// legnagyobb ami f
int bkeres(std::function<bool(uint64_t)> f)
{
	uint64_t l = 0, r = n2-1;
	while (l < r) {
		uint64_t x = (l+r+1)/2;
		if (f(x)) l = x;
		else r = x-1;
	}
	return l;
}

int main(void)
{
	int ti, tn;
	cin >> tn;
	for (ti = 1; ti <= tn; ti++) {
		uint64_t p;
		cin >> n >> p;
		uint64_t a, b;
		n2 = (((uint64_t)1)<<n);
//		for (uint64_t i = 0; i < n2; i++) {
//			uint64_t xx = legjobb(i);
//			cout << i << " "<< xx << endl;
//		}
		a = bkeres([&p](uint64_t x) { return legrosszabb(x) < p; });
		b = bkeres([&p](uint64_t x) { return legjobb(x) < p; });
		cout << "Case #" << ti << ": " << a << " " << b << endl;
	}
	return 0;
}
