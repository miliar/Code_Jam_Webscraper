/*
 * probc.cpp
 *
 *  Created on: 13-Apr-2013
 *      Author: ravi
 */
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cmath>
using namespace std;
#include "probc.h"

probc::probc() {
	// TODO Auto-generated constructor stub

}

probc::~probc() {
	// TODO Auto-generated destructor stub
}


bool probc::ispalin(unsigned long long a, unsigned long long b) {
	if (a == b)
		return true;

	return false;
}

unsigned long long probc::reverseNum(unsigned long long a) {
	unsigned long long rev = 0;
	unsigned long long temp = a;
	int rem = 0;
	while (temp) {
		rem = temp % 10;
		rev = rev * 10;
		rev += rem;
		temp = temp / 10;
	}

	return rev;
}

void probc::solve(char *inputFile) {
	ifstream input(inputFile);
	ofstream output("output.txt");

	string line;

	// Number of test cases
	getline (input, line);

	int testcases = atoi(line.c_str());

	int count = 1;
	unsigned long long start = 0, end = 0;
	unsigned long long fasnum = 0;
	while  (input.good()) {
		if (count > testcases)
			break;

		getline (input, line);
		stringstream stream(line);

		// I am expecting only two numbers here, so..
		stream >> start;
		stream >> end;

		fasnum = 0;
		for (unsigned long long i = start; i <= end; i++) {
			unsigned long long rev = reverseNum(i);
			if (true == ispalin(i, rev)) {
				unsigned long long sqrnum = sqrt(i);

				if ((sqrnum * sqrnum) != i)
					continue;

				unsigned long long revsqrnum = reverseNum(sqrnum);
				if (true == ispalin(sqrnum, revsqrnum)) {
					fasnum++;
				}
			}
		}

		output << "Case #" << count << ": ";
		output << fasnum << endl;
		count++;
	}

	input.close();
	output.close();
}
