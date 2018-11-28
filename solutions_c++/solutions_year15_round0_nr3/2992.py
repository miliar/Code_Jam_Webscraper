/**
* @file dijkstra.cpp
* @author Samuel Yee
*
* Code for problem C of Google Code Jam 2015 Qualification Round, Dijkstra.
*
*/

#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

#define LINES_PER_CASE 2

struct quart {
	unsigned int q : 2;  // 0 = 1, 1 = i, 2 = j, 3 = k
	int sign : 2;
};

// simple memoization
quart* memo;

string process_case(vector<string> lines);
quart multiply(quart a, quart b);
quart get_quart(char c);
bool search_string(string str, int q);

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

// actual code goes here
string process_case(vector<string> lines) {
	stringstream ss;
	ss.str(lines[0]);

	int l, x;
	ss >> l >> x;

	string str;
	for (int i = 0; i < x; ++i) {
		str.append(lines[1]);
	}

	// Deal with the easy cases first
	if (str.length() < 3)
		return "NO";
	else if (str.length() == 3) {
		if (str == "ijk")
			return "YES";
		else
			return "NO";
	}

	// store multiplied values
	memo = new quart[str.length()];

	int count = 0;
	quart current;
	current.q = 0;
	current.sign = 1;

	for (string::reverse_iterator rit = str.rbegin(); rit != str.rend(); ++rit) {
		current = multiply(get_quart(*rit), current);
		memo[count] = current;
		++count;
	}
	
	bool result = search_string(str, 1);

	delete[] memo;

	return result ? "YES" : "NO";
}

// multiply two quarternions
static int mult_quart[4][4] = {
	{0, 1, 2, 3},
	{1, 0, 3, 2},
	{2, 3, 0, 1},
	{3, 2, 1, 0}
};
static int mult_signs[4][4] = {
	{1, 1, 1, 1},
	{1, -1, 1, -1},
	{1, -1, -1, 1},
	{1, 1, -1, -1}
};
quart multiply(quart a, quart b) {
	quart r;
	r.q = mult_quart[a.q][b.q];
	r.sign = a.sign * b.sign * mult_signs[a.q][b.q];

	return r;
}

quart get_quart(char c) {
	quart r;
	r.sign = 1;
	switch (c) {
		case 'i':
			r.q = 1;
			break;
		case 'j':
			r.q = 2;
			break;
		case 'k':
			r.q = 3;
			break;
	}

	return r;
}

// search the string
bool search_string(string str, int q) {
	int len = str.length();
	if (len == 0)
		return false;

	quart current;
	current.q = 0;
	current.sign = 1;

	// deal with the base case: if we are looking for k, multiply till the end
	if (q == 3) {
		if (memo[len-1].q == 3 && memo[len-1].sign == 1)
			return true;
		else
			return false;
	}

	// otherwise, consume until we get the result we want, then search for the next one.
	for (int i = 0; i < len; ++i) {
		current = multiply(current, get_quart(str[i]));

		if (current.q == q && current.sign == 1) {
			if (search_string(str.substr(i+1), q+1))
				return true;
			// if we are unsuccessful, keep trying
		}
	}

	// if we get here, it means we ran out of characters, so return false
	return false;
}