// Uses gmp (The GNU Multiple Precision Arithmetic Library)
// Link with -lgmp -lgmpxx

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <cmath>
#include <gmpxx.h>

using namespace std;

void getInputFile(int argc, char* argv[], ifstream &inputFile)
{
	if (argc != 2) {
		cerr << "Require one argument (input file); exiting ...\n";
		exit(1);
	}
	string filename = argv[1];
	inputFile.exceptions(ifstream::failbit);
	inputFile.open(filename.c_str());
}

void getOutputFile(int argc, char* argv[], ofstream &outputFile)
{
	string filename = argv[1];
	unsigned dotIndex = filename.find_last_of('.');
	if (dotIndex != string::npos)
		filename.erase(dotIndex);
	filename += ".out";
	outputFile.exceptions(ofstream::failbit);
	outputFile.open(filename.c_str());
}

void processCase(istream& inputFile, ostream& outputFile)
{
	mpf_class r, t;
	inputFile >> r >> t;
	mpf_class nf = (-(2*r-1)+sqrt((2*r-1)*(2*r-1) + 8*t)) / 4.0; // floating point errors?
	mpz_class n = floor(nf);
//	cout << r << " " << t << " " << nf << " " << n << "\n";
	outputFile << n;
}

int main(int argc, char *argv[])
{
	ifstream inputFile;
	getInputFile(argc, argv, inputFile);
	ofstream outputFile;
	getOutputFile(argc, argv, outputFile);
	mpf_set_default_prec(160); // (10^18)^2 = 10^36 < 16^36 < 2^160

	int numCases;
	inputFile >> numCases >> ws;
	for (int caseIndex = 0; caseIndex < numCases; ++caseIndex) {
		outputFile << "Case #" << caseIndex+1 << ": ";
		processCase(inputFile, outputFile);
		outputFile << "\n";
	}
}


