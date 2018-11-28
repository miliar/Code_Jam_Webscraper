//============================================================================
// Name        : gcj2015.cpp
// Author      : Ravi
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <iostream>
#include <fstream>
#include <iostream>
#include <cstdlib>
using namespace std;

void proba(char *inpfile) {
	ifstream inp(inpfile);
	ofstream out("output.txt");

	int tc;
	inp >> tc;
	int tcout = 0;
	while(tc) {
		tc--;
		tcout++;
		int len, i = 1;
		inp >> len;
		len++;
		int extras = 0, currova = 0;
		string count;
		inp >> count;
		int temp = count[0] - '0';
		currova += temp;
		while (i < len) {
			if (('0' != count[i]) && currova < i) {
				int temp = i - currova;
				extras += temp;
				currova += temp;
				temp = count[i] - '0';
				currova += temp;
			} else {
				int temp = count[i] - '0';
				currova += temp;
			}
			i++;
		}

		out << "Case #" << tcout << ": " << extras << endl;
	}
}

int main() {
	#define INP "/home/ravi/workspace/gcj2015/Debug/A-large.in"
	proba(INP);
	return 0;
}
