// Compiler verion : GCC 5.2.1
// Language: C++ 14

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>

using namespace std;
const int MAXSTACK = 100;
char pancakeStack[MAXSTACK];

void flipPancakesallofthem(int offset, char side) {
	for (int i = 0; i < offset; i++) {
		pancakeStack[i] = side;
	}
}

int maneuver(int stackSize) {
	if (stackSize == 1) {
		if (pancakeStack[0] == '+')
			return 0;
		else if (pancakeStack[0] == '-')
			return 1;
		else
			return -1; // error case
	}

	int flipCounts = 0;

	for (int i = 1; i < stackSize; i++) {
		if (pancakeStack[i-1] != pancakeStack[i]) {
			flipCounts++;
			flipPancakesallofthem(i, pancakeStack[i]);
		}
	}
	if (pancakeStack[stackSize-1] == '-')
		flipCounts++;

	return flipCounts;
}

int main()
{
	fstream fInput("B-large.in");
	string line = "";

	while (getline(fInput, line)) {
		// the number of cases
		int cases = stoi(line);
//		cout << cases << endl;

		for (int i = 0; i < cases; i++) {
			getline(fInput, line); //get a credit
			strcpy(pancakeStack, line.c_str());
			int size = strlen(pancakeStack);
//			cout << "pancake: " << pancakeStack << " size: " << size << endl;
			cout <<"Case #"<< i + 1 <<": " << maneuver(size) << endl;
		}

	}

	return 0;
}
