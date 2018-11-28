#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <queue>
// Developed in Visual Studio 2013

class CookieClicker {
public:
	// costOfFarm is C, cookiesPerFarm is F, goal is X
	CookieClicker(double costOfFarm, double cookiesPerFarm, double goal) {
		result = 0;
		bool optimized = false;
		int farms = 0;
		while (!optimized) {
			// Invariant: cookies = 0;
			// Case 1: Buy new cookie farm ASAP
			double timeToNextFarm = costOfFarm / (cookiesPerFarm * farms + 2);
			double timeToGoalWFarm = timeToNextFarm + goal / (cookiesPerFarm * (farms + 1) + 2);
			// Case 2: Don't buy new cookie farm ASAP
			double timeToGoalDefault = goal / (cookiesPerFarm * farms + 2);

			if (timeToGoalWFarm < timeToGoalDefault) { // If buying a farm would mean getting to the goal faster
				farms++;
				result += timeToNextFarm;
			}
			else {
				result += timeToGoalDefault;
				optimized = true;
			}
		}
	}
	double answer() {
		return result;
	}
private:
	double result;
};

int main() {
	FILE *fp = fopen("output.txt", "w");
	if (fp == NULL)
	{
		printf("Error opening file!\n");
		exit(1);
	}

	std::ifstream input("input.in");
	if (input.is_open()) { // Input file found
		std::string line;
		getline(input, line);
		int numTestCases = atoi(line.c_str());
		for (int k = 0; k < numTestCases; k++) { // For each test case

			getline(input, line);

			std::istringstream parameters(line);
			std::string temp;
			parameters >> temp;

			double c = atof(temp.c_str());
			parameters >> temp;
			double f = atof(temp.c_str());
			parameters >> temp;
			double x = atof(temp.c_str());

			CookieClicker testCase(c, f, x);
			fprintf(fp, "Case #%d: %.7f\n", k + 1, testCase.answer());
		}
		input.close();
		fclose(fp);

		return 0; // End Program
	}
	else {
		std::cout << "No input file found";
		return 0; // Abort
	}
}