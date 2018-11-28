#include <iostream>
#include <limits>
#include <assert.h>
using namespace std;

int main()
{
	int nCases = 0;
	cin >> nCases;
	for (int n = 0; n < nCases; n++) {
		// read first row
		
		double farmCost, farmProduce, goalNumber;
		cin >> farmCost >> farmProduce >> goalNumber;

		
		double prevTime = numeric_limits<double>().max();
		int nFarms = 0;
		double prevFarmsTime = 0;
		do {
			// calculate game time with nFarms in microseconds
			double currTime = 0;
			for (int i = 0; i < nFarms; i++) {
				currTime += farmCost * 1000000 / (2 + i*farmProduce);
			}
			currTime += goalNumber * 1000000 / (2 + nFarms*farmProduce);
			if (currTime < prevTime) {
				prevTime = currTime;
				nFarms++;
			} else {
				break;
			}
		} while (true);
		// output result
		cout.precision(12);
		cout << "Case #" << n + 1 << ": ";
		cout << prevTime / 1000000 << endl;
	}
}


