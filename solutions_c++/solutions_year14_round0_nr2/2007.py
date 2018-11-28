#include <iostream>
#include <iomanip>      // std::setprecision

using namespace std;

int main(int argc, char const *argv[])
{
	int testCases;
	cin >> testCases;

	for (int i=0; i<testCases; i++) {
		long double farmPrice, farmRevenue, winningCookies;
		cin >> farmPrice;
		cin >> farmRevenue;
		cin >> winningCookies;

		long double cookiesPerSecond = 2.0;
		long double totalTime = 0.0;

		while (true) {
			long double timeUntilNextFarm = farmPrice/cookiesPerSecond;
			long double nextTimeUntilWin = winningCookies/(cookiesPerSecond + farmRevenue);
			long double timeUntilWinningCookies = winningCookies/cookiesPerSecond;

			if (nextTimeUntilWin + timeUntilNextFarm > timeUntilWinningCookies) {
				totalTime = totalTime + timeUntilWinningCookies;
				break;
			}
			else { //Buy farm
				totalTime = totalTime + timeUntilNextFarm;
				cookiesPerSecond = cookiesPerSecond + farmRevenue;
			}
		}

		cout << "Case #" << i + 1 << ": ";
		printf("%.7Lf\n",totalTime); 
	}


	return 0;
}