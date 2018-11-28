#include <stdio.h>

int main()
{
	int t;
	scanf("%d", &t);

	for(int nc=1; nc<=t; nc++)
	{
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		double ganho = 2;
		double total = 0;

		while(x/ganho > c/ganho + x/(ganho+f))
		{
			total += c/ganho;
			ganho += f; 
		}

		total +=x/ganho;

		printf("Case #%d: %0.7lf\n", nc, total);
	}
}
