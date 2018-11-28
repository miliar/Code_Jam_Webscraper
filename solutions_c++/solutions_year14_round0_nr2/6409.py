#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include<iostream>
#include<vector>

using namespace std;


double requiredTimeInRate(double rate, double requiredCookie, double cookieInHand);
double requiredTimeWithNewFarm(double rate, double cookieInHand, double cForFarm, double firmRate,double X, double &time);


int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int testCases;

	cin>>testCases;

	for (int x = 1; x <= testCases; x++)
	{

		double C,F,X;
		cin>>C>>F>>X;

		double currentRate=2;
		double cookieInHand=0;
		long double spentSeconds =0;

		while (cookieInHand < X)
		{
			double time;
			//calculate which one is good new farm or going on
			double time1 = requiredTimeWithNewFarm(currentRate,cookieInHand,C,F,X, time);
			double time2 = requiredTimeInRate(currentRate,X,cookieInHand);

			if (time1 < time2)
			{
				//make new farm and update data
				spentSeconds += time;
				currentRate += F;
				cookieInHand = 0;
			}
			else
			{
				spentSeconds += time2;
				break;
				//cookieInHand = time2*currentRate;
			}
		}
		//cout<<"Case #"<<x<<": "<<spentSeconds<<endl; 
		printf("Case #%d: %.7f\n",x,spentSeconds);
	}

	return 0;
}

double requiredTimeInRate(double rate, double requiredCookie, double cookieInHand)
{
	return (requiredCookie - cookieInHand) / rate;
}

double requiredTimeWithNewFarm(double rate, double cookieInHand, double cForFarm, double firmRate,double X, double &time)
{
	double sec = 0;
	//first generate until we have enough cookie
	sec = (cForFarm - cookieInHand) / rate;

	time = sec;

	rate = rate + firmRate;
	cookieInHand = 0;

	double newSec = (X - cookieInHand) / rate;

	return sec + newSec;
}