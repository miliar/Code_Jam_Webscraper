#include <stdio.h>

int main()
{
	//freopen("B-large.in", "r", stdin);
	//freopen("B-l.out", "w", stdout);

	int t, cas;
	double c, f, x;
	double m;
	double res;

	scanf("%d", &t);
	for(cas=1; cas<=t; cas++)
	{
		scanf("%lf %lf %lf", &c, &f, &x);
		m=2;
		res=0;
		while((x-c)/m>x/(m+f))
		{
			res+=c/m;
			m+=f;
		}
		res+=x/m;
		printf("Case #%d: %lf\n", cas, res);
	}
}