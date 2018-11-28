#include<iostream>
#include<fstream>
#include<string>
using namespace std;

string lastword(string s) {
	int n = s.length();
	string result = "";
	if (n == 0) return result;

	result += s[0];
	for (int i = 1; i < n; i++) {
		if (s[i] < result[0]) {
			result += s[i];
		}
		else
		{
			result = s[i] + result;
		}
	}

	return result;
}

void main() {
	fstream infile, outfile;
	int testnum;
	string s;
	infile.open("A-large.in", ios::in);
	outfile.open("output.dat", ios::out);
	infile >> testnum;
	getline(infile, s);
	for (int i = 1; i <= testnum; i++) {
		getline(infile, s);
		outfile << "Case #" << i << ": " << lastword(s) << '\n';
	}
}