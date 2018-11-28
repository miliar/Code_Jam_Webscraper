#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ifstream fin("c.in");
ofstream fout("c.out");

ll getf(ll x) {
	if (x == 2 || x == 3) return -1;
	if ((x & 1) == 0) return 2;
	for (ll i = 3; i*i <= x; i += 2)
		if (x % i == 0) return i;
	return -1;
}

int main() {
	int n, j, ct = 0;
	fin >> n;
	fin >> n >> j;
	ll varl = n - 2, base = 1 + (1LL << (n-1));
	fout << "Case #1:\n";
	for (ll i = 0; i < (1<<varl); i++) {
		ll full = base + 2*i, safes[20] = {};
		bool good = true;

		for (int b = 2; good && b <= 10; b++) {
			ll res = 0;
			for (ll j = n-1; j >= 0; j--) {
				res *= b;
				if (full & (1LL<<j)) res++;
			}
			safes[b] = getf(res);
			if (safes[b] == -1) good = false;
			if (b == 10 && good) {
				fout << res;
				for (int j = 2; j <= 10; j++) fout << ' ' << safes[j];
				fout << '\n';
				if (++ct == j) return 0;
			}
		}
	}
}
