#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t, ct = 1;
	freopen("B-large.in", "r", stdin);
	freopen("cc2", "w", stdout);
	scanf("%d", &t);
	while(t--) {
	int t, i, j;
	double C, F, X;
	scanf("%lf%lf%lf", &C, &F, &X);
	double a, b, c, d;
		c = 2.0;
		d = 0.0;
		a = X / 2;
		b = d + (C / c) + (X / (c + F));
		while (a > b) {
			d += (C / c);
			a = d + (X / (c + F));
			c += F;
			b = d + (C / c) + (X / (c + F));
		}
		printf("Case #%d: %.7lf\n", ct++, a);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
