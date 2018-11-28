#include <bits/stdc++.h>
using namespace std;

long long prime(long long x) {
	for (long long i = 2; i * i <= x; ++i) {
		if (x % i == 0) {
			return i;
		}
	}
	return 0;
}

bool check(long long x, vector <long long> &good) {
	vector <long long> bin;
	while (x > 0) {
		bin.push_back(x % 2);
		x /= 2;
	}
	reverse(bin.begin(), bin.end());
	for (long long i = 2; i <= 10; ++i) {
		long long y = 0;
		for (long long j = 0; j < bin.size(); ++j) {
			y = y * i + bin[j];
		}
		long long v = prime(y);
		if (v == 0) {
			return 0;
		}
		good.push_back(v);
	}
	return 1;
}

void print_binary(long long x) {
	if (x == 0) {
		return;
	}
	print_binary(x / 2);
	cout << x % 2;
}

long long transfer(long long x, long long sys) {
	vector <long long> bin;
	while (x > 0) {
		bin.push_back(x % 2);
		x /= 2;
	}
	reverse(bin.begin(), bin.end());
	long long y = 0;
	for (auto e: bin) {
		y = y * sys + e;
	}
	return y;
}

set <long long> used;

void solve() {
	long long n, k;
	cin >> n >> k;
	cout << endl;
	for (long long len = 2; len < k; ++len) {
		for (long long a = len + 1; a <= n - len; ++a) {
			if ((n - len) % a == 0) {
				for (long long i = (1 << (len - 1)) + 1; i < (1 << len); i += 2){
					long long x = i;
					for (long long j = 0; j < (n - len) / a; ++j) {
						x = (x << a) + i;
					}
					if (used.count(x)) {
						continue;
					}
					used.insert(x);
					print_binary(x);
					for (long long j = 2; j <= 10; ++j) {
						cout << ' ' << transfer(i, j);
					}
					cout << endl;
					--k;
					if (k == 0) {
						return;
					}
				}
			}
		}
	}

}

int main() {
	long long T;
	cin >> T;
	for (long long t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		solve();
	}
}
