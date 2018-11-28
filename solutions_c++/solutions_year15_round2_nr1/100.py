#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

long long rev(long long x) {
	long long ret = 0ll;

	while (x > 0ll) {
		ret *= 10ll; ret += x % 10ll; x /= 10ll;
	}

	return ret;
}

long long f(long long x) {
	int len = 0; long long tmp = x;
	while (tmp >= 10ll) { tmp /= 10ll; len++; }

	long long to = 1ll;
	for (int i = 0; i < len; ++i) to *= 10ll;

	long long p = 1ll, ret = x - to;
	for (int i = 0; i < len; ++i) {
		p *= 10ll;
		long long l = x / p, r = x % p, t;
		if (r == 0 && l * p != to) {
			l--; r = p - 1ll;
			t = r + rev(l) + 1;
			if (t < ret) ret = t;
		}
		else {
			t = r + rev(l);
			if (t < ret) ret = t;
		}
	}
//cout << x << ", " << ret << "|";
	if (len == 0) return ret;
	return ret + f(to - 1ll) + 1ll;
}

void work(long long n) {
	cout << f(n) + 1ll << endl;
}

int main() {
	int T; cin >> T;

	for (int t = 1; t <= T; ++t) {
		long long n; cin >> n;
		cout << "Case #" << t << ": ";
		work(n);
	}

	/*for (int t = 1; t <= 1000000; ++t) {
		cout << "Case #" << t << ": ";
		work(t);
	}*/

	return 0;
}
