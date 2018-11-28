#include<stdio.h>

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.txt","w",stdout);
	int runtime;
	scanf("%d",&runtime);
	for (int run = 1; run <= runtime; run++)
	{
		double income = 2.0000000,time = 0,c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		while ((x * f - c * income - c * f) > 0)
		{
			time += c / income;
			income += f;
		}
		time += x / income;
		printf("Case #%d: %.7f\n",run,time);
	}
}
