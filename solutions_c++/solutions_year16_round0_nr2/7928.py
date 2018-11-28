#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int solve(string s) {

	int n = 0;

	bool state = false;

	char prevch, ch = s.at(s.length() - 1);

	if (ch == '-')
		n++;

	for (int i = 2; i <= s.length(); i++) {
		prevch = ch;
		ch = s.at(s.length() - i);
		
		if (ch != prevch)
			n++;
	}

	return n;
}

int main() {

	int t;
	string s;

	fstream infile;
	infile.open("B-large.in", ios_base::in | ios_base::app);

	fstream outfile;
	outfile.open("out.out", ios_base::out | ios_base::app);

	infile >> t;

	for (int i = 1; i <= t; i++) {
		infile >> s;
		outfile << "Case #" << i << ": " << solve(s) << endl;
	}

	return 0;
}