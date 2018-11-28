#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

const int MaxX = 100 * 1000;

double getTime(double c, double f, double x, int farms) {
	double timePerSec = 2.0;
	double result = 0.0;
	for (int i = 0; i < farms; i++) {
		result += c / timePerSec;
		timePerSec += f;
	}
	return result + x / timePerSec;
}

double solve(double c, double f, double x) {
	double result = 1e9;	
	int l = 0, r = MaxX + 1;
	while (l < r - 2) {
		int m1 = l + (r - l) / 3;
		int m2 = l + ((r - l) * 2) / 3;
		if (getTime(c, f, x, m1) > getTime(c, f, x, m2))
			l = m1;
		else
			r = m2;
	}
	for (int i = l; i <= r; i++)
		result = min(result, getTime(c, f, x, i));
	return result;
}

int main () {
	int t;
	scanf ("%d", &t);
	for (int test = 0; test < t; test++) {
		double c, f, x;
		scanf ("%lf%lf%lf", &c, &f, &x);
		printf ("Case #%d: %.7f\n", test + 1, solve(c, f, x));
	}
}

