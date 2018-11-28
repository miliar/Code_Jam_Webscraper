#include <iostream>
#include <cstdio>
using namespace std;


int main()
{
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		double c,f,x;
		cin>>c;
		cin>>f;
		cin>>x;
		double totaltime=0;
		double time1=0;
		double time2=0;
		double rate=2;
		while(1)
		{
			time1=x/rate;
			time2=(c/rate)+x/(rate+f);
			if(time1<time2)
			{
				totaltime+=time1;
				break;
			}
			else
			{
				
				totaltime+=c/rate;
				rate=rate+f;
			}

		}
		cout.precision(7);
		cout<<"Case #"<<i+1<<": ";
		printf("%.7lf\n",totaltime);
	}
}