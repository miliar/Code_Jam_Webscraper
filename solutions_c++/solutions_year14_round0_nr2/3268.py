#include<stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;
int main() {
	double c, f, x;
	int testcase;
	cin >> testcase;
	for (int tc = 1; tc <= testcase; ++tc) {
		cin >> c;
		cin >> f;
		cin >> x;
		double timeSum = 0;
		double rate = 2;
		double tFinish = x / rate;

		//cout.precision(7);

		while (true) {
			//case buy new factory;
			double rateFactory = rate + f;
			double tBuildFactory = c / rate;
			double tFactoryFinish = timeSum + tBuildFactory + x / rateFactory;

			//cout << "tFinish" << tFinish << endl;
			//cout << "tFactory" << tFactoryFinish << endl;

			if (tFinish < tFactoryFinish) {
				break;
			}

			//buy new factory is better choice;
			rate = rateFactory;
			timeSum += tBuildFactory;
			tFinish = tFactoryFinish;
		}
		printf("Case #%d: %.7f\n", tc, tFinish);
		//system("pause");
	}
	return 0;
}