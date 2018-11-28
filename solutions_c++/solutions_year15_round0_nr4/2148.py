/**
* @file omino.cpp
* @author Samuel Yee
*
* Code for problem D of Google Code Jam 2015 Qualification Round, Ominous Omino.
*
*/

#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

#define LINES_PER_CASE 1

string process_case(vector<string> lines);

// main only handles input/output
int main(int argc, char* argv[]) {
	if (argc != 2) {
		cout << "Usage: " << argv[0] << " inputfile" << endl;
		return -1;
	}

	string inputfilename(argv[1]);

	ifstream infile;
	infile.open(inputfilename);
	if (!infile) {
		cout << "Could not open " << argv[1] << endl;
		return -1;
	}

	size_t pos = inputfilename.find(".");
	string outputfilename = inputfilename.substr(0, pos);
	outputfilename.append(".out");

	ofstream outfile;
	outfile.open(outputfilename);

	// get number of test cases
	int num_cases = 0;
	infile >> num_cases;

	string line;

	// discard the rest of the line
	getline(infile, line);

	for (int i = 0; i < num_cases; ++i) {
		cout << "Running case " << i+1 << endl;
		vector<string> input;

		for (int j = 0; j < LINES_PER_CASE; ++j) {
			getline(infile, line);
			input.push_back(line);
		}

		string result = process_case(input);
		outfile << "Case #" << i+1 << ": " << result << endl;
	}

	infile.close();
	outfile.close();
}

string process_case(vector<string> lines) {
	stringstream ss;
	ss.str(lines[0]);

	int x, r, c;
	ss >> x >> r >> c;

	// deal with easy cases
	if (x == 1)
		return "GABRIEL";
	else if (x == 2) 
		return (r * c % 2 == 0) ? "GABRIEL" : "RICHARD";
	else if (x == 3)
		return (r * c % 3 == 0 && r >= 2 && c >= 2) ? "GABRIEL" : "RICHARD";
	else if (x == 4) {
		if (r * c == 16 || r * c == 12)
			return "GABRIEL";
		else
			return "RICHARD";
	}
	else if (x >= 7)
		return "RICHARD";

	return "RICHARD";
}