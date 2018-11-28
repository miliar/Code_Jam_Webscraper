#include <cstdio>
#include <iomanip>
#include <iostream>
using namespace std;

typedef long long ll;
typedef long double ld;

const int Maxn = 1000005;
const ll lim = 2000000000000;

int t;
int n, p, q, r, s;
int a[Maxn];

bool canGive(ll x)
{
	int i = 0;
	for (int t = 0; t < 3; t++) {
		ll sum = 0;
		while (i < n && sum + a[i] <= x) { sum += a[i]; i++; }
	}
	return i == n;
}

int main()
{
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d %d %d %d %d", &n, &p, &q, &r, &s);
		ll sum = 0ll;
		for (int i = 0; i < n; i++) {
			a[i] = (ll(i) * p + q) % r + s;
			sum += a[i];
		}
		ll l = 0, r = lim;
		ll res;
		while (l <= r) {
			ll m = l + r >> 1;
			if (canGive(m)) { res = m; r = m - 1; }
			else l = m + 1;
		}
		cout << "Case #" << tc << ": " << fixed << setprecision(14) << ld(sum - res) / sum << endl;
	}
	return 0;
}