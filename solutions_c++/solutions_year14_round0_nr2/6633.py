#include <cstdio>
#include <algorithm>
using namespace std;

double C, F, X;
const double EPS = 1e-9;
double tbl[1000000];
inline double f(int n) {
	return tbl[n] + X / (2 + n*F);
}

int main() {
	tbl[0] = 0.0;
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++) {
		scanf("%lf%lf%lf", &C, &F, &X);
		for(int i=1; i<1000000; i++) {
			tbl[i] = tbl[i-1] + C / (2 + (i-1)*F);
		}
		int l = 0, r = 1000000;
		while(l+3 < r) {
			int k1 = l + (r-l) / 3, k2 = l + (r-l) * 2 / 3;
			if(f(k1) < f(k2) - EPS) r = k2;
			else l = k1;
		}
		printf("Case #%d: %.7lf\n", t, min(f(l), min(f(l+1), f(l+2))));
	}
	return 0;
}
