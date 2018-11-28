#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cmath>

using namespace std;

long long n, p;

long long calc(long long n, long long p) {
	long long k = 1ll, ret = 0ll;

	while (true) {
		if (p + p <= n) return ret;
		n /= 2ll; p -= n; k += k; ret += k;
	}

	return -1ll;
}

void work() {
	cin >> n >> p;
	n = 1ll << n;

	if (n == p) {
		cout << n - 1ll << " " << n - 1ll << endl; return ;
	}

	cout << calc(n, p) << " " << n - calc(n, n - p) - 2ll << endl;
}

int main() {
	int T; cin >> T;
	for (int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": ";
		work();
	}

	return 0;
}
