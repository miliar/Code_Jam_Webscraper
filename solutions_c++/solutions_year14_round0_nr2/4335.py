/*
 * Michał Łazowik
 *
 * Google Code Jam 2014
 * Qualification Round
 * Problem B. Cookie Clicker Alpha
 *
 */

#include <cstdio>
#include <cmath>

using namespace std;

typedef long double LD;

#define REP(x, n) for (int x = 0; x < n; ++x)
#define FOR(x, b, e) for (int x = b; x <= (e); ++x)

LD solve(LD farm, LD add, LD target) {
	LD time = 0, rate = 2;

	while (farm / rate + target / (rate+add) < target / rate) {
		time += farm / rate;
		rate += add;
	}

	time += target / rate;

	return time;
}

int main() {
	int q;
	LD c, f, x;

	scanf("%d", &q);

	FOR(i, 1, q) {
		scanf("%Lf %Lf %Lf", &c, &f, &x);
		printf("Case #%d: %.7Lf\n", i, solve(c, f, x));
	}

	return 0;
}
