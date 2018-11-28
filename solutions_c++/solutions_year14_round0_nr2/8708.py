// Jai Mata Di
// https://code.google.com/codejam/contest/2974486/dashboard#s=p1
#include <iostream>
#include <cstdio>
#include <limits>
#include <iomanip>
using namespace std;
class CookieFactory {
	double costOfFarm;
	double increaseInRateOfCookieProduction;
	double targetCookieCount;
	double initialRateOfCookieProduction;
	double previousTimeForTarget;

public:
	CookieFactory() {
		cin >> costOfFarm >> increaseInRateOfCookieProduction >> targetCookieCount;
		initialRateOfCookieProduction = 2;
		previousTimeForTarget = std::numeric_limits<double>::max();
	}
	double findTimeToReachTarget(double currentTime, double rateOfCookieProduction, double cookieCount) {
		// Handle TODO: check <
		double timeForTarget = currentTime + (targetCookieCount / rateOfCookieProduction);
		//cout << timeForTarget << endl;
		if (timeForTarget > previousTimeForTarget)
			return previousTimeForTarget;
		else {
			previousTimeForTarget = timeForTarget;
			return findTimeToReachTarget(currentTime + (costOfFarm / rateOfCookieProduction),
					rateOfCookieProduction + increaseInRateOfCookieProduction, 0);
		}
	}
};
int main() {
	int noOfTestCases;
	cin >> noOfTestCases;
	for (int testCaseNo = 1; testCaseNo <= noOfTestCases; testCaseNo++) {
		CookieFactory c;
		double d = c.findTimeToReachTarget(0, 2, 0);
		printf("Case #%d: %.7lf\n", testCaseNo,d);
	}
	return 0;
}

