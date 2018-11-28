#include <stdio.h>

int main()
{
	int T,c=1;
	scanf("%d",&T);
	while(T--)
	{
		double previous_time = 0;
		double total_time;
		double Cr = 2.0;
		double C,F,X;

		scanf("%lf%lf%lf",&C,&F,&X);

		while(true)
		{
			if((X/Cr) < ((C/Cr) + X/(Cr+F)))
			{
				total_time = previous_time + X/Cr;
				break;
			}
			else
			{
				previous_time+=C/Cr;
				Cr+=F;
			}
		}
		printf("Case #%d: %.7lf\n",c++,total_time);
	}
	return 0;
}