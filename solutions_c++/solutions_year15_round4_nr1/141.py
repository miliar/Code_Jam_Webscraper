#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <random>
using namespace std;

#define FOR(i,a,b) for(int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)
#define PB push_back

const double inf = 1e30;
const double eps = 1e-10;
double rate[110], t[110], V, goal;

int sgn(double x) {
	if (x < -eps) return -1;
	return (x > eps);
}

double solve(int a, int b, int c) {
	if (a > b) {
		if (t[c] == goal) return 1/rate[c];
		return inf;
	}
	double totR = 0, totC = 0;
	FOR(i, a, b) {
		totR += rate[i];
		totC += rate[i] * t[i];
	}
	double x1 = totC / totR - goal;
	double w1 = totR;
	double x2 = t[c] - goal;
	double w2 = rate[c];
	if (sgn(x1) == 0 || sgn(x2) == 0) {
		if (sgn(x1) == 0 && sgn(x2) == 0) return 1/(w1+w2);
		return inf;
	}
	if (x1 > 0) {x1 = -x1; x2 = -x2;}
	if (x2 < 0) return inf;
	if (sgn((x1*w1 + x2*w2)) < 0) return inf;
	return 1 / (w1 - w1 * x1 / x2);
}

int main() {
	int nT;
	scanf("%d", &nT);
	FOR(cN, 1, nT) {
		int n;
		scanf("%d%lf%lf", &n, &V, &goal);
		REP(i, n) scanf("%lf%lf", &rate[i], &t[i]);
		REP(i, n)
		FOR(j, i+1, n-1) if (t[i] > t[j]) {
			swap(t[i], t[j]);
			swap(rate[i], rate[j]);
		}
		double ans = inf;
		REP(a, n)
		FOR(b, a, n-1) if (a == 0 || b == n-1) {
			double res;
			res = solve(a+1, b, a);
			ans = min(ans, res);
			res = solve(a, b-1, b);
			ans = min(ans, res);
		}
		printf("Case #%d: ", cN);
		if (ans == inf) puts("IMPOSSIBLE");
		else printf("%.9lf\n", ans*V);
	}
}
