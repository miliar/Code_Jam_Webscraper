#include <cstdio>
#include <iostream>
#include <set>
#define repn(i, a, b) for(int i = a; i < b; i++)
#define rep(i, a) repn(i, 0, a)

using namespace std;

double compute(int n, double c, double f, double x) {
	double ans = 0;
	double v = 2;
	rep (i, n) {
		ans += c/v;
		v += f;
	}
	return ans + x /v;
}

void solve() {
	double c, f, x;	
	double v = 2;
	cin >> c >> f >> x;
	int i = 0;
	while (true) {
		double a = x/(i*f + v);
		double b = c/(i*f + v) + x/((i+1)*f + v);
		if (a < b) {
			printf("%.7lf\n",compute(i, c, f, x));
			break;
		}
		i++;
	}
}

int main() {
	int test = 0;
	cin >> test;
	rep (i, test) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
