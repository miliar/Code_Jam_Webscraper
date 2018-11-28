//============================================================================
// Name        : CookieClicker.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <boost/lexical_cast.hpp>
#include <boost/algorithm/string.hpp>
using namespace std;

int main() {
	ifstream inputFile("input.in");
	ofstream outputFile("output.out");

	string line;
	if(inputFile.is_open()) {
		getline(inputFile,line);

		int testCases = boost::lexical_cast<int>(line); //using functions from Boost library

		for(int i=0; i<testCases; i++) {

			double costFarm = 0.0;
			double rateIncrease = 0.0;
			double target = 0.0;

			double timetowin = 0.0;
			double cookieRate = 2.0;

			getline(inputFile,line);
			vector<string> strs;
			boost::split(strs,line,boost::is_any_of(" "));

			costFarm = boost::lexical_cast<double>(strs[0]);
			rateIncrease = boost::lexical_cast<double>(strs[1]);
			target = boost::lexical_cast<double>(strs[2]);

			while(true) { // decision making

				double timewithoutfarm = target / cookieRate;
				double timewithfarm = costFarm / cookieRate + target/(cookieRate + rateIncrease);

				if(timewithoutfarm < timewithfarm) { // do not build a farm
					timetowin += timewithoutfarm;
					break;
				} else { // build a farm
					timetowin += costFarm / cookieRate;
					cookieRate += rateIncrease;
				}
			}

			outputFile << setprecision(7) << fixed;
			outputFile << "Case #" << i+1 << ": " << timetowin << endl;
		}

	}

	inputFile.close();
	outputFile.close();
	return 0;
}
