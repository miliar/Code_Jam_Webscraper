#include <stdio.h>
#include <math.h>
#include <queue>
#include <string.h>
#include <iostream>
using namespace std;
int t, n;
double a[120];
double b[120];
double A, B;
deque<pair<double, double> > N;
deque<pair<double, double> > P;
int main() {
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		N.clear();
		P.clear();
		scanf("%d%lf%lf", &n, &A, &B);
		for (int i = 0; i < n; i++) {
			scanf("%lf%lf", &a[i], &b[i]);
			b[i] -= B;
		}
		double sa = 0;
		for (int i = 0; i < n; i++) {
			if (fabs(b[i]) < 1e-9) {
				sa += a[i];
			} else if (b[i] < 0) {
				N.push_back(make_pair(-b[i], a[i]));
			} else {
				P.push_back(make_pair(b[i], a[i]));
			}
		}

		while (N.size() && P.size()) {
			double b0 = N.front().first;
			double b1 = P.front().first;
			double f = min(N.front().second / b1, P.front().second / b0) ;
			N.front().second -= f * b1;
			P.front().second -= f * b0;

			sa += f * (b0 + b1);

			if (N.front().second < 1e-9) {
				N.pop_front();
			}
			if (P.front().second < 1e-9) {
				P.pop_front();
			}
		}
		if (sa > 0) {
			printf("Case #%d: %.9f\n", tt, A / sa);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", tt);
		}
	}
	return 0;
}