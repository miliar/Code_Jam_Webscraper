// ConsoleApplication5.cpp : Defines the entry point for the console application.
#include <iostream>
#include <conio.h>
#include <vector>
#include <fstream>
#include <string>

using namespace std;


int main() {
	int T = 0;
	long int N = 0;
	vector <string> pancakeStackVec;
	ifstream infile;
	ofstream outfile;
	string line;

	infile.open("D:/GoogleCodeJam/large.in");
	outfile.open("D:/GoogleCodeJam/PancakeLargeOut.txt");


	if (infile.is_open()) {
		bool first = true;
		while (getline(infile, line)) {
			int intVal = atoi(line.c_str());
			if (first == true) {
				T = intVal;
				first = false;
			} else {
				pancakeStackVec.push_back(line);
			}
		}
		infile.close();
	}


	for (int j = 0; j < T; j++) {
		string pancakeStack = pancakeStackVec[j];
		int len = pancakeStack.length();
		int count = 0;
		int i = 0;
		for (i = 0; i < len -1; i++) {

			if (pancakeStack[i] != pancakeStack[i + 1]) {
				count++;
			}
			
		}
		if (pancakeStack[i] == '-') {
			count++;
		}
		outfile << "Case #" << j+1 << ": " << count << endl;

	}

	infile.close();
	outfile.close();
	_getch();
}