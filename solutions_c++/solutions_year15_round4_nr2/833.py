//============================================================================
// Name        : gcj_b.cpp
// Author      : huangxs139
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

const double eps = 1e-6;

bool eq(double a, double b) {
	if (a < b+eps && a > b-eps)
		return 1;
	return 0;
}

int main() {
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("B-small-attempt2.out", "w", stdout);

	int t;
	int n;
	double x, v;
	double r[110], c[110];
	double t1, t2;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		printf("Case #%d: ", cas);
		scanf("%d", &n);
		scanf("%lf%lf", &v, &x);
		for (int i = 1; i <= n; i++)
			scanf("%lf%lf", &r[i], &c[i]);
		if (n > 2)
			printf("NOT YET\n");
		if (n == 1) {
			if (!eq(c[1], x))
				printf("IMPOSSIBLE\n");
			else
				printf("%.9f\n", v/r[1]);
		} else if (n == 2) {
			if (eq(c[1], c[2])) {
				if (!eq(c[1], x))
					printf("IMPOSSIBLE\n");
				else
					printf("%.9f\n", v/(r[1]+r[2]));
			} else {
				t1 = v*(x-c[2])/r[1]/(c[1]-c[2]);
				t2 = v*(x-c[1])/r[2]/(c[2]-c[1]);
				if (t1 < 0 || t2 < 0)
					printf("IMPOSSIBLE\n");
				else
					printf("%.9f\n", max(t1, t2));
			}
		}
	}
	return 0;
}
