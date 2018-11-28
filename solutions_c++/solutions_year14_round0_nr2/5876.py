#include <cstdio>

int ntest;

int main()
{
	scanf("%d", &ntest);
	for(int test = 1;test <= ntest;++test)
	{
		double C, F, X;
		double n = 0, rate = 2.0;
		scanf("%lf %lf %lf", &C, &F, &X);
		double mini = -1;
		double temp = 0;
		while(1)
		{
			double d = temp + X / rate;
			if(mini < 0 || d < mini)
				mini = d;
			else
				break;
			temp += C / rate;
			rate += F;
		}
		printf("Case #%d: ", test);
		printf("%.7lf\n", mini);
	}
}
