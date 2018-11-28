#include<stdio.h>

double SimulateCookies(double c, double f, double x)
{
	double s=0.0;
	double currentrate = 2.0;
	bool work = true;
	while(work)
	{
		double timetotarget = x / currentrate;
		double timetofactory = c / currentrate;
		double timetotargetafterfactory = x/ (currentrate + f);
		if(timetotarget < timetofactory + timetotargetafterfactory)
		{
			s+=timetotarget;
			work = false;
		}
		else
		{
			currentrate += f;
			s+=timetofactory;
		}
	}
	return s;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w", stdout);
	int T;
	double C,F,X;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++)
	{
		scanf("%lf %lf %lf",&C,&F,&X);
		printf("Case #%d: %.7lf\n",cs,SimulateCookies(C,F,X));
	}
	return 0;
}