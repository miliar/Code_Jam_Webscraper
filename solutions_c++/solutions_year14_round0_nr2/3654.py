#include<iostream>
#include<iomanip>

bool shouldIBuyFactory(double C, double F, double X, double cookpersec) {
	return ((C / cookpersec) + (X / (cookpersec + F))) < (X / cookpersec);
}


int main(void) {
	int cases;
	std::cout << std::fixed;
	std::cin >> cases;
	int current = 1;
	while (cases--) {
		double C, F, X;
		std::cin >> C >> F >> X;

		double timeSpentTillNow = 0.0;
		//int currentFarms = 0;
		double currentCookiesPerSec = 2.0;

		while (shouldIBuyFactory(C, F, X, currentCookiesPerSec)) {
			//currentFarms++;
			timeSpentTillNow += C / currentCookiesPerSec;
			currentCookiesPerSec += F;
		}
		timeSpentTillNow += X / currentCookiesPerSec;

		std::cout << "Case #" << current << ": ";
		current++;
		std::cout << std::setprecision(7) << timeSpentTillNow << std::endl;
	}
	return 0;
}
