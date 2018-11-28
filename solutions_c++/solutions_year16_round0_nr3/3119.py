#include <bits/stdc++.h>
#define D(x) cout << #x << " = " << (x) << endl

using namespace std;

bool prime(long long a) {
	for (long long i = 2; i * i <= a; ++i) {
		if ((a % i) == 0)
			return false;
	}
	return true;
}

long long parse(long long cur, int base, int n) {
	long long ans = 0;
	for (int i = n; i >= 0; --i) {
		ans *= base;
		if ((cur >> i) & 1) {
			ans += 1;
		}
	}	
	return ans;
}

bool check(long long cur, int base, int n) {
	return !prime(parse(cur, base, n));
}

void printbinary(long long a, int n) {
	for (int i = n; i >= 0; --i) {
		if ((a >> i) & 1) cout << 1;
		else cout << 0;
	}	
}

void printfirstdivisor(long long a) {
	for (long long i = 2; i < a; ++i) {
		if ((a % i) == 0) {
			cout << i;
			return;
		}
	}
	assert(0);
}

void solve() {
	int n, j;
	cin >> n >> j;
	n--;
	int base = 1 << n;
	vector<long long> a;
	a.reserve(n + 10);
	for (long long i = 1; i < base; ++i) {
		if (i & 1) {
			long long cur = base | i;
			int ok = 1;
			for (int j = 2; j < 11; ++j) {
				ok &= check(cur, j, n);
			}
			if (ok)
				a.push_back(cur);
		}
		if (a.size() == j) break;
	}

	for (int i = 0; i < j; ++i) {
		printbinary(a[i], n);
		for (int k = 2; k < 11; ++k) {
			cout << " ";
			printfirstdivisor(parse(a[i], k, n));
		}
		cout << endl;	
	}
}

int main() {
	int tc;
	cin >> tc;
	int c = 1;
	while (tc--) {
		cout << "Case #" << (c++) << ":" << endl;
		solve();
	}
	return 0;
}
