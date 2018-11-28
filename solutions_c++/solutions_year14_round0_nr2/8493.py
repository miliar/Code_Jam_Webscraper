
#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;

typedef long long i8;

int tst;

double solve() {
	double c, f, x;
	scanf("%lf%lf%lf",&c,&f,&x);
	double an=x/2;
	double p=2, t=0;
	while (t<an) {
		double re=t+x/p;
		an=min(an,re);
		t+=c/p;
		p+=f;
	}
	return an;
}

main() {
	scanf("%d", &tst);
	for (int cas=1; cas<=tst; cas++) {
		printf("Case #%d: %.7lf\n", cas, solve());
	}
}
