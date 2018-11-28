#include<iostream>
#include<iomanip>
#include<cstdio>
using namespace std;
double t,c,f,x,r;
int main()
{
	double time1,time2,time3,time;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		r=2.0;
		time=0.0,time1=0.0,time2=0.0,time3=0.0;
		cin>>c>>f>>x;
		time=c/r;
		time2=x/r;
		if((c/r)>=(x/r))
		{
			time=x/r;
		}
		else
		{
			while(1)
			{
				r+=f;
				time1=time+(c/r);
				time3=time2;
				time2=time+(x/r);
				if(time3<time2)
				{
					time=time3;
					break;
				}
				else
				{
					time=time1;
				}
			}
		}
		cout<<"Case #"<<i+1<<": ";
		printf("%0.7lf\n",time);
	}
}
