#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main() {
	ifstream input;
	input.open("in.txt", ios::in);

	int testCases = 0;
	input >> testCases;

	for (int c = 1; c <= testCases; c++) {
		string s;
		input >> s;
		char prev = '+';
		int moves = 0;
		int len = s.length();
		for (int i = 1; i <= len; i++) {
			if (s.at(len - i) != prev) {
				prev = s.at(len - i);
				moves++;
			}
		}
		cout << "Case #" << c << ": " << moves << endl;
	}
}
