/*
 * 1000.cpp
 *
 *  Created on: 2013-12-14
 *      Author: lenovo
 */
#include<iostream>
#include<cstdio>
using namespace std;
int main() {
	int T, Case = 0;
	scanf("%d", &T);
	double C, F, X, ans, t;
	bool ok;
	int i, n;
	while (T--) {
		Case++;
		scanf("%lf %lf %lf", &C, &F, &X);
		ok = 0;
		n = 1;
		ans = X / 2.0;
		while (!ok) {
			t = X / (2.0 + F * (double) n);
			for (i = 0; i < n; i++)
				t += (C / (2.0 + F * (double) i));
			if (t >= ans)
				ok = 1;
			else
				ans = t;
			n++;
		}
		printf("Case #%d: %.7lf\n", Case, ans);
	}
	return 0;
}
