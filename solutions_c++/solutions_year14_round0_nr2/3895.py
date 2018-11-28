#include<iostream>
#include<cfloat>
#include <iomanip> 

using namespace std;

int main()
{
	int num = 0, cases = 1;
	cin >> num;
	while(cases <= num)
	{
		double rate = 2.0;
		double C, F, X;
		cin>>C>>F>>X;
		double cookies = 0;
		double time = 0;
		if(C > X)
		{
			time = X/rate;
			cookies = X;
		}
		else 
		{
			time += C/rate;
			cookies = C;
		}
		while(cookies < X)
		{
			double regularRemainingTime = (X - cookies)/rate;
			double newRemainingTime = DBL_MAX;
			newRemainingTime = X/(rate + F); 
			if(regularRemainingTime < newRemainingTime)
			{
				cookies = X;
				time += regularRemainingTime;
			}
			else
			{
				rate = rate + F;
				cookies = C;
				time += C/rate;
			}
		}
		cout<<"Case #"<<cases<<": "<<setprecision(7) << fixed<<time<<endl;
		cases++;
	}
	return 0;
}

