#include <iostream>
#include <string>
#include <fstream>
#include <stdio.h>
#include <set>

using namespace std;

void parse();
string solve(string str);

int main() {
	parse();
	getchar(); 
}

void parse() {
	string file = "Input2.txt";
	ifstream in(file);
	ofstream outputfile;
	outputfile.open("Output2.txt");

	int totalCases;
	in >> totalCases;
	for (int caseNum = 1; caseNum <= totalCases; caseNum++) {
		string input;
		in >> input;
		string res = solve(input);
		res = "Case #" + to_string(caseNum) + ": " + res + "\n";
		cout << res;
		outputfile << res;
	}
	outputfile.close();
}

string solve(string str) {
	int changes = 1;
	char pattern = str[0];
	int n = str.length();
	for (int i = 0; i < n; i++) {
		char candidate = str[i];
		if (candidate != pattern) {
			changes++;
			pattern = candidate;
		}
	}
	if (str[n - 1] == '+') {
		return to_string(changes - 1);
	}
	else {
		return to_string(changes);
	}
}