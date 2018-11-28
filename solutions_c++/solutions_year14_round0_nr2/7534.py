#include <stdio.h>
#include <string.h>
#define ull unsigned long long
#define loop(i, j, n)  for(int (i) = (j); i < n; i++)
#define sd(x) scanf("%d", &x)
#define slld(x) scanf("%lld", &x)

using namespace std;

int main() {
	int t;
	sd(t);
	for(int k=1; k<=t; k++) {
		double c, f, x, maxvalue, rate = 2.0, ct, ot;
		scanf("%lf%lf%lf", &c, &f, &x);
		ot = x/rate;
		while(1) {
			ct = ot - x/rate + c/rate;
			rate += f;
			ct += x/rate;
			if(ct > ot) break;
			ot = ct;
		}
		printf("Case #%d: %.7lf\n", k, ot);
	}
	return 0;
}
