//LANG:C++
#include <cstdio>
#include <cstring>

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.in", "w", stdout);

	double c, f, x, rate=2, esti, time=0, fac=0;
	int t;
	scanf("%d", &t);
	for (int i=0; i<t; i++) {
		fac = 0;
		time = 0;
		rate = 2;
		scanf("%lf%lf%lf", &c, &f, &x);
		while (x/rate > (x/(rate+f))+(c/rate)) {
			time+=c/rate;
			rate+=f;
			fac++;
		}
		esti = (x/rate)+time;
		printf("Case #%d: %.7lf\n", i+1, esti);
	}
}
