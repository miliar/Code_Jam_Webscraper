#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

long long bet[40];
long long have;
int n;

double calc(long long m, int l) {
	double ans = 0;
	for (int i = 0; i <= l; ++i) {
		ans += 36 * (m - bet[i]);
	}
	return ans / (l + 1.0);
}

void solve() {
	scanf("%lld%d", &have, &n);
	//cerr << have << endl;
	for (int i = 0; i < n; ++i) {
		scanf("%lld", &bet[i]);
		//cerr << bet[i] << endl;
	}
	for (int i = n; i <= 36; ++i) {
		bet[i] = 0;
	}
	sort(bet, bet + 37);

	double ans = 0;
	for (int i = max(36 - n, 0); i <= 36; ++i) {
		long long left = 0;
		for (int j = 0; j <= i; ++j) {
			left += bet[j];
		}
		long long least = bet[i];
		if (least * (i + 1) - left > have) {
			continue;
		}
		long long lo = least, hi = (have + left) / (i + 1);
		/*
		if (i < 36) {
			hi = min(hi, bet[i + 1] - 1);
		}
		while (lo + 3 <= hi) {
			long long m1 = (lo + lo + hi) / 3;
			int c1 = 0; 
			long long psum1 = 0;
			for (int k = i + 1; k <= 36; ++k) {
				if (bet[k] <= m1) {
					c1++;
					psum1 += bet[k];
				}
			}
			double x1 = calc(m1, i) - m1 * (i + 1) + left - ((m1 + 1) * c1 - psum1);
			if (m1 * (i + 1) - left + (m1 + 1) * c1 - psum1 > have) {
				x1 = -100;
			}

			long long m2 = (hi + hi + lo) / 3;
			int c2 = 0; 
			long long psum2 = 0;
			for (int k = i + 1; k <= 36; ++k) {
				if (bet[k] <= m2) {
					c2++;
					psum2 += bet[k];
				}
			}
			double x2 = calc(m2, i) - m2 * (i + 1) + left - ((m2 + 1) * c2 - psum2);
			if (m2 * (i + 1) - left + (m2 + 1) * c2 - psum2 > have) {
				x2 = -100;
			}

			if (x1 < 0) {
				lo = m1;
			}
			if (x2 < 0) {
				hi = m2;
			}	
			if (x1 < 0 || x2 < 0) {
				continue;
			}

			if (x1 > x2) {
				hi = m2;
			} else {
				lo = m1;
			}
		}
		*/
		//cerr << "=============" << endl;
		while (lo <= hi) {
			//cerr << "!" << k << " " << calc(k, i) - k * (i + 1) + left << endl;
			long long k = (lo + hi) / 2;
			int c = 0;
			long long psum = 0;
			for (int it = i + 1; it <= 36; ++it) {
				if (bet[it] <= k) {
					c++;
					psum += bet[it];
				}
			}
			long long cost = k * (i + 1) - left + (k + 1) * c - psum;
			if (cost <= have) {
				ans = max(ans, calc(k, i) - cost);
				lo = k + 1;
				//cerr << calc(k, i) - cost << endl;
			} else {
				hi = k - 1;
				//cerr << "invalid" << endl;
			}
		}
		//cerr << i << " " << ans << endl;
	}	

	printf("%.10f\n", ans); 
}

int main() {
	freopen("A-large.in", "r", stdin);
	//freopen("A-small-attempt3.in", "r", stdin);
	//freopen("A-small-attempt2.in", "r", stdin);
	//freopen("A-small-attempt1.in", "r", stdin);
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A.in", "r", stdin);
	//freopen("A.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int _ = 1; _ <= T; ++_) {
		printf("Case #%d: ", _);
		solve();
		fflush(stdout);
	}
}
