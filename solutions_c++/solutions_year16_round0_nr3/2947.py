#include <algorithm>
#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>
#define ll long long
#define f first
#define s second
#define mp make_pair
#define pb push_back

using namespace std;

ll T, n, j, id;
ll a[16], b[10], d[10];
ll ans[51][16], ansd[51][10];

bool isPrime(ll x) {
	for (ll p = 2; p * p <= x; ++p)
		if (x % p == 0)
			return false;
	return true;
}

bool check() {
	for (ll base = 2; base <= 10; ++base) {
		ll cur = 0;
		for (int i = 0; i < n; ++i)
			cur = cur * base + a[i];
		if (isPrime(cur))
			return false;					
		b[base - 2] = cur;
	}

	for (int i = 0; i < 9; ++i) {
		ll cur = b[i];
		for (ll divisor = 2; divisor * divisor <= cur; ++divisor) {
			if (cur % divisor == 0) {
				d[i] = divisor;
				break;
			}
		}
	}

	return true;
}

void print() {
	for (int i = 0; i < n; ++i) {
		cout << a[i];
	}
	cout << endl;
}

void solve() {
	id++;
	scanf("%d%d", &n, &j);
	printf("Case #%d:\n", id);
	a[0] = a[n - 1] = 1;
	int k = 0;
	bool ok = false;
	
	for (int cnt = 0; cnt <= n - 2; ++cnt) {
		int x = cnt;
		for (int i = n - 2; i >= 1; --i)
			if (x > 0) {
				a[i] = 1;
				--x;
			} else 
				a[i] = 0;
		do {
			if (check()) {
				if (k < j) {
					for (int i = 0; i < n; ++i)
						ans[k][i] = a[i];
					for (int i = 0; i < 9; ++i)
						ansd[k][i] = d[i];
					++k;
				} else {
					ok = true;
					break;
				}
			}
		} while (next_permutation(a + 1, a + n - 1));

		if (ok)
			break;
	}

	for (int k = 0; k < j; ++k) {
		for (int i = 0; i < n; ++i)
			printf("%d", ans[k][i]);
		for (int i = 0; i < 9; ++i)
			printf(" %d", ansd[k][i]);
		printf("\n");
	}
		
}

int main() {
	#ifdef LOCAL
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	#endif
	scanf("%d", &T);
	while (T--) {
		solve();
	}

	return 0;
}
                                


