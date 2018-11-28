#include <iostream>
#include <stdio.h>
#include <iomanip>
#include <stdlib.h>
using namespace std;

double buyFarm(double c,double rate,double x,double rateIncrease,double,double);

int main()
{
	double c,f,x;
	double time;
		
	int t;
	freopen("B-small-attempt3.in","r+",stdin);
	freopen("B-small-attempt3.out","w+",stdout);
	cin>>t;

	for(int i=0;i<t;i++)
	{
		cin >>c>>f>>x;
		double currentrate=2;
		if(x<c)
		{
			time=x/2.0;
			cout<<std::setprecision(7)<<std::fixed<<"Case #"<<i+1<<": "<<time<<endl; 
		}
		else
		{
			double rate=2.0;
			int count = 0;
			double z=buyFarm(c,rate,x,f,x/rate,0);
			cout<<std::setprecision(7)<<std::fixed<<"Case #"<<i+1<<": "<<z<<endl; 
		}
	}

}


double buyFarm(double c,double rate,double x,double rateIncrease,double utime,double lasttime)
{

	double time=utime;
	double newRate=rate+rateIncrease;
	double time1=lasttime+(c/rate)+x/newRate;
	double time2=lasttime+(c/rate);
	if(time <=time1)
		return time;
	else
		buyFarm(c,newRate,x,rateIncrease,time1,time2);
}




		
