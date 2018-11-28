#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <stdio.h>
#include <iostream>

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		double C, F, X;
		C = 0; F = 0; X = 0;
		scanf("%lf %lf %lf", &C, &F, &X);
		double currate = 2;
		double ans = 0;
		while (1) {
			double curans = ans + X / currate;
			double latrate = currate + F;
			double latans = ans + C / currate + X / latrate;
			if (latans > curans) {
				ans = curans;
				break;
			} else {
				ans = ans + C / currate;
				currate = currate + F;
			}
		}
		printf("Case #%d: %.6lf\n", i, ans);
	}
	return 0;
}
