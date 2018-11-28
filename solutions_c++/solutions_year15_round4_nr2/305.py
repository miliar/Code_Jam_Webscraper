#include <cstdio>
#include <utility>
#include <algorithm>

#define sign(x) ((x < -EPS) ? -1 : x > EPS)

using namespace std;

const int N = 233;
const long double EPS = 1E-14;

int n;
long double v, R;
pair<long double, long double> p[N];

bool ok(long double limit){
	long double now, mi = 0, ma = 0;
	now = v;
	for(int i = 0; i < n && now > EPS; i++){
		long double add = limit * p[i].second;
		if (sign(add - now) >= 0) add = now;
		now -= add;
		mi += add * p[i].first;
	}
	now = v;
	for(int i = n - 1; i >= 0 && now > EPS; i--){
		long double add = limit * p[i].second;
		if (sign(add - now) >= 0) add = now;
		now -= add;
		ma += add * p[i].first;
	}
	return sign(mi - R * v) <= 0 && sign(ma - R * v) >= 0;
}

int main(){
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; cas++){
		printf("Case #%d: ", cas);
		double x, y;
		scanf("%d%lf%lf", &n, &x, &y);
		v = x;
		R = y;
		for(int i = 0; i < n; i++){
			scanf("%lf%lf", &x, &y);
			p[i] = make_pair(y, x);
		}
		sort(p, p + n);
		long double l = 0, r = 10000000000.0, mid;
		while(r - l > 1E-12){
			mid = (l + r) / 2.0;
			if (ok(mid)) r = mid;
			else l = mid;
		}
		if (sign(p[0].first - R) <= 0 && sign(R - p[n - 1].first) <= 0) printf("%.12f\n", (double)r);
		else puts("IMPOSSIBLE");
	}
}
