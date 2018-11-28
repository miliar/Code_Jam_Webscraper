#include <iostream>
#include <cstdio>
using namespace std;

double play(double C, double F, double X)
{
	double minTime=DBL_MAX;
	double time;
	for(int f=0;;f++)
	{
		time=0;
		for(int i=0;i<f;i++)
		{
			time+=C/(i*F+2);
		}
		time+=X/(f*F+2);
		if(time<minTime)
		{
			minTime=time;
		}
		else
			break;
	}
	return minTime;
}

int main()
{
	int T;
	cin >>T;
	for(int t=1;t<=T;t++)
	{
		double C,F,X;
		cin>>C>>F>>X;
		printf("Case #%d: %.7lf\n",t,play(C,F,X));
	}
	return 0;
}