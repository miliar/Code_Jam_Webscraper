#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int T;
	double C,F,X;	
	//C: Farm's cost
	//F: Farm's production rate of cookies
	//X: Target number of cookies
	
	double rate;
	double estimatedTime;
	double timeToProduceCookies;
	double timeToBuyFarm;
	double timeToProduceCookiesWithNewRate;
	double u1, u2;
	


	cin>>T;
	for(int i=0; i<T; i++)
	{
		cin>>C>>F>>X;
		
		rate = 2; //rate of production
		estimatedTime = 0;
		

		while(1)
		{
			timeToProduceCookies = X/rate;
			timeToBuyFarm = C/rate;
			timeToProduceCookiesWithNewRate = X/(rate+F);

			u1 = timeToProduceCookies;
			u2 = timeToBuyFarm + timeToProduceCookiesWithNewRate;

			if(u1>u2)
			{
				estimatedTime += timeToBuyFarm;
				rate += F;
			}
			else
			{
				estimatedTime += timeToProduceCookies;
				break;
			}
				
		}		
		cout<<setprecision(7)<<fixed;
		cout<<"Case #"<<i+1<<": "<<estimatedTime<<endl;
	}
}
