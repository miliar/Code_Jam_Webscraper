#include <cstdio>

int sol(int cse)
{
	double c,f,x,d;
	int i,j,k;
	double sum,presum;

	scanf("%lf %lf %lf", &c, &f, &x);

	
	for(d = 2.0, sum=0;1;)
	{
		if(sum+x/d < sum+c/d+x/(d+f))
		{
			printf("Case #%d: %lf\n", cse, sum + x/d);
			return 0;
		}
		else
		{
			sum += c/d;
			d += f;
		}
	}
}

int main()
{
	int t;
	int i;
	for(scanf("%d",&t), i=1; i<=t; sol(i), i++);
}