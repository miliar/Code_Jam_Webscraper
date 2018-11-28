#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int calculate(string stack) {
	int count = 0;
	int length = stack.size();

	if (stack[length - 1] == '-') {
		count++;
	}

	if (length == 1) {
		return count;
	}

	char pre = stack[length - 1];

	for (int i = length - 2; i >= 0; i--) {
		if (stack[i] != pre) {
			count++;
			pre = stack[i];
		}
	}

	return count;
}


int main(void) {

	ifstream inputFile("B-large.in");
	int numOfCases;
	inputFile >> numOfCases;
	string *stack = new string[numOfCases];
	for (int i = 0; i < numOfCases; i++) {
		inputFile >> stack[i];
	}
	inputFile.close();

	ofstream outputFile("B-large-output.txt");
	for (int i = 0; i < numOfCases; i++) {
		outputFile << "Case #" << i + 1 << ": " << calculate(stack[i]) << endl;
	}
	outputFile.close();
	delete[] stack;

	return 0;
}

