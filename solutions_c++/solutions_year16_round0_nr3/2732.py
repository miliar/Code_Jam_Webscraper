#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include "math.h"
#include <vector>
#include <stack>

using namespace std;

// open input and output files
// pre: user is prepared to enter file names at the keyboard
// post: files have been opened
void openFiles(ifstream &infile, ofstream &outfile);
bool differentBases(double x, int length);
double prime(double x);
double increment(double x);
string format(double x);


int main()
{/*
	cout << increment(101);
	std::vector<double> coinjams[33];
	double jams = 1;
	for (double x = 1; x < 17; x++) {
		while (jams < pow(10, x)) {
			if (differentBases(jams,x)) {
				coinjams[x].push_back(jams);
			}
			jams = increment(jams);
		}
	}*/
	// open input & output data files
	
	ifstream infile;
	ofstream outfile;
	openFiles(infile, outfile);

	cout << "Reading the input file..." << endl;

	outfile << "Case #1:" << endl;
	double y = 1000000000000001;
	
	for (int x = 0; x < 50; x++) {
			double base10 = y;
			double base9 = 0;
			double base8 = 0;
			double base7 = 0;
			double base6 = 0;
			double base5 = 0;
			double base4 = 0;
			double base3 = 0;
			double base2 = 0;
			double holder = y;
			for (int w = 0; w < 16; w++) {
				double temporary = fmod(holder, 10);
				base9 += (temporary)*pow(9, w);
				base8 += (temporary)*pow(8, w);
				base7 += (temporary)*pow(7, w);
				base6 += (temporary)*pow(6, w);
				base5 += (temporary)*pow(5, w);
				base4 += (temporary)*pow(4, w);
				base3 += (temporary)*pow(3, w);
				base2 += (temporary)*pow(2, w);
				if (temporary == 0) {
					holder = holder / 10;
				}
				else {
					holder--;
					holder = holder / 10;
				}
			}
			base10 = prime(base10);
			if (base10 == 0) {
				x--;
			}
			else {
				base2 = prime(base2);
				if (base2 == 0) {
					x--;
				}
				else {
					base3 = prime(base3);
					if (base3 == 0) {
						x--;
					}
					else {
						base4 = prime(base4);
						if (base4 == 0) {
							x--;
						}
						else {
							base5 = prime(base5);
							if (base5 == 0) {
								x--;
							}
							else {
								base6 = prime(base6);
								if (base6 == 0) {
									x--;
								}
								else {
									base7 = prime(base7);
									if (base7 == 0) {
										x--;
									}
									else {
										base8 = prime(base8);
										if (base8 == 0) {
											x--;
										}
										else {
											base9 = prime(base9);
											if (base9 == 0) {
												x--;
											}
											else {
												/*string out = "";
												double holder = y;
												for (size_t q = 0; q < 16; q++) {
													int temp = fmod(y, 10);
													if (temp == 0) {
														out = '0' + out;
														y = y / 10;
													}
													else {
														out = '1' + out;
														y = y - 1;
														y = y / 10;
													}
												}
												y = holder;*/
												outfile << format(y) << " " << format(base2) 
													<< " " << format(base3)
													<< " " << format(base4)
													<< " " << format(base5)
													<< " " << format(base6)
													<< " " << format(base7)
													<< " " << format(base8)
													<< " " << format(base9)
													<< " " << format(base10) << endl;
												cout << x << ": " << format(y) << endl;
											}
										}
									}
								}
							}
						}
					}
				}
			}
			y = increment(y);
			y = increment(y);
			/*outfile << "10000000";
			outfile << y;
			outfile << "0 2 3 4 5 6 7 8 9 10" << endl;
			cout << "10000000";
			cout << y;
			cout << "0 2 3 4 5 6 7 8 9 10" << endl;
			y = increment(y);*/
	}






	// close the files
	infile.close();
	outfile.close();
	cout << "Done." << endl;
	
}


// open input and output files
// pre: user is prepared to enter file names at the keyboard
// post: files have been opened
void openFiles(ifstream &infile, ofstream &outfile)
{

	// open input data file
	string inFileName;
	cout << "Enter the name of the input file: ";
	cin >> inFileName;
	infile.open(inFileName.c_str());
	if (infile.fail()) {
		cout << "Error opening input data file" << endl;
		char junk;
		cout << "press enter to exit";
		junk = cin.get();
		junk = cin.get();
		exit(1);
	}

	// open output data file
	string outFileName;
	cout << "Enter the name of the output file: ";
	cin >> outFileName;
	outfile.open(outFileName.c_str());
	if (outfile.fail()) {
		cout << "Error opening output data file" << endl;
		char junk;
		cout << "press enter to exit";
		junk = cin.get();
		junk = cin.get();
		exit(1);
	}

}



double prime(double x) {
	bool isprime = true;
	if (x == 2) {
		return false;
	}
	for (int i = 3; i <= sqrt(x); i += 2)
	{
		if ((fmod(x,i)) == 0)
		{
			return i;
			
		}
	}

	return 0;
}

bool differentBases(double x, int length) {
	double base10 = x;
	double base9 = 0;
	double base8 = 0;
	double base7 = 0;
	double base6 = 0;
	double base5 = 0;
	double base4 = 0;
	double base3 = 0;
	double base2 = 0;
	for (int y = 0; y < length; y++) {
		base9 += ((fmod(x,10)))*pow(9, y);
		base8 += ((fmod(x,10)))*pow(8, y);
		base7 += ((fmod(x,10)))*pow(7, y);
		base6 += ((fmod(x,10)))*pow(6, y);
		base5 += ((fmod(x,10)))*pow(5, y);
		base4 += ((fmod(x,10)))*pow(4, y);
		base3 += ((fmod(x,10)))*pow(3, y);
		base2 += ((fmod(x,10)))*pow(2, y);
	}
	return (!prime(base10) && !prime(base9) && !prime(base8) && !prime(base7) && !prime(base6) && !prime(base5) && !prime(base4) && !prime(base3) && !prime(base2));
}

double increment(double x) {
	double checker = 10;
	while (true) {
		if (fmod(x,checker) == 0)
		{
			return x + (checker / 10);
		}
		else {
			return 10 * increment((x-1) / 10);
		}
		checker *= 10;
	}
}
string format(double x) {
	string s = "";
	while (x > 0) {
		double temp = fmod(x, 10);
		char c = temp + '0';
		s = c+s;
		x = x - temp;
		x = x / 10;
	}
	return s;
}