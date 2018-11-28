#include <cstdio>
#define RI(a) scanf("%d", &(a))
#define REP(i, n) for (int i = 0; i < (int) (n); i++)
using namespace std;
double c, f, x;
double ff() {
	double oo = 0, ooo = x/2;
	for (int i = 0; i < 1000000; i++) {
		oo += c / (2 + i * f);
		if (oo + x / (2 + (i+1) * f)>ooo) return ooo;
		ooo=oo + x / (2 + (i+1) * f);
	}
}
int main() {
	int ttt, tt = 0;
	RI(ttt);
	while (tt++ < ttt) {
		printf("Case #%d: ", tt);
		scanf("%lf%lf%lf", &c, &f, &x);
		printf("%lf\n", ff());

	}
}
