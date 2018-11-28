#include <iostream>
#include <iomanip>

using namespace std;

double produceCookies(double, double, double, double);

int main()
{
	int testCases = 0;
	double sFarmCost = 0;
	double sCookieRate = 0;
	double sGoal = 0;

	cin>>testCases;

	for (int i = 0; i < testCases; i++ ) {

		cin>>sFarmCost;
		cin>>sCookieRate;
		cin>>sGoal;

		double mustFinishWithin = sGoal/sCookieRate;

		cout<<"Case #"<<i+1<<": "<<setprecision(15)<<produceCookies(double(sGoal), 2.0, double(sFarmCost), double(sCookieRate))<<endl;

	}

	return 0;
}

double produceCookies(double currGoal, double currRate, double currFarmCost, double incRate) {

	// Time it will take to purchase next farm.
	double getFarmTime = currFarmCost/currRate;

	// Time it will take to finish without purchasing
	double finishNowTime = currGoal/currRate;
	double finishNextTime = getFarmTime + currGoal/(currRate + incRate);

	// The time it would've taken to finish the rest of the cookies
	double timeToFinish = (currGoal - currFarmCost)/currRate;

	if (finishNowTime < finishNextTime) {
		return finishNowTime;
	}

	return getFarmTime + produceCookies(currGoal, currRate + incRate, currFarmCost, incRate);

	// If it is faster to finish without buying a farm, then do so.
/*	if (mustFinishWithin < getAnotherFarmTime) {
		return finishNowTime;
	} else {
		return getAnotherFarmTime;
	}*/
}