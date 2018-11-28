#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const double INF = 1e12;
const int MAXN = 100000;

double get_time(double fn, double c, double f, double x){
	double ret = 0.0;
	double rate = 2.0;
	while (fn--){
		ret += c / rate;
		rate += f;
	}
	ret += x / rate;
	return ret;
}

double getmin(double a, double b, double c){
	return (a < b ? a : b) < c ? (a < b ? a : b) : c;
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, l, r, midl, midr;
	double c, f, x, suml, sumr, ret;

	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases){
		scanf("%lf %lf %lf", &c, &f, &x);
		ret = INF;

		l = 0;
		r = MAXN;
		while (l <= r){
			midl = l + (r - l) / 3;
			midr = r - (r - l) / 3;
			suml = get_time(midl, c, f, x);
			sumr = get_time(midr, c, f, x);
			if (suml < sumr){
				r = midr - 1;
			}
			else {
				l = midl + 1;
			}
			ret = getmin(ret, suml, sumr);
		}
		printf("Case #%d: %.7f\n", cases, ret);
	}
	return 0;
}