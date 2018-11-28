#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef long double LD;
const int maxint = 0x7f7f7f7f, mod = 1000000007;
const double eps = 1e-8, pi = acos(-1.0);

void rd() { }
template<typename... T> void rd(int &h, T &... t) { scanf("%d", &h); rd(t...); }
template<typename... T> void rd(long long &h, T &... t) { scanf("%lld", &h); rd(t...); }
template<typename... T> void rd(double &h, T &... t) { scanf("%lf", &h); rd(t...); }

const int maxn = 1000001;
int n, p, q, r, s, tests;
LL a[maxn], sum[maxn];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	rd(tests);
	for (int tt = 1; tt <= tests; ++tt) {
		rd(n, p, q, r, s);
		for (int i = 1; i <= n; ++i) {
			LL y = (LL) (i - 1) * p + q;
			y %= r;
			y += s;
			a[i] = y;
			sum[i] = sum[i - 1] + a[i];
		}
		int cur = 1;
		LL ret = ~0ull >> 1;
		for (int i = 1; i <= n; ++i) {
			if (cur < i) cur = i;
			while (cur + 1 <= n) {
				LL s1 = sum[cur] - sum[i - 1];
				LL s2 = sum[n] - sum[cur];
				if (s1 < s2) ++cur;
				else break;
			}
			LL val = max(sum[cur] - sum[i - 1], sum[n] - sum[cur]), val2 = ~0ull >> 1;
			if (cur != i) {
				cur -= 1;
				val2 = max(sum[cur] - sum[i - 1], sum[n] - sum[cur]);
				cur += 1;
			}
			LL tmp = min(val, val2);
			tmp = max(tmp, sum[i - 1]);
			ret = min(ret, tmp);
		}
		printf("Case #%d: %.15f\n", tt, 1 - (LD) ret / sum[n]);
	}
	return 0;
}

