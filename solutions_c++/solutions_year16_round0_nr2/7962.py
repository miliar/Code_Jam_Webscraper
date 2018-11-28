// RevengeOfThePancakes.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <sstream>
#include <string> // this should be already included in <sstream>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int RevengeOfThePancakesCalc(string n)
{
	int maneuverNum = 0;
	int currentManuevervalue = 1;
	bool firstGoodCakeDone = false;
	char lastCake = '+';
	std::string::iterator it = n.begin();
	for (; it != n.end(); ++it)
	{
		if ((*it) == '+')
		{
			if (lastCake == '-')
				maneuverNum += currentManuevervalue;
			if (!firstGoodCakeDone)
				currentManuevervalue = 2;
			firstGoodCakeDone = true;
		}
		lastCake = (*it);
	}
	--it;
	if ((*it) == '-') maneuverNum += currentManuevervalue;

	return maneuverNum;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int t, result;
	string n;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> n;
		result = RevengeOfThePancakesCalc(n);
		cout << "Case #" << i << ": " << result << endl;
	}
	return 0;
}

