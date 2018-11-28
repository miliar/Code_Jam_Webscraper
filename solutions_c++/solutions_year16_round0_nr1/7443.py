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
#include "bigInt.h"
int number;

void displayOutput(int testNumber, std::string result) {
	std::cout << "Case #" << testNumber << ": " << result << std::endl;

}

void displayVec(int testNumber, std::vector<int> vec) {
	std::cout << "Case #" << testNumber << ": ";
	std::vector<int>::iterator v = vec.begin();
	while (v != vec.end()) {
		std::cout << *v;
		v++;
	}
	std::cout << std::endl;
}

bool isFinish(std::vector<int> vec) {
	for (int i = 0; i < 10; i++) {
		std::vector<int>::iterator v = vec.begin();
		int isFinish = 0;
		while (v != vec.end()) {
			//std::cout << "value of v = " << *v << std::endl;
			if (*v == i) {
				isFinish = 1;
				break;
			}
			v++;
		}
		if (isFinish == 0) {
			return false;
		}
	}
	return true;
}

void solveProblem(int testNumber, std::string line) {
	std::string result;
	std::vector<int> vec;

	BigInt::Rossi n(line, BigInt::DEC_DIGIT);

	//int n = atoi(line.c_str());
	if (n == BigInt::Rossi(0)) {
		//std::cout <<n <<std::endl;
		displayOutput(testNumber, "INSOMNIA");
	} else {

		for (int i = 0; i < line.size(); i++) {
			int cnt = atoi(line.substr (i,1).c_str());
			//std::cout << "Name of v = " << cnt << std::endl;

			//Compare to push into vector
			std::vector<int>::iterator v = vec.begin();
			int ishas = 0;
			while (v != vec.end()) {
				//std::cout << "value of v = " << *v << std::endl;
				if(*v == cnt) {
					ishas = 1;
					break;
				}
				v++;
			}
			if (ishas == 0) {
				vec.push_back(cnt);
				if(isFinish(vec)) {
					displayOutput(testNumber, line);
					return;
				}
			}
		}
		int j = 1;
		while (j>0) {
			BigInt::Rossi result;
			result = n * j;
			std::string line1 = result.toStrDec();
			for (int i = 0; i < line1.size(); i++) {
				int cnt = atoi(line1.substr(i, 1).c_str());

				//Compare to push into vector
				std::vector<int>::iterator v = vec.begin();
				int ishas = 0;
				while (v != vec.end()) {
					if (*v == cnt) {
						ishas = 1;
						break;
					}
					v++;
				}
				if (ishas == 0) {
					vec.push_back(cnt);
					if (isFinish(vec)) {
						displayOutput(testNumber, line1);
						return;
					}
				}
			}
			j++;
		}
		//displayOutput(testNumber, line);
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
