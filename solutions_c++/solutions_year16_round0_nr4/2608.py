#include <iostream>
#include <fstream>

#include <string>
#include <sstream>
#include <cstdlib>
#include "math.h"
#include <vector>
#include <stack>
#include "BigNum.h"

using namespace std;

// open input and output files
// pre: user is prepared to enter file names at the keyboard
// post: files have been opened
void openFiles(ifstream &infile, ofstream &outfile);
bool differentBases(long double x, int length);
long double prime(long double x);
long double increment(long double x);
string format(long double x);


int main()
{/*
	cout << increment(101);
	std::vector<long double> coinjams[33];
	long double jams = 1;
	for (long double x = 1; x < 17; x++) {
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

	/*outfile << "Case #1:" << endl;
	BigNum y(10000000, 0, 0, 1);
	
	for (int q = 0; q < 500; q++) {
		BigNum base10 = y;
		BigNum base9(0, 0, 0, 0);
		BigNum base8(0, 0, 0, 0);
		BigNum base7(0, 0, 0, 0);
		BigNum base6(0, 0, 0, 0);
		BigNum base5(0, 0, 0, 0);
		BigNum base4(0, 0, 0, 0);
		BigNum base3(0, 0, 0, 0);
		BigNum base2(0, 0, 0, 0);
		BigNum holder = y;
		for (int w = 0; w < 32; w++) {
			long double temporary = holder.mod10();
			base9.add((temporary)*pow(9, w));
			base8.add((temporary)*pow(8, w));
			base7.add((temporary)*pow(7, w));
			base6.add((temporary)*pow(6, w));
			base5.add((temporary)*pow(5, w));
			base4.add((temporary)*pow(4, w));
			base3.add((temporary)*pow(3, w));
			base2.add((temporary)*pow(2, w));
			if (temporary == 0) {
				holder.divide10();
			}
			else {
				holder.divide10();
			}
		}
		double holder10 = 0;
		double holder9 = 0;
		double holder8 = 0;
		double holder7 = 0;
		double holder6 = 0;
		double holder5 = 0;
		double holder4 = 0;
		double holder3 = 0;
		double holder2 = 0;
		int sum = 0;
		bool valid = false;
		for (double x = 3; x < (4 * pow(10, 15)) && !valid; x += 2) {
			if (base10.divide(x)) {
				valid = true;
				holder10 = x;
			}
		}
		if (valid) {
			valid = false;
			for (double x = 3; x < (4 * pow(10, 15)) && !valid; x += 2) {
				if (holder9 == 0 && base9.divide(x)) {
					valid = true;
					holder9 = x;
				}
			}
			if (valid) {
				valid = false;
				for (double x = 3; x < (4 * pow(10, 15)) && !valid; x += 2) {
					if (holder8 == 0 && base8.divide(x)) {
						valid = true;
						holder8 = x;
					}
				}
				if (valid) {
					valid = false;
					for (double x = 3; x < (4 * pow(10, 15)) && !valid; x += 2) {
						if (holder7 == 0 && base7.divide(x)) {
							valid = true;
							holder7 = x;
						}
					}
					if (valid) {
						valid = false;
						for (double x = 3; x < (4 * pow(10, 15)) && !valid; x += 2) {
							if (holder6 == 0 && base6.divide(x)) {
								valid = true;
								holder6 = x;
							}
						}
						if (valid) {
							valid = false;
							for (double x = 3; x < (4 * pow(10, 15)) && !valid; x += 2) {
								if (holder5 == 0 && base5.divide(x)) {
									valid = true;
									holder5 = x;
								}
							}
							if (valid) {
								valid = false;
								for (double x = 3; x < (4 * pow(10, 15)) && !valid; x += 2) {
									if (holder4 == 0 && base4.divide(x)) {
										valid = true;
										holder4 = x;
									}
								}
								if (valid) {
									valid = false;
									for (double x = 3; x < (4 * pow(10, 15)) && !valid; x += 2) {
										if (holder3 == 0 && base3.divide(x)) {
											valid = true;
											holder3 = x;
										}
									}
									if (valid) {
										valid = false;
										for (double x = 3; x < (4 * pow(10, 15)) && !valid; x += 2) {
											if (holder2 == 0 && base2.divide(x)) {
												sum++;
												holder2 = x;
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}

			if (valid) {
				outfile << y.toPrint() << " "
					<< format(holder2) << " "
					<< format(holder3) << " "
					<< format(holder4) << " "
					<< format(holder5) << " "
					<< format(holder6) << " "
					<< format(holder7) << " "
					<< format(holder8) << " "
					<< format(holder9) << " "
					<< format(holder10) << endl;

			}
			else q--;
		

		cout << y.toPrint() << endl;
		y.increment();
		y.increment();
	}		/*outfile << "10000000";
			outfile << y;
			outfile << "0 2 3 4 5 6 7 8 9 10" << endl;
			cout << "10000000";
			cout << y;
			cout << "0 2 3 4 5 6 7 8 9 10" << endl;
			y = increment(y);*/


	

size_t num, k,c,s;
infile >> num;
for (int x = 1; x <= num; x++) {
	outfile << "Case #" << x << ":";
	infile >> k;
	infile >> c;
	infile >> s;
	for (int y = 1; y <= k; y++) {
		outfile << " " << y;
	}
	outfile << endl;
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



long double prime(long double x) {
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

bool differentBases(long double x, int length) {
	long double base10 = x;
	long double base9 = 0;
	long double base8 = 0;
	long double base7 = 0;
	long double base6 = 0;
	long double base5 = 0;
	long double base4 = 0;
	long double base3 = 0;
	long double base2 = 0;
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

long double increment(long double x) {
	long double checker = 10;
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
string format(long double x) {
	string s = "";
	while (x > 0) {
		long double temp = fmod(x, 10);
		char c = temp + '0';
		s = c+s;
		x = x - temp;
		x = x / 10;
	}
	return s;
}