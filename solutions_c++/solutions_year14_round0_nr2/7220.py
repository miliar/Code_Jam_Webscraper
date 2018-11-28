#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

double C, F, X;

inline double howMuchTimeToX(double production, double objective = X)
{
	//cout << "howMuchTimeToX = " << objective << " / " << production << endl;
	return objective / production;
}

inline double projectionBuyingFarm(double production)
{
	//cout << "projectionBuyingFarm : " ;
	double timeToBuyFarm = howMuchTimeToX(production, C);
	//cout << " timeToBuyFarm = " << timeToBuyFarm;
	double timeAfterBuyingFarm = howMuchTimeToX(production + F);
	//cout << ", timeAfterBuyingFarm = " << timeAfterBuyingFarm << endl;
	return timeToBuyFarm + timeAfterBuyingFarm;
}

int main()
{
	int T, i = 0;
	double timeToX, timeFarm, production, timeSpent, cookies;

	cin >> T;
	while(i++ < T)
	{
		cin >> C;
		cin >> F;
		cin >> X;
		timeFarm = 0.0;
		timeToX = 0.0;
		production = 2.0;
		timeSpent = 0.0;
		cookies = 0.0;

		//cout << "C = " << C << ", F = " << F << ", X = " << X << endl;
		while(1)
		{
			timeToX = howMuchTimeToX(production);
			timeFarm = projectionBuyingFarm(production);
			//cout << "Time To Get X = " << timeToX << endl;
			//cout << "Time To Get X buying Farm = " << timeFarm << endl;

			if(timeToX <= timeFarm)
			{
				timeSpent += timeToX;
				break;
			}
			else
			{
				timeSpent += howMuchTimeToX(production, C);
				production += F;
			}
		}

		printf("Case #%i: %.7lf\n", i, timeSpent);
		//cout << "Case #" << i << ": " << timeSpent << endl ;
	}

	return 0;
}