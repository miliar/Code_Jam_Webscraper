#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <windows.h>
#include <iomanip>

using namespace std;

void processCase(ifstream &infile, ofstream &outfile, int number);

int main() {
	ifstream infile;
	ofstream outfile;
	string filename = "B-large.in";
	string filename1 = "A-small-practice.out";
	infile.open(filename.c_str());
	outfile.open(filename1.c_str());
	int cases;
	infile >> cases;
	for (int i = 1; i <= cases; i++) {
		processCase(infile, outfile, i);
	}
	return 0;
}

void processCase(ifstream &infile, ofstream &outfile, int number) {
	double C, F, X;
	double speed = 2.0;
	double timeElapsed = 0.0;
	infile >> C >> F >> X;
	if (C >= X) {
		timeElapsed = X / speed;
	} else {
		while (true) {
			timeElapsed += C / speed;
			if ((X - C) / speed <= X / (speed + F)) {
				timeElapsed += (X - C) / speed;
				break;
			} else {
				speed += F;
			}
		}
	}
	outfile << "Case #" << number << ": " << fixed << setprecision(7) << timeElapsed << endl;
}