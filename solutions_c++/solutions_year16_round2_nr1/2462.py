// 2015q3.cpp : Defines the entry point for the console application.;
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <functional>
//#include <boost/math/special_functions/sign.hpp>


using namespace std;

string problem(std::ifstream& fin, std::ofstream& ferr) {

	string S;
	char c;
	stringstream r;


	int d[10];
	int l['Z'+1];


	fin >> S;
	//"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
	
	// _ZERO T_WO SI_X EI_GHT  FO_UR _FIVE SE_VEN 

	// "ZERO",  "TWO",
	// "SIX", "SEVEN",
	// "FOUR", "FIVE", 
	// "EIGHT", 
	// 	"THREE", 	"ONE",	"NINE"


	memset(d, 0, sizeof(d));
	memset(l, 0, sizeof(l));

	for (int i = 0; i < S.length(); ++i ) {
		l[S[i]]++;
	}

// ZERO 
	d[0] = l['Z'];
	
	l['O'] -= l['Z'];
	l['R'] -= l['Z'];
	l['E'] -= l['Z'];
	l['Z'] -= l['Z'];

	d[2] = l['W'];

	l['O'] -= l['W'];
	l['T'] -= l['W'];
	l['W'] -= l['W'];
	
	d[6] = l['X'];

	l['S'] -= l['X'];
	l['I'] -= l['X'];
	l['X'] -= l['X'];

	d[7] = l['S'];

	l['N'] -= l['S'];
	l['E'] -= l['S'];
	l['V'] -= l['S'];
	l['E'] -= l['S'];
	l['S'] -= l['S'];

	d[4] = l['U'];

	l['F'] -= l['U'];
	l['O'] -= l['U'];
	l['R'] -= l['U'];
	l['U'] -= l['U'];
	
	d[5] = l['F'];

	l['E'] -= l['F'];
	l['V'] -= l['F'];
	l['I'] -= l['F'];
	l['F'] -= l['F'];

	d[8] = l['G'];

	l['E'] -= l['G'];
	l['I'] -= l['G'];
	l['H'] -= l['G'];
	l['T'] -= l['G'];
	l['G'] -= l['G'];

	d[3] = l['H'];

	l['T'] -= d[3];
	l['H'] -= d[3];
	l['R'] -= d[3];
	l['E'] -= d[3];
	l['E'] -= d[3];

	d[1] = l['O'];

	l['O'] -= d[1] ;
	l['N'] -= d[1] ;
	l['E'] -= d[1] ;

	d[9] = l['I'];

	l['N'] -= d[9];
	l['I'] -= d[9];
	l['N'] -= d[9];
	l['E'] -= d[9];

	__nop;

	for (int i = 0; i < 10;  ++i) {
		r << std::string(d[i], i + '0');
	}


	return r.str();
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
