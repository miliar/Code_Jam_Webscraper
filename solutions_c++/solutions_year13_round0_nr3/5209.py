/*
 * main.cpp
 *
 *  Created on: Apr 12, 2013
 *      Author: Matt
 */


#include <iostream>
#include <fstream>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

//#define DEBUG 1

char* valueA = new char [64];
char* valueB = new char [64];

void flip(const char* src, char* dest) {
	int len  = strlen(src);

	if(len == 1) {
		dest[0] = src[0];
		dest[1] = '\0';
		return;
	}

	int last  = len - 1;
	int index = 0;

	for(; index < len; index++) {
		valueB[index] = valueA[last--];
	}

	valueB[index] = '\0';
}

long square_value(const long& value) {
	long double temp = sqrt(value);

	long convert = (long)(temp + 0.5);

#ifdef DEBUG
	cout << "Temp:    " << temp << endl
		 << "Convert: " << convert << endl;
#endif

	if((convert*convert) == value)
		return convert;
	else
		return -1L;
}

bool is_palidrome(const long& value) {
	itoa(value, valueA, 10);

	flip(valueA, valueB);

#ifdef DEBUG
	cout << "ValueA: " << valueA << endl
		 << "ValueB: " << valueB << endl;
#endif

	if(strcmp(valueA, valueB) == 0)
		return true;
	else
		return false;
}

long count_fas(const long& start, const long& end) {
	long count  = 0L;
	long square = 0L;

	for(long index=start; index <= end; index++) {
		if(is_palidrome(index) && ((square = square_value(index)) != -1L)) {
			if(is_palidrome(square))
				count++;
		}
	}

	return count;
}

int main(int argc, char** argv) {

	ifstream ifile("data/small.in");

	if(ifile.fail() || !ifile.is_open()) {
		cerr << "Could not open input file!" << endl;
		return 1;
	}

	ofstream ofile("data/output.txt");

	long testCount  = 0L;
	long startValue = 0L;
	long endValue   = 0L;

	ifile >> testCount;

	for(long test=0; test < testCount; test++) {
		ifile >> startValue >> endValue;

		ofile << "Case #" << (test+1) << ": " << count_fas(startValue, endValue) << endl;
	}

	ifile.close();

	ofile.flush();
	ofile.close();

	return 0;
}
