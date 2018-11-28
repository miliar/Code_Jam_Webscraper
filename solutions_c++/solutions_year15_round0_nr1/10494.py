// Standing_Ovation.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <iterator>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm> // for std::copy
using namespace std;

std::vector<int> readFile(string fname);
void calculate(int tests, std::vector<int> cases);

int _tmain(int argc, _TCHAR* argv[])
{
	std::vector<int> audience = readFile("A-small-attempt0.in");
	//cout << "Tests: " << audience.at(0) << "\n";
	int testCases = audience.at(0);
	audience.erase(audience.begin());
	audience.erase(audience.begin());
	audience.erase(audience.begin());
	//cout << "Tests: " << testCases << "\n";

	//calculate(testCases, audience);
	calculate(100, audience);
	return 0;
}

void calculate(int tests, std::vector<int> cases) {
	int i = 0;
	int k = 0;
	while(i < tests) {
		cout << "Case #" << (i+1) << ": ";
		int maxShy = (int)cases.at(k);
		int up = 0;
		int add = 0;
		
		//cout << "Max Shy: " << maxShy << " Aud: ";
		for(int j=0; j<maxShy+1; j++) {
			if(j == 0 && cases.at(k+1) == 0) {
				//up += cases.at(k+1);
				add++;
				up++;
			} else {
				if(up >= j) {
					up += cases.at(k+1);
				} else {
					// Need to add
					up += cases.at(k+1);
					add++;
					up++;
				}
			}
			//cout << cases.at(k+1) << " ";
			k++;
		}
		//cout << "Up: " << up << " ";
		//cout << "Add: " << add << "\n";
		cout << add << "\n";
		k++;
		i++;
	}
}

std::vector<int> readFile(string fname) {
	std::ifstream is(fname);
	std::istream_iterator<char> start(is), end;
	std::vector<char> chars(start, end);
	//std::cout << "Read " << chars.size() << " numbers" << std::endl;

	std::vector<int> numbers;

	for(int i=0; i<chars.size(); i++) {
		numbers.push_back(chars.at(i) - '0');
	}

	// print the numbers to stdout
	/*std::cout << "numbers read in:\n";
	std::copy(numbers.begin(), numbers.end(), 
            std::ostream_iterator<string>(std::cout, " "));
	std::cout << std::endl;*/
	return numbers;
}


