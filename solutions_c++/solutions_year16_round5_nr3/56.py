/**
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

typedef long long ll;

ll sqr( ll x ) {
	return x * x;
}

void solve() {
	int n, s;
	scanf("%d%d", &n, &s);
	int x[n], y[n], z[n];
	int vx[n], vy[n], vz[n];
	forn(i, n) {
		scanf("%d%d%d", &x[i], &y[i], &z[i]);
		scanf("%d%d%d", &vx[i], &vy[i], &vz[i]);
	}
	vector<ll> d(n, 1e18);
	vector<int> u(n, 0);
	d[0] = 0;
	forn(i, n) {
		int mi = -1;
		forn(j, n)
			if (!u[j] && (mi == -1 || d[j] < d[mi]))
				mi = j;
		u[mi] = 1;
		forn(j, n)
			d[j] = min(d[j], max(d[mi], sqr(x[j] - x[mi]) + sqr(y[j] - y[mi]) + sqr(z[j] - z[mi])));
	}
	printf("%.15f\n", sqrt(d[1]));
}

int main() {
	int n;
	scanf("%d ", &n);
	for (int i = 1; i <= n; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}
