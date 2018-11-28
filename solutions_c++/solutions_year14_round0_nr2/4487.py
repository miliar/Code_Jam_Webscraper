#include <stdio.h>
int main()
{
	int t, i, j, integer;
	double c, f, x, tmp, count;
	scanf("%d", &t);
	for( i = 0; i < t; i++) {
		count = 0;
		scanf("%lf %lf %lf", &c, &f, &x);
		tmp = (f*x/c - 2)/f;
		integer = (int)tmp;
		if(integer > 0) {
			for( j = 0; j < integer; j++)
		  		count += c/(2 + f * j);
			count += x/(2 + f * integer);
		  	printf("Case #%d: %.7lf\n", i+1,count);
		}
		else
		  printf("Case #%d: %.7lf\n", i+1,x/2);
	}
	return 0;
}
