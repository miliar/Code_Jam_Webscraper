#include<stdio.h>
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("m3.out", "w", stdout);
	int t, i, j, tot = 0;
	double c, f, x,a,p,q,b;
	scanf("%d", &t);
	while (t--) {
		tot++;
		p = 2.0;
		q = 0.0;
		scanf("%lf%lf%lf", &c, &f, &x);
		a = x / 2;
		b = q + (c / p) + (x / (p+f));
		while (a > b) {
			q = q + (c / p);
			a = q + (x / (p+f));
			p = p + f;
			b = q + (c / p) + (x / (p+f));
		}
		printf("Case #%d: %.7lf\n", tot, a);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
