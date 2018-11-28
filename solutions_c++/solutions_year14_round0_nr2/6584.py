#include <cstdio>
#include <algorithm>
using namespace std;

double C, F, X;

double f(int n) {
	double money = 0;
	double v = 2;
	double time = 0;
	for (int i = 0; i < n; i ++) {
		time += C / v;
		v += F;
	}
	double ret = time + X / v;
//	printf("f(%d) = %lf\n", n, ret);
	return ret;
}

double bsearch(int l, int r) {
	if (l == r) return f(l);
	if (l + 1 == r) {
		double fl = f(l), fr = f(r);
		return min(fl, fr);
	}
	int m = (l + r) / 2;
	if (f(m) < f(m + 1)) {
		return bsearch(l, m);
	} else {
		return bsearch(m + 1, r);
	}
}

int main() {
	int tn, ti;
	scanf("%d", &tn);
	for (int ti = 0; ti < tn; ti ++) {
		scanf("%lf%lf%lf", &C, &F, &X);
		printf("Case #%d: %.7lf\n", ti+1, bsearch(0, 1000000));
	}
}
