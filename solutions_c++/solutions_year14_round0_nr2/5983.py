#include <stdio.h>

#define FOR(i,a) for(int i=0;i<a;i++)
#define FORS(i,s,e) for(int i=(s);i<(e);i++)

int readInt()
{
	int tmp;
	scanf("%d",&tmp);
	return tmp;
}

float readFloat()
{
	float tmp;
	scanf("%f",&tmp);
	return tmp;
}

double readDouble()
{
	double tmp;
	scanf("%lf",&tmp);
	return tmp;
}

void testcase(int caseNum)
{
	double c,f,x;
	c = readDouble();
	f = readDouble();
	x = readDouble();

	// printf("%lf %lf %lf\n",c,f,x);

	double total = 0.0;
	double farmRate = 2.0;
	while(1)
	{
		double timeToEndCurrent = x/farmRate;
		double timeToEndWithUpgrade = (c/farmRate)+(x/(farmRate+f));
		if(timeToEndCurrent < timeToEndWithUpgrade)
		{
			total += timeToEndCurrent;
			break;
		}
		else
		{
			total += (c/farmRate);
			farmRate += f;
		}
	}
	printf("%.8f \n",total);

}

int main()
{
	int T = readInt();
	FORS(i,1,T+1)
	{
		printf("Case #%d: ",i);
		testcase(i);
	}
	return 0;
}