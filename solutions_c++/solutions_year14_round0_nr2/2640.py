#include <iostream>
using namespace std;

int main(void) {
	int numCases;
	double C, F, X;
	
	cin >> numCases;
	for (int numCase = 1; numCase <= numCases; numCase++) {
		double currentCookies = 0, currentTime = 0, cookiesPerSecond = 2;
		
		cin >> C >> F >> X;
		while (true) {
			double timeToWin = (X - currentCookies) / cookiesPerSecond;
			double timeToFarm = (C - currentCookies) / cookiesPerSecond;
			double timeLapse = min(timeToWin, timeToFarm);
			
			currentCookies += timeLapse * cookiesPerSecond;
			currentTime += timeLapse;
			
			if (currentCookies >= X) {
				break;
			} else {
				double timeToWinIfBuyFarm = X / (cookiesPerSecond + F);
				double timeToWinIfNotBuyFarm = (X - currentCookies) / cookiesPerSecond;
				
				if (timeToWinIfNotBuyFarm <= timeToWinIfBuyFarm) {
					currentTime += timeToWinIfNotBuyFarm;
					break;
				} else {
					currentCookies = 0;
					cookiesPerSecond += F;
				}
			}
		}
		
		cout.precision(7);
		cout << "Case #" << numCase << ": " << fixed << currentTime << endl;
	}
}
