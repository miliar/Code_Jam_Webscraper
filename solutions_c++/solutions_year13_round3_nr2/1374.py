#include <cassert>
#include <cmath>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>

// #include <gmpxx.h>


using namespace std;


void read_and_solve(istream &in, ostream &out)
{
	int T;
	in >> T;

	for (int t = 0 ; t < T ; t++) {
		int X, Y;
		in >> X >> Y;

		out << "Case #" << (t+1) << ": ";

		for (int i = 0 ; i < (abs(X)) ; i++) {
			if (X < 0)
				out << "EW";
			else
				out << "WE";
		}

		for (int i = 0 ; i < (abs(Y)) ; i++) {
			if (Y < 0)
				out << "NS";
			else
				out << "SN";
		}

		out << endl;
	}
}


int main(int argc, char **argv) {
	if (argc < 2) {
		cerr << "Not enough parameters" << endl;
		return 1;
	}

	std::string input_file(argv[1]);
	ifstream input(input_file);
	if (!input.is_open()) {
		cerr << "Can't open file " << input_file << endl;
		return 1;
	}

	std::string output_file = input_file.substr(0, input_file.rfind('.')) + ".out";
	ofstream output(output_file, ios::out | ios::trunc);
	if (!output.is_open()) {
		cerr << "Can't open file " << output_file << endl;
		return 1;
	}

	read_and_solve(input, output);

	return 0;
}
