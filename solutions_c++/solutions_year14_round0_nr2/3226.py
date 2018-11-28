#include <cstdio>
#include <algorithm>
using namespace std;

double test() {
	double x,c,f;
	scanf("%lf%lf%lf", &c, &f, &x);
	double speed = 2.0;
	double res = x/speed;
	double cur = 0;
	while (speed < f * (x/c-1)) {
		cur += c/speed;
		speed += f;
		res = min(res, x/speed+cur);
	}
	return res;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++) {
		printf("Case #%d: %.7lf\n", tt, test());
	}
	return 0;
}
