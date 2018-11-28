#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;

const double EPS = 1e-7;

int cmp(double a, double b) {
	if (fabs(a - b) < EPS) return 0;
	return a < b ? -1 : 1;
}

double v[9], x[9];

int main() {
	int testCaseNum;
	scanf("%d", &testCaseNum);
	for (int testCase = 1; testCase <= testCaseNum; ++testCase) {
		int N;
		double V, X;
		scanf("%d%lf%lf", &N, &V, &X);
		for (int i = 1; i <= N; ++i) {
			scanf("%lf%lf", &v[i], &x[i]);
		}
		
		printf("Case #%d: ", testCase);
		if (N == 1) {
			if (cmp(X, x[1]) != 0) {
				printf("IMPOSSIBLE\n");
			} else {
				printf("%.10lf\n", V / v[1]);
			}
			continue;
		}
		
		if (cmp(X, x[1]) * cmp(X, x[2]) == 1) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		double t;
		if (cmp(x[1], x[2]) == 0) {
			t = v[1] / (v[1] + v[2]);
		} else {
			t = (X - x[2]) / (x[1] - x[2]);
		}
		printf("%.10lf\n", max(V * t / v[1], V * (1 - t) / v[2]));
	}
	return 0;
}