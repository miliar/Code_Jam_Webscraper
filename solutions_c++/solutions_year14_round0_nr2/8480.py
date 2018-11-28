// cards.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <iomanip>
#include "windows.h"
using namespace std;

bool checkbigger(double lhs, double rhs) {
	return lhs > rhs;	
}

int _tmain(int argc, _TCHAR* argv[])
{
	//Sleep(10*1000);
	int t = 0;
	cin >> t;
	for (auto i = 0; i < t; ++i) {
		double c, f, x;
		c = f = x = 0;
		cin >> c >> f >> x;

		double total = 0;
		double rate  = 2;
		double timetofarm = c/rate;
		double timetocomplan = x / rate;

		while (1) {
			
			if (checkbigger(timetofarm, timetocomplan)) {
				total += timetocomplan;
				break;
			}

			double newrate = rate + f;
			double sim = timetofarm + x / newrate;

			if (checkbigger(sim, timetocomplan)) {
				total += timetocomplan;
				break;
			}

			total += timetofarm;
			rate  = newrate;
			timetofarm = c/rate;
			timetocomplan = x / rate;
		} // while

		cout << "Case #" << i+1 <<": " << fixed << setprecision(7) << total << endl;

	} // i
	return 0;
}

