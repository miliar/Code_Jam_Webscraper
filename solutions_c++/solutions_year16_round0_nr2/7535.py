/*
 * main.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: letronggiap
 */
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
int number;
using namespace std;
void displayOutput(int testNumber, int result) {
	std::cout << "Case #" << testNumber << ": " << result << std::endl;

}

void solveProblem(int testNumber, std::string line) {
	std::vector<int> vec;


	for (int i = 0; i < line.size(); i++) {
		std::string str = line.substr(i, 1).c_str();
		if (str.compare("-") == 0) {
			vec.push_back(0);
		}
		if (str.compare("+") == 0) {
			vec.push_back(1);
		}
	}

	std::vector<int>::iterator v = vec.begin();
	int valPre = 0;
	int first = 0;
	int result = 0;
	while (v != vec.end()) {
		//std::cout << "value of v = " << *v << std::endl;
		if (first == 0) {
			first++;
		} else {
			if (valPre != *v) {
				result++;
			}
		}
		valPre = *v;
		v++;

	}

	if (result == 0) {
		  while (!vec.empty())
		  {
		    int r = vec.back();
		    if (r == 0) {
		    	std::cout << "Case #" << testNumber << ": " << 1 << std::endl;

		    } else {
		    	std::cout << "Case #" << testNumber << ": " << 0 << std::endl;

		    }
		    return;
		  }
	}

	 while (!vec.empty()) {
		int r = vec.back();

		if (r == 0) {
			std::cout << "Case #" << testNumber << ": " << result + 1 << std::endl;

		} else {
			std::cout << "Case #" << testNumber << ": " << result << std::endl;

		}
	    return;

	}
}


void readInput(std::string filename) {
	std::ifstream source;
	source.open(filename);
	std::string line;
	int i = 0;
	while (std::getline(source, line)) {
		if (i == 0) {
			number = atoi(line.c_str());
			//printf("number: %d\n",number);

		} else {
			//std::cout << "Case #" << i << ": " << line << std::endl;

			solveProblem(i, line);
		}
		i++;
	}

}

int main(int argc, char *argv[]) {
	std::string fileInput(argv[1]);
	readInput(fileInput);
	return 0;
}
