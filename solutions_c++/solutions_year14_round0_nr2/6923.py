#include<stdio.h>
int main()
{
	freopen("output.txt", "w", stdout);
	int t, i, j;
	double c, f, x, q;
	double min, sum;

	scanf("%d", &t);

	for (i = 1; i <= t; i++){
		q = 2;
		sum = 0;
		scanf("%lf %lf %lf", &c, &f, &x);
		min = x / q;
		for (j = 0;; j++){
			sum += c / q;
			q += f;
			if (sum >= min) break;
			if (sum + x / q < min) min = sum + x / q;
		}
		printf("Case #%d: %.7lf\n", i, min);
	}
}