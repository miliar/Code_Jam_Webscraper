// 2015q3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <functional>
//#include <boost/math/special_functions/sign.hpp>


using namespace std;

string problem(std::ifstream& fin, std::ofstream& ferr) {

	string P;
	int c = 0;

	bool state = false;

	fin >> P;



		/*
		   ++++ non
		   --- 1
		   -+ 1 (1)
		   +- 2 (1,2)
		   -+-	3   1,2,3 or 3,1,2
		   +-+ 2
		   -+-+ 3
		   +-+- 4
		   5
		   -
		   -+
		   +-
		   +++
		   --+-

		   */
	cerr << "first " << P[0] << "X" << endl;

	if (P[0] == '-') {
		c = 1; state = true;
	}

	for (int i = 1; i < P.length(); i++) {
		if (!state) {
			if (P[i] == '-') {
				c += 2;
				state = ! state;
			}
		}else{
			if (P[i] == '+') {
				state = ! state;
			}
		}

	}
	return to_string(c);

}

int main()
{
	int T;
	string filename;

	string result;

	cout << "Enter the file prefix" << endl;
	cin >> filename;

	std::ifstream f_in(filename + ".in");
	std::ofstream f_out(filename + ".out");
	std::ofstream f_err(filename + ".err");


	if (!f_in) { cerr << "Failed to open input file." << endl; }
	if (!f_out) { cerr << "Failed to open output file." << endl; }
	if (!f_out) { cerr << "Failed to open debug file." << endl; }

	if (f_in && f_out) {

		f_in >> T;

		for (int i = 1; i <= T; i++) {
			result = problem(f_in, f_err);
			cerr << "Case #" << i << ": " << result << endl;
			f_out << "Case #" << i << ": " << result << endl;
		}

		f_in.close();
		f_out.close();
	}
}
