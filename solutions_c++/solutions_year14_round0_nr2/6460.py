#include<iostream>
#include<stdio.h>
#include<math.h>
#include<iomanip>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int cse=1;cse<=t;cse++)
	{
		double c,f,x,sum=0,rate=2;
		cin>>c>>f>>x;
		double val=0;
		while(1)
		{
			double currTime=x/rate;
			double incTime=c/(rate);
			double newTime=x/(rate+f);
			if(currTime<(incTime+newTime))
			{
				sum+=currTime;
				break;
			}
			else
			{
				sum+=(incTime);
				rate+=f;
			}
//cout<<currTime<<"\t"<<incTime+newTime<<"\t"<<sum<<endl;
		}
std::cout << std::fixed;
		cout<<"Case #"<<cse<<": "<<std::setprecision(7)<<sum<<endl;
	}

	return 0;
}
