#include <cstdio>

void work() {
	double c, f, x;
	scanf("%lf%lf%lf", &c, &f, &x);
	double r = 2.0;
	double t1 = 0;
	double t2 = c/r;
	while(t1 + x/r > t1 + t2 + x/(r+f)) {
		t1 += t2;
		r += f;
		t2 = c/r;
	}
	printf("%lf\n", t1 + x/r);
}

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i ++)
		printf("Case #%d: ", i), work();
	return 0;
}
