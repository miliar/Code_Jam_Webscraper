// 2015q3.cpp : Defines the entry point for the console application.;
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

	long long B, R;
	string s, r = "0123456789";
	int c = 0;

	fin >> B;

	if (B == 0) 	return "INSOMNIA";

	// is 100 reasonible -- large numbers?
	for (int i = 1; i <= 1000; ++i) {
		R = i*B;
		s = to_string(R);

		while (R) {
			if (r[R % 10] != 'y') {
				r[R % 10] = 'y';
				c++;
			}

			R /= 10;
		}
		if (c == 10) {
			return to_string(i*B);
		}
	}

	return "INSOMNIA";
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
