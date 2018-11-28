#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int t;
	double c,f,x;
	cin>>t;
	double t2[t];
	for(int i=0;i<t;i++)
	{
		double time=0;
		cin>>c;
		cin>>f;
		cin>>x;
		double rate=2;
		for(;;)
		{
			double r_c=c/rate;
			double r_x_next=x/(rate+f);
			double r_x=x/rate;
			if(r_x<=(r_c+r_x_next))
			{
			    time+=r_x;
			    t2[i]=time;
				break;	
			}
			else
			{
				time+=r_c;
				rate+=f;
				
			}
		}
		
	}
	
	for(int i=0;i<t;i++)
	{
		cout<<setprecision(7)<<fixed;
		cout<<"Case #"<<i+1<<": "<<t2[i]<<"\n";
	}
}