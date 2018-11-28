#include <cstdio>
#include <algorithm>
using namespace std;

#define INF (1e18)
#define EPS (1e-12)

int T, N;
long double V, X, VX;
struct node {
	long double R, C, RC;
	bool operator < (const node &t) const {
		return C + EPS < t.C;
	}
}RC[1005];
long double sum, m, mi, mid, ma;

long double low(long double mid) {
	long double ret = 0;
	long double VV = V;
	for (int i = 0; i < N && VV >= EPS; ++i) {
		long double a = min(VV / RC[i].R, mid);
		VV -= a * RC[i].R;
		ret += a * RC[i].RC;
	}
	if (VV > EPS) return INF;
	return ret;
}

long double high(long double mid) {
	long double ret = 0;
	long double VV = V;
	for (int i = N - 1; i >= 0 && VV >= EPS; --i) {
		long double a = min(VV / RC[i].R, mid);
		VV -= a * RC[i].R;
		ret += a * RC[i].RC;
	}
	if (VV > EPS) return -INF;
	return ret;
}

bool check(long double mid) {
	return low(mid) <= 0 && 0 <= high(mid);
	//printf("%lf %lf %lf\n", low(mid), VX, high(mid));
	return low(mid) - EPS <= VX && VX <= high(mid) + EPS;
}

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d%lf%lf", &N, &V, &X);
		VX = V * X;
		sum = 0;
		m = 1e8;
		mi = 1e8;
		ma = -1e8;
		for (int i = 0; i < N; ++i) {
			scanf("%lf%lf", &RC[i].R, &RC[i].C);
			RC[i].C -= X;
			RC[i].RC = RC[i].R * RC[i].C;
			sum += RC[i].R;
			m = min(m, RC[i].R);
			mi = min(mi, RC[i].C);
			ma = max(ma, RC[i].C);
		}
		if (0 - EPS > ma || 0 + EPS < mi) {
		//if (X - EPS > ma || X + EPS < mi) {
			printf("Case #%d: IMPOSSIBLE\n", tc);
			continue;
		}
		sort(RC, RC + N);
		//mi = V / sum;
		//ma = V / m;
		mi = 0;
		ma = 1e10;
		for (int i = 0; i < 1000; ++i) {
			mid = (mi + ma) / 2.0;
			if (check(mid)) {
				ma = mid;
			}
			else mi = mid;
			if (abs(ma - mi) < EPS) break;
		}
		printf("Case #%d: %.9lf\n", tc, mi);
	}
	return 0;
}