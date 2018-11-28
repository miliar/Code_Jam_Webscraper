#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

void solve(int test)
{
	double timeToFarm;
	double timeToWin;
	double timeToWinWithFarm;
	double farmCost;
	double farmCookies;
	double totalGain = 2;
	double winCookies;
	double totalTime = 0;
	bool won = false;
	
	cin >> farmCost;
	cin >> farmCookies;
	cin >> winCookies;
	
	while(!won)
	{
		timeToWin = winCookies/totalGain;
		timeToFarm = farmCost/totalGain;
		timeToWinWithFarm = timeToFarm + (winCookies/(totalGain+farmCookies));
		
		if(timeToWin < timeToWinWithFarm)
		{
			totalTime += timeToWin;
			won = true;
		}
		else
		{
			totalTime += timeToFarm;
			totalGain += farmCookies;
		}
	}
	
	cout << "Case #" << test << ": " << totalTime << "\n";
}

int main()
{
	int tests;
	
	cin >> tests;
	tests++;
	cout << setprecision(7);
	cout << fixed;
	
	for(int test=1; test<tests; test++)
	{
		solve(test);
	}

	return(0);
}