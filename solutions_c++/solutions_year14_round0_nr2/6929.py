#include<iostream>
#include<iomanip>
#include<cstdio>
using namespace std;
int main()
{
	double C,F,X;
	int t;
	
	freopen("input4.in","r",stdin);
	freopen("output4.txt","w",stdout);
	cout.precision(7);
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		double cPerSec=2.0;
		cin>>C;
		cin>>F;
		cin>>X;
		double time=0;
		double cookies=0;
		while(1)
		{
			cookies=C;
			time+=C/cPerSec;
			if((X-C)/cPerSec < X/(cPerSec+F))
			{
				time+=(X-C)/cPerSec;
				break;
			}
			else
			{
				cookies-=C;
				cPerSec+=F;
			}
		}
		printf("Case #%d: %.7f",k,time);
		printf("\n");
	    //cout<<"Case #"<<k<<": "<<setprecision(10)<<time<<"\n";
	}
	return 0;
}

