#include<cstdio>
using namespace std;

int t, cn=1;
double c, f, x;

int main() {
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	for (scanf("%d", &t); cn<=t; cn++) {
		scanf("%lf%lf%lf", &c, &f, &x);
		double rate = 2.0, time = 0.0;
		while(x/rate > c/rate + x/(rate+f)) {
			time += c/rate;
			rate += f;
		}
		time += x/rate;
		printf("Case #%d: %.10f\n", cn, time);
	}
	return 0;
}