#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

int n;

double V, X;

pair<double, double> p[110];

const double eps = 1e-9;

bool check(double m) {
	double v = V, sum = 0;
	for (int i = 0; i < n; i++) {
		double v0 = min(v, p[i].second * m);
		v -= v0;
		sum += v0 * p[i].first;
	}
	//printf("--- %lf %lf\n", sum, V * X);
	if (sum > V * X || v > eps) return 0;
	v = V;
	sum = 0;
	for (int i = n - 1; i >= 0; i--) {
		double v0 = min(v, p[i].second * m);
		v -= v0;
		//printf("sum = %lf\n", sum);
		sum += v0 * p[i].first;
	}
	//printf("sum %lf %lf %lf\n", m, sum, v);
	return sum >= V * X && v < eps;
}

int main() {
	int cas;
	scanf("%d", &cas);
	for (int re = 1; re <= cas; re++) {

		scanf("%d", &n);
		scanf("%lf%lf", &V, &X);
		for (int i = 0; i < n; i++) {
			scanf("%lf%lf", &p[i].second, &p[i].first);
		}
		sort(p, p + n);
		for (int i = 0; i < n; i++) {
			//printf("%lf %lf\n", p[i].first, p[i].second);
		}
		if (p[0].first > X || p[n - 1].first < X) {
			printf("Case #%d: IMPOSSIBLE\n", re);
			continue;
		}
		if (n == 1) {
			printf("Case #%d: %.10lf\n", re, V / p[0].second);
			continue;
		}
		double l = 0, r;
		if (p[0].first < p[n-1].first) {
			double V0 = (V*X - V*p[n-1].first) / (p[0].first - p[n-1].first);
			double V1 = V - V0;
			r = max(V0 / p[0].second, V1 / p[n-1].second);
		} else {
			r = V / (p[0].second + p[n-1].second);
		}
		printf("Case #%d: %.10lf\n", re, r);
		//printf("r = %lf\n", r);
		/*
		while (l + eps < r) {
			double m = (l + r) / 2;
			if (check(m)) {
				r = m;
			} else {
				l = m;
			}
		}*/
		//printf("Case #%d: %.10lf\n", re, l);
	}
}