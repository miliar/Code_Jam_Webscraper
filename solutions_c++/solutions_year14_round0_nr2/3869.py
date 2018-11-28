#include<iostream>
#include <iomanip>

using namespace std;

double solve(double farmCost, double farmBonus, double objective);
int evalFarmBuy(double currCookies, double currProd, double farmCost, double farmBonus, double objective);
double advance(double currCookies, double currProd, double farmCost, double objective);

void main()
{
	cout << fixed;
	cout << setprecision(7);
	
	int cases;
	cin >> cases;
	
	for(int c = 1; c <= cases; c++)
	{
		double farmCost, farmBonus, objective;
		
		cin >> farmCost >> farmBonus >> objective;
		
		double ans = solve(farmCost, farmBonus, objective);
		
		cout << "Case #" << c << ": " << ans << endl;		
	}
}

double solve(double farmCost, double farmBonus, double objective)
{
	double currProd = 2;
	
	double currTime = 0;	
	double currCookies = 0;
		
	while(currCookies < objective)
	{			
		int eval = evalFarmBuy(currCookies, currProd, farmCost, farmBonus, objective);
			
		if (eval == 1)
		{			
			currCookies -= farmCost;
			currProd += farmBonus;			
		}
		else if (eval == 2)
		{
			double cookiesMissing = objective - currCookies;
			double timeMissing = cookiesMissing / currProd;		
			
			currCookies += cookiesMissing;
			currTime += timeMissing;
			break;
		}
		
		double advanceTime = advance(currCookies, currProd, farmCost, objective);
		
		currCookies += currProd * advanceTime;
		currTime += advanceTime;
	}
	
	return currTime;
}

double advance(double currCookies, double currProd, double farmCost, double objective)
{
	double timeToNextFarm = (farmCost - currCookies) / currProd;

	double timeToEnd = (objective - currCookies) / currProd;

	if (timeToNextFarm < timeToEnd)
	{
		return timeToNextFarm;
	}
	
	return timeToEnd;
}

// 0: Cant afford
// 1: Buy
// 2: Never buy again
int evalFarmBuy(double currCookies, double currProd, double farmCost, double farmBonus, double objective)
{
	if (currCookies < farmCost)
	{
		return 0;
	}
	
	double cookiesMissing = objective - currCookies;
	double timeMissing = cookiesMissing / currProd;
		
	double newProd = currProd + farmBonus;
	double newCookiesMissing = objective - (currCookies - farmCost);
	double newTimeMissing = newCookiesMissing / newProd;
		
	if (newTimeMissing < timeMissing)
	{
		return 1;
	}
	else
	{
		return 2;
	}
}