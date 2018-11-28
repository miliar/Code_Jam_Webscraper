//============================================================================
// Name        : CookieClickerAlpha.cpp
// Author      : J.Son
// Version     :
// Copyright   : GNU LGPL
// Description : 2014 Google Code Jam Qualification Round Problem B
//============================================================================

#include <cstdio>

using namespace std;

int main() {
	int t;

	scanf("%d", &t);

	for (int cases = 1; cases <= t; cases++) {
		double c, f, x, time = 0;

		scanf("%lf %lf %lf", &c, &f, &x);

		double curV = 2, threshold = f * (x - c) / c;

		while (curV < threshold) {
			time += c / curV;
			curV += f;
		}

		time += x / curV;

		printf("Case #%d: %.7lf\n", cases, time);
	}

	return 0;
}
