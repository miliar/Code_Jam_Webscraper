// ConsoleApplication2.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
#pragma warning(disable: 4996) //Disabling use _s function warning.

#include<iostream>
#include<iomanip>

int _tmain(int argc, _TCHAR* argv[])
{

	using namespace std;

	int count;
	freopen("input.txt", "r", stdin);
	freopen( "C:\\Users\\veharshv\\Desktop\\output.txt", "w", stdout );
	cin>>count;

	double costOfFarm,enhancedRate,requiredCookies;

	double totalTime, totalCookies, currentRate;

	double timeIfBuy, timeIfNotBuy;

	for(int c=1;c<=count;c++)
	{		
		cin>>costOfFarm>>enhancedRate>>requiredCookies;

		totalTime = totalCookies = 0;
		currentRate = 2;

		bool flag = true;

		if(requiredCookies < costOfFarm)
		{
			totalTime = requiredCookies / 2.0;
			flag = false;
		}

		while(flag)
		{
			totalTime += (costOfFarm - totalCookies) / currentRate;
			totalCookies = costOfFarm;

			//Time require if not buy
			timeIfNotBuy = (requiredCookies - totalCookies) / currentRate;

			//Time is buy
			timeIfBuy = requiredCookies / (currentRate + enhancedRate);

			if(timeIfBuy < timeIfNotBuy)
			{
				totalCookies = 0;
				currentRate += enhancedRate;
			}
			else
			{
				totalTime += timeIfNotBuy;
				break;
			}
		}

		cout<<"Case #"<<c<<": "<<std::fixed << std::setprecision(7)<<totalTime<<endl;
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}

