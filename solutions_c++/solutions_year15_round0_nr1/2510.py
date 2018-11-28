/*
 * standingovation.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: Jason
 */
#include <iostream>
#include <fstream>

using namespace std;

int main() {
	int c;
	ifstream ifile;
	ofstream ofile;
	ifile.open("input.txt");
	ofile.open("output.txt");
	ifile >> c;
	for (int i = 0; i < c; i++) {
		int m, t = 0, a = 0;
		string s;
		ifile >> m >> s;
		for (int j = 0; j <= m; j++) {
			if (t < j) {
				a += (j-t);
				t = j;
			}
			t += (s[j]-'0');
		}
		ofile << "Case #" << i+1 << ": " << a << endl;
	}
}
