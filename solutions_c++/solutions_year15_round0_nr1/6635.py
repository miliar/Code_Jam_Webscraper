//============================================================================
// Name        : StandingOvation.cpp
// Author      : Sarah Lutteropp
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <stdlib.h>     /* atoi */
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main() {
	string numCases;

	string line;
	ifstream myfile("A-small-attempt0.in");
	if (myfile.is_open()) {
		getline(myfile, numCases);
		int n = atoi(numCases.c_str());

		for (int test = 0; test < n; test++) {
			std::vector<int> people;
			getline(myfile, line);
			for (size_t idx = 2; idx < line.size(); idx++) {
				people.push_back((int) (line.at(idx)) - 48);
			}

			int actThreshold = 0;
				int extra = 0;
				for (size_t i = 0; i < people.size(); i++) {
					int diff = i - actThreshold;
					if (diff > 0) {
						extra += diff;
						actThreshold += diff;
					}
					actThreshold += people[i];
				}

				cout << "Case #" << test + 1 << ": " << extra << endl;
		}

		myfile.close();
	}
	return 0;
}
