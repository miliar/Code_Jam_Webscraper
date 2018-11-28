#include <iostream>
#include <fstream>
#include <array>
#include <vector>
#include "CGCJLib.hpp"

#define PROBLEM_LETTER "D"
#define SIZE "small"
#define VERSION_NUM "1"

using namespace std;

// [x][r][c]
// Sometimes doing it in your head is the easiest way
bool canRichardWin[4][4][4] = {
		{{ false, false, false, false }, { false, false, false, false }, { false, false, false, false }, { false, false, false, false }},
		{{ true, false, true, false }, { false, false, false, false }, { true, false, true, false }, { false, false, false, false }},
		{{ true, true, true, true }, { true, true, false, true }, { true, false, false, false }, { true, true, false, true }},
		{{ true, true, true, true }, { true, true, true, true }, { true, true, true, false }, { true, true, false, false }}
};

int main() {
	ifstream input(CGCJLib::getSourcePath() + "/" + PROBLEM_LETTER + "-" + SIZE + "-" + VERSION_NUM + ".in");
	ofstream output(CGCJLib::getSourcePath() + "/" + PROBLEM_LETTER  + "-" + SIZE + "-" + VERSION_NUM + ".out");
	output.setf(ios::fixed, ios::floatfield);
	output.precision(7);
	int testCases;
	input >> testCases;
	for(int i=0;i<testCases;i++) {
		int ominoOrder, gridWidth, gridHeight;
		input >> ominoOrder >> gridWidth >> gridHeight;
		//cout << "canRichardWin[" << ominoOrder-1 << "][" << gridWidth-1 << "][" << gridHeight-1 << "] = " << (canRichardWin[ominoOrder-1][gridWidth-1][gridHeight-1] ? "true" : "false") << endl;
		output << "Case #"  << i+1 << ": " << (canRichardWin[ominoOrder-1][gridWidth-1][gridHeight-1] ? "RICHARD" : "GABRIEL") << endl;
	}
	return 0;
}
