// TestAppFeb2016.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;

int freq[26];
void calculateFrequencies(string &str) {
	for (int i = 0; i < 26; i++) {
		freq[i] = 0;
	}
	int len = str.length();
	for (int i = 0; i < len; i++) {
		freq[str[i] - 'A']++;
	}
}

void eliminateZeroes(ostringstream &outstr) {
	int numZeros = freq['Z' - 'A'];
	for (int i = 0; i < numZeros; i++) {
		outstr << '0';
	}
	freq['Z' - 'A'] -= numZeros;
	freq['E' - 'A'] -= numZeros;
	freq['R' - 'A'] -= numZeros;
	freq['O' - 'A'] -= numZeros;
}

void eliminateTwos(ostringstream &outstr) {
	int numTwos = freq['W' - 'A'];
	for (int i = 0; i < numTwos; i++) {
		outstr << '2';
	}
	freq['T' - 'A'] -= numTwos;
	freq['W' - 'A'] -= numTwos;
	freq['O' - 'A'] -= numTwos;
}

void eliminateSixes(ostringstream &outstr) {
	int numSixes = freq['X' - 'A'];
	for (int i = 0; i < numSixes; i++) {
		outstr << '6';
	}
	freq['S' - 'A'] -= numSixes;
	freq['I' - 'A'] -= numSixes;
	freq['X' - 'A'] -= numSixes;
}

void eliminiateEights(ostringstream &outstr) {
	int numEights = freq['G' - 'A'];
	for (int i = 0; i < numEights; i++) {
		outstr << '8';
	}
	freq['E' - 'A'] -= numEights;
	freq['I' - 'A'] -= numEights;
	freq['G' - 'A'] -= numEights;
	freq['H' - 'A'] -= numEights;
	freq['T' - 'A'] -= numEights;
}

void eliminateThrees(ostringstream & outstr) {
	int numThrees = freq['T' - 'A'];
	for (int i = 0; i < numThrees; i++) {
		outstr << '3';
	}
	freq['T' - 'A'] -= numThrees;
	freq['H' - 'A'] -= numThrees;
	freq['R' - 'A'] -= numThrees;
	freq['E' - 'A'] -= numThrees;	
	freq['E' - 'A'] -= numThrees;
}

void eliminiateFours(ostringstream &outstr) {
	int numThrees = freq['R' - 'A'];
	for (int i = 0; i < numThrees; i++) {
		outstr << '4';
	}
	freq['F' - 'A'] -= numThrees;
	freq['O' - 'A'] -= numThrees;
	freq['U' - 'A'] -= numThrees;
	freq['R' - 'A'] -= numThrees;
}

void eliminiateFives(ostringstream &outstr) {
	int numThrees = freq['F' - 'A'];
	for (int i = 0; i < numThrees; i++) {
		outstr << '5';
	}
	freq['F' - 'A'] -= numThrees;
	freq['I' - 'A'] -= numThrees;
	freq['V' - 'A'] -= numThrees;
	freq['E' - 'A'] -= numThrees;
}

void eliminiateSevens(ostringstream &outstr) {
	int numThrees = freq['S' - 'A'];
	for (int i = 0; i < numThrees; i++) {
		outstr << '7';
	}
	freq['S' - 'A'] -= numThrees;
	freq['E' - 'A'] -= numThrees;
	freq['V' - 'A'] -= numThrees;
	freq['E' - 'A'] -= numThrees;
	freq['N' - 'A'] -= numThrees;
}

void eliminiateOnes(ostringstream &outstr) {
	int numThrees = freq['O' - 'A'];
	for (int i = 0; i < numThrees; i++) {
		outstr << '1';
	}
	freq['O' - 'A'] -= numThrees;
	freq['N' - 'A'] -= numThrees;
	freq['E' - 'A'] -= numThrees;
}

void eliminiateNines(ostringstream & outstr) {
	int numThrees = freq['I' - 'A'];
	for (int i = 0; i < numThrees; i++) {
		outstr << '9';
	}
	freq['N' - 'A'] -= numThrees;
	freq['I' - 'A'] -= numThrees;
	freq['N' - 'A'] -= numThrees;
	freq['E' - 'A'] -= numThrees;
}
void eliminateFrequencies(string &result) {
	ostringstream outstr;
	outstr.str("");
	eliminateZeroes(outstr);
	eliminateTwos(outstr);
	eliminateSixes(outstr);
	eliminiateEights(outstr);
	eliminateThrees(outstr);
	eliminiateFours(outstr);
	eliminiateFives(outstr);
	eliminiateSevens(outstr);
	eliminiateOnes(outstr);
	eliminiateNines(outstr);
	result = outstr.str();
	sort(result.begin(), result.end());
}
int main()
{
	std::ifstream infile("C:\\Users\\Reyansh\\Downloads\\A-large-1.in");
	std::ofstream outfile("C:\\Users\\Reyansh\\Downloads\\A-large-1.out");
	int nInputs;
	infile >> nInputs;
	std::string sequence;
	for (int i = 0; i < nInputs; i++) {
		infile >> sequence;
		calculateFrequencies(sequence);
		string result;
		eliminateFrequencies(result);
		outfile << "Case #" << i + 1 << ": " << result << endl;
	}
	outfile.flush();
	infile.close();
	outfile.close();
    return 0;
}

