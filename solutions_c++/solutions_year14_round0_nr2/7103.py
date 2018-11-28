#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

double solve(double c, double f, double x) {
	double answer = 1. * x / 2;
	double q = 2, time = 0;
	while (1) {
		double fuck_1 = x / q, fuck_2 = c / q;

		if (time + fuck_2 >= answer) {
			time += fuck_1;
			answer = min(answer, time);
			break;
		}
		else {
			answer = min(answer, time + fuck_1);
			time += fuck_2, q += f;
		}
	}

	return answer;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		double c, f, x;
		cin >> c >> f >> x;
		double answer = solve(c, f, x);
		printf("Case #%d: %0.8f\n", i + 1, answer);
	}

	return 0;
}