#include <stdio.h>
int main()
{
	int T;
	double C,F,X;
	int caseCount;
	FILE *in = fopen("data.in","r");
	FILE *out = fopen("data.out","w");
	fscanf(in,"%d",&T);
	for(caseCount=1;caseCount<=T;caseCount++)
	{
		fscanf(in,"%lf %lf %lf",&C,&F,&X);
		double seconds=0.0,cookies=0.0;
		double speed=2.0;
		while(cookies<X)
		{
			//strategy judge
			if(cookies>=C)
			{
				double pointT = C/F;
				if(pointT > (X-cookies)/speed)
				{
					seconds += (X-cookies)/speed;
					cookies += (X-cookies);
				}
				else
				{
					cookies -= C;
					speed += F;
				}
			}
			else
			{
				if(X-cookies<C)
				{
					seconds+=((X-cookies)/speed);
					cookies+=(X-cookies);
				}
				else
				{
					cookies+=C;
					seconds +=(C/speed);
				}
			}
		}
		fprintf(out,"Case #%d: %.7lf\n",caseCount,seconds);
	}
	return 0;
}