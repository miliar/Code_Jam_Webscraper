/**
* @file mushroom.cpp
* @author Samuel Yee
*
* Code for problem A of Google Code Jam Problem 1A, Mushroom Monster.
*
*/

#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

#define CLEAR(ss) \
	(ss).str(string()); \
	(ss).clear();

#define LINES_PER_CASE 2

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

// end template

string process_case(vector<string> lines)
{
	stringstream ss;
	ss.str(lines[0]);
	int n;
	ss >> n;

	int m[n];
	CLEAR(ss);
	ss.str(lines[1]);
	for (int i = 0; i < n; ++i)
	{
		ss >> m[i];
	}

	// compute using the two computation methods
	int first_total = 0;
	int second_max_decrease = 0;

	for (int i = 1; i < n; ++i)
	{
		int diff = m[i-1] - m[i];
		first_total += (diff > 0) ? diff : 0;
		second_max_decrease = (diff > second_max_decrease) ? diff : second_max_decrease;
	}

	// run through a second time to find the second_total
	int second_total = 0;
	for (int i = 1; i < n; ++i)
	{
		second_total += (m[i-1] > second_max_decrease) ? second_max_decrease : m[i-1];
	}

	CLEAR(ss);
	ss << first_total << " " << second_total;

	return ss.str();
}