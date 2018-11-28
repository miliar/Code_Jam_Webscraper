#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;

const int MAXN = 100 + 5;
const long double eps = 0.0000000000001l;

int n;
long double v, x;
long double b[MAXN];

inline long double getdouble() {
	double x;
	scanf("%lf", &x);
	return (long double) x;
}

struct node {
	long double x, y;
	void read() {
		x = getdouble();
		y = getdouble();
	}
	bool operator <(const node &t) const {
		return y < t.y;
	}
};

node a[MAXN];

inline bool check(long double mid) {
	long double ans = v, sum = 0, target = v * x;
	for (int i = 1; i <= n; i++)
		b[i] = 0;
	for (int i = 1; i <= n; i++) {
		long double t = a[i].x * mid;
		if (ans > 0) {
			if (t < ans) {
				b[i] = t;
				sum += t * a[i].y;
				ans -= t;
				continue;
			}
			b[i] = ans;
			t -= ans;
			ans = 0;
			sum += b[i] * a[i].y;
		}
		if (sum / v > x + eps)
			return false;
		if (fabs(sum / v - x) < eps)
			return true;
		for (int j = 1; j < i; j++) {
			long double t2 = min(b[j], t);
			if ((sum + t2 * (a[i].y - a[j].y)) / v > x - eps)
				return true;
			sum += t2 * (a[i].y - a[j].y);
			b[j] -= t2;
			b[i] += t2;
			t -= t2;
		}
	}
	return false;
}

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T, kase = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &n);
		v = getdouble();
		x = getdouble();
		for (int i = 1; i <= n; i++)
			a[i].read();
		if (n == 1) {
			if (x == a[1].y)
				printf("Case #%d: %.10lf\n", ++kase, (double) (v / a[1].x));
			else
				printf("Case #%d: IMPOSSIBLE\n", ++kase);
			continue;
		}
		sort(a + 1, a + n + 1);
		long double l = 0, r = 1e10;
		for (int i = 0; i < 1000; i++) {
			long double mid = (l + r) / 2;
			if (check(mid))
				r = mid;
			else
				l = mid;
		}
		if (l > 1e9)
			printf("Case #%d: IMPOSSIBLE\n", ++kase);
		else
			printf("Case #%d: %.10lf\n", ++kase, (double) l);
	}
	return 0;
}
