//============================================================================
// Name        : FairnSquare.cpp
// Author      : 
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>

using namespace std;

bool isFair(unsigned long long n) {
	stringstream ss;
	ss << n;
	string s = ss.str();
	size_t s_size = s.size();
	int floor_s_size_2 = floor(s_size/2);
	for (int i(0); i < floor_s_size_2; ++i) {
		if (s[i] != s[s_size-1-i]) {
			return false;
		}
	}
	return true;
}

bool isSquare(unsigned long long n) {
	double d_sqrt = sqrt( n );
	unsigned long long ul_sqrt = d_sqrt;
	return (ul_sqrt == d_sqrt) && isFair(ul_sqrt);
}

unsigned long long process_case(ifstream* piFile) {
	unsigned long long A, B;
	*piFile >> A;
	*piFile >> B;
	cout << "A = " << A << ", B = " << B << endl;

	unsigned long long r = 0;

	for (unsigned long long i = A; i <= B; ++i) {
		if (isFair(i) && isSquare(i)) {
			++r;
		}

	}

	return r;
}

void process_file(ifstream* piFile, ofstream* poFile) {
	size_t T;
	*piFile >> T;
	cout << "The input file contains " << T << " test cases." << endl;

	for (size_t i(1); i < T+1; ++i) {
		cout << "Case " << i << endl;
		*poFile << "Case #" << i << ": " << process_case(piFile) << endl;
	}

}


int main(int argc, char ** argv) {
	if (argc != 2) {
		cout << "Usage: " << argv[0] << " input-file" << endl;
		return 0;
	}

	string iFilePath(argv[1]);
	ifstream iFile(iFilePath.c_str(), ios::in);
	if (!iFile.is_open()) {
		cout << "Error: Could not open input file [ " << iFilePath << "]." << endl;
		return 1;
	}
	stringstream oFilePath;
	oFilePath << iFilePath << "-output.txt";
	ofstream oFile(oFilePath.str().c_str(), ios::out);
	if (!oFile.is_open()) {
		cout << "Error: Could not open output file [ " << oFilePath << "]." << endl;
		iFile.close();
		return 1;
	}

	process_file(&iFile, &oFile);

	cout << "End." << endl;
	iFile.close();
	oFile.close();
	return 0;
}
