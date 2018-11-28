#include <fstream>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <iterator>
#include <string>
#include <limits>
#include <vector>

using namespace std;
int main(int argc, char** argv) {

	ofstream result;
	result.open ("OutputProblemTwo.txt");
	ifstream file;
	string lineBuffer;
	int numOfTestCases;
	int testCaseNum = 0;
	file.open("InputProblemTwo.txt"); //
	getline(file,lineBuffer);
	numOfTestCases = atoi(lineBuffer.c_str());
	while (!file.eof()) {
		getline(file, lineBuffer);
		if (lineBuffer.length() == 0)
			continue; //ignore all empty lines
		else {
			testCaseNum++;
			bool timeImproved = true;
			double C,F,X;
			double cookieRate = 2;
			double numOfFarms = 0;
			double totalTimesToBuyFarms = 0;
			double totalTimeToMakeXCookies = 0;
			double totalTime = 0;
			double optimalTime;
			std::istringstream buf(lineBuffer);
			std::istream_iterator<std::string> beg(buf), end;
			std::vector<std::string> tokens(beg, end);
			C = atof(tokens[0].c_str()); // Farm price
			F = atof(tokens[1].c_str()); // Cookies made by a farm
			X = atof(tokens[2].c_str()); // Total cookies
			optimalTime = X/cookieRate;

			while(timeImproved)
			{
				totalTimesToBuyFarms += C/cookieRate;
				cookieRate += F;
				totalTimeToMakeXCookies = X/cookieRate;
				totalTime = totalTimesToBuyFarms + totalTimeToMakeXCookies;
				if(totalTime < optimalTime)
				{
					optimalTime = totalTime;
					timeImproved = true;
				}
				else
					timeImproved = false;
			}
			cout.precision(7);
			result <<  "Case #"<< testCaseNum << fixed << ": " << optimalTime;
		}
		result << endl;
	}
	result.close();
	//getchar();
	return 0;
}
