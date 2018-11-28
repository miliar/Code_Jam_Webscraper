#include <cstdio>
#define EPS 1e-7
int t;
long double c, f, x, cur_t, rate;
//if I jump by the number of cookies required for a farm, I shouldn't go over unless C > X, as long as I do my checks right.
//C is num required for farm; F is production of farm; X is target.
bool isEq(double a, double b) {
	return (a-b < EPS && b-a < EPS);
}
bool lEq(double a, double b) {
	return (a < b+EPS);
}
bool gEq(double a, double b) {
	return (a > b-EPS);
}
bool les(double a, double b) {
	return (a < b-EPS);
}
bool gre(double a, double b) {
	return (a > b+EPS);
}
int main() {
	freopen("cookiein.txt", "r", stdin);
	freopen("cookieout2.txt", "w", stdout);
	scanf("%d ", &t);
	for (int i = 1; i <= t; i++) {
		cur_t = 0;
		rate = 2;
		printf("Case #%d: ", i);
		scanf("%Lf %Lf %Lf ", &c, &f, &x);
		//may not need the following --> need to test
		if (gEq(c, x)) {
			printf("%Lf\n", x/rate);
			continue;
		}
		while (les(cur_t+c/rate+x/(rate+f), cur_t+x/rate)) {
			//buy a farm
			cur_t += c/rate;
			rate += f;
		}
		cur_t += x/rate;
		printf("%Lf\n", cur_t);
	}
	return 0;
}
