/**
* @file standingovation.cpp
* @author Samuel Yee
*
* Code for problem A of Google Code Jam 2015 Qualification Round, Standing Ovation.
*
*/

#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

string process(string ln);

// main only handles input/output
int main() {
	ifstream infile;
	infile.open("A-large.in");
	ofstream outfile;
	outfile.open("A-large.out");

	// get number of test cases
	int num_cases = 0;
	infile >> num_cases;

	string line;
	// discard the rest of the line
	getline(infile, line);

	for (int i = 0; i < num_cases; ++i) {
		getline(infile, line);
		string result = process(line);
		outfile << "Case #" << i+1 << ": " << result << endl;
	}

	infile.close();
	outfile.close();
}

// actual code goes here
string process(string ln) {
	stringstream ss;
	ss.str(ln);

	int smax;
	ss >> smax;

	char c;

	int current_standing = 0;
	int num_friends = 0;

	// now read smax + 1 digits
	for (int i = 0; i <= smax; ++i) {
		ss >> c;
		int n = c - '0';


		// if we already have more people standing than the shyness level, then they stand
		if (current_standing >= i) {
			current_standing += n;
		}
		// otherwise, find out how many more people we need
		else {
			num_friends += i - current_standing;
			current_standing = n + i;
		}
	}

	return to_string(num_friends);
}