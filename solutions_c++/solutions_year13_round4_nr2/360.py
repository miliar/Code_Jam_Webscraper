#include <iostream>
#include <algorithm>

using namespace std;

long long solve(long long n, long long p) {
	if (p == (1LL << n)) {
		return (1LL << n) - 1;
	}
	p--;
	for (int i = n - 1; i >= 0; i--) {
		if (!(p & (1LL << (long long)i))) {
			long long d = n - i;
			return (1LL << d) - 2LL;
		}
	}
}

int main() {
	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		cout << "Case #" << t << ": ";
		long long n, p;
		cin >> n >> p;
		if (p == (1LL << n)) {
			cout << (1LL << n) - 1LL << ' ' << (1LL << n) - 1LL << endl;
			continue;
		}
		cout << solve(n, p) << ' ' << (1LL << n) - 2LL - solve(n, (1LL << n) - p) << endl;
	}
}