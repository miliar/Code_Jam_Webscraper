#include <cstdio>

long double go(long double c, long double f, long double x, long double plus){
	long double now = 0;
	if (x / plus < c / plus + x / (plus + f)) return x / plus;
	return c / plus + go(c, f, x, plus + f);
}


int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++){
		long double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);
		printf("Case #%d: %.7lf\n",tt,go(c, f, x, 2));
	}
}