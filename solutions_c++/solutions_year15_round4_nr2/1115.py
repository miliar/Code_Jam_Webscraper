#include <stdio.h>
#include <algorithm>
#include <iostream>
using namespace std;

struct water {
	long double r, t;
	water() {};
	bool operator < (const water &other) const {
		return other.t - t > 0;
	}
} w[110];

bool feq(long double a, long double b) {
	long double d = a > b ? a - b : b - a;
	return d < 1e-12L;
}

long double v, x;
int n;

void solve() {
	cin >> n >> v >> x;
	long double rate = 0, tot = 0;
	for (int i = 0; i < n; i ++) {
		cin >> w[i].r >> w[i].t;
		rate += w[i].r, tot += (w[i].t - x) * w[i].r;
	}
	sort(w, w + n);
	if (feq(tot, 0)) printf("%.12Lf\n", (long double)v / rate);
	else if (tot > 0.0) {
		for (int i = n - 1; i >= 0; i --) {
			long double change = (w[i].t - x) * w[i].r;
			if (tot - change > 1e-12L) {
				rate -= w[i].r;
				tot -= change;
			}
			else {
				rate -= tot / (w[i].t - x);
				tot = 0;
				break;
			}
		}
		if (rate > 1e-12L) printf("%.12Lf\n", (long double)v / rate);
		else printf("IMPOSSIBLE\n");
	}
	else {
		for (int i = 0; i < n; i ++) {
			long double change = (w[i].t - x) * w[i].r;
			if (change - tot > 1e-12L) {
				rate -= w[i].r;
				tot -= change;
			}
			else {
				rate -= tot / (w[i].t - x);
				tot = 0;
				break;
			}
		}
		if (rate > 1e-12L) printf("%.12Lf\n", (long double)v / rate);
		else printf("IMPOSSIBLE\n");
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i ++) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
