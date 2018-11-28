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
/*bool differentBases(unsigned long int x, int length);
bool prime(unsigned long int x);
unsigned long int increment(unsigned long int x);*/

void recursiveSolver(string s, size_t &max, size_t cur);
string flip(string s,size_t num);


int main()
{/*
	cout << increment(101);
	std::vector<unsigned long int> coinjams[33];
	unsigned long int jams = 1;
	for (unsigned long int x = 1; x < 17; x++) {
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


	string line;

	int num;
	infile >> num;
	getline(infile, line);
	int input = 0;
	for (int x = 1; x <= num; x++) {
		outfile << "Case #" << x << ": ";
		getline(infile, line);
		cout << line << "\t";
		char last = line[0];
		for (size_t x = 1; x < line.length(); x++) {
			if (line[x] == last) {
				line.erase(x, 1);
				x--;
			}
			last = line[x];
		}
		size_t max = line.length();
		if (line.length() % 2 == 1 && line[0] == '+') {
			max--;
		}
		if (line.length() % 2 == 0 && line[0] == '-') {
			max--;
		}
		outfile << max << endl;
		cout << max << endl;
	}





	char c;
	cin >> c;


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

void recursiveSolver(string s, size_t& max, size_t cur) {
	char last = s[0];
	for (size_t x = 1; x < s.length(); x++) {
		if (s[x] == last) {
			s.erase(x, 1);
			x--;
		}
		last = s[x];
	}
	if (max <= cur) {
		return;
	}
	bool solved = true;
	for (size_t x = 0; x < s.length(); x++) {
		if (s[x] == '-') {
			solved = false;
		}
	}
	if (solved)
	{
		max = cur;
		return;
	}
	for (size_t x = 1; x <= s.length(); x++) {
		string temp = flip(s, x);
		recursiveSolver(temp, max, (cur + 1));
	}
	
}

string flip(string s, size_t num) {
	std::stack<char> revStack;
	for (size_t x = 0; x < num; x++) {
		char y = s[0];
		s = s.substr(1);
		if (y == '+') {
			revStack.push('-');
		}
		else revStack.push('+');
	}
	string w =  "";
	while (!revStack.empty()) {
		w += revStack.top();
		revStack.pop();
	}
	s = w + s;
	return s;
}
/*
bool prime(unsigned long int x) {
	bool isprime = true;
	if (x == 2) {
		return false;
	}
	for (int i = 3; i <= sqrt(x); i += 2)
	{
		if ((x % i) == 0)
		{
			return false;
			
		}
	}

	return true;
}

bool differentBases(unsigned long int x, int length) {
	unsigned long int base10 = x;
	unsigned long int base9 = 0;
	unsigned long int base8 = 0;
	unsigned long int base7 = 0;
	unsigned long int base6 = 0;
	unsigned long int base5 = 0;
	unsigned long int base4 = 0;
	unsigned long int base3 = 0;
	unsigned long int base2 = 0;
	for (int y = 0; y < length; y++) {
		base9 += (x % 10)*pow(9, y);
		base8 += (x % 10)*pow(8, y);
		base7 += (x % 10)*pow(7, y);
		base6 += (x % 10)*pow(6, y);
		base5 += (x % 10)*pow(5, y);
		base4 += (x % 10)*pow(4, y);
		base3 += (x % 10)*pow(3, y);
		base2 += (x % 10)*pow(2, y);
	}
	return (!prime(base10) && !prime(base9) && !prime(base8) && !prime(base7) && !prime(base6) && !prime(base5) && !prime(base4) && !prime(base3) && !prime(base2));
}

unsigned long int increment(unsigned long int x) {
	unsigned long int checker = 10;
	while (true) {
		if (x%checker == 0)
		{
			return x + (checker / 10);
		}
		else {
			return 10 * increment(x / 10);
		}
		checker *= 10;
	}
}*/
