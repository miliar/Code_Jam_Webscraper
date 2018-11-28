#include <bits/stdc++.h>

using namespace std;

int getdig(long long n) {
	int res = 0;
	int nold = n;
	while (n > 0) {
		int k = n % 10;
		res |= 1<<k;
		n /= 10;
	}
	//printf("Found %d in %d\n", res, nold);
	return res;
}

int main() {
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		long long n;
		cin >> n;
		long long cur = n;
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", i);
		} else {
			int fl = 0;
			while (fl != 1024 - 1) {
				fl |= getdig(cur);
				if (fl == 1024 - 1) break;
				cur += n;
			}
			printf("Case #%d: %lld\n", i, cur);
		}
	}
}
