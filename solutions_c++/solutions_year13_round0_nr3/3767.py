//============================================================================
// Name        : FairAndSquare.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
using namespace std;

bool is_palindrome(int n) {
	ostringstream oss;
	oss << n;
	string str = oss.str();
	int digits = (signed) str.length();
	for (int i=0; i<(digits+1)/2; ++i) {
		if (str[i] != str[str.length()-1-i]) {
			return false;
		}
	}
	return true;
}

int fairsquares(int start, int end) {
	int total = 0;
	start = ceil(sqrt(start));
	end = floor(sqrt(end));
	for (int i=start; i<=end; ++i) {
		if (is_palindrome(i) && is_palindrome(pow((float) i, 2))) {
			total += 1;
		}
	}
	return total;
}

int main(int argc, char** argv) {
	ifstream infile;
	int ncases;
	infile.open(argv[1]);
	infile >> ncases;
	for (int i=0; i<ncases; ++i) {
		int start = 0;
		int end = 0;
		infile >> start;
		infile >> end;
		cout << "Case #" << i+1 << ": " << fairsquares(start, end) << endl;
	}
}
