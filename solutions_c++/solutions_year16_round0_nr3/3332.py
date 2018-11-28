#include <bits/stdc++.h>

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

using namespace std;

typedef long long ll;

const int maxn = 201000;

void solve() {
	int n = 16, k = 50, good[11];
	for (int msk = (1 << (n - 1)) + 1; msk < (1 << n) && k; msk += 2) {
		fill(good, good + 11, -1);
		for (int d = 2; d <= 10; ++d) {
			for (int p = 2; p <= 100; ++p) {
				int cur = 0;
				for (int i = 0; i < n; ++i) {
					cur = cur * d % p;
					if ((msk >> (n - i - 1)) & 1) cur = (cur + 1) % p;
				}
				if (cur == 0 && good[d] == -1) good[d] = p;
			}
		}
		bool ok = true;
		for (int d = 2; d <= 10; ++d) {
			ok &= good[d] != -1;
		}
		if (ok) {
			--k;
			string s;
			for (int x = msk; x; x >>= 1) {
				s += '0' + (x & 1);
			}
			reverse(s.begin(), s.end());
			cout << s;
			for (int d = 2; d <= 10; ++d) {
				cout << " " << good[d];
			}
			cout << "\n";
		}
	}
}

int main() {
	int t = 1;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ":\n";
		solve();
	}
}
