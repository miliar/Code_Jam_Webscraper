#include <iostream>
#include <fstream>

using namespace std;

int calculate(int start) {
	int collect[10] = { 0 };
	int mult = 0;
	bool hasSleep = false;
	int num;
	
	while (hasSleep!=true) {
		mult++;
		num = start * mult;
		int tmp = num;
		while (tmp != 0) {
			int digit = tmp % 10;
			if (collect[digit] == 0) {
				collect[digit]++;
			}
			tmp /= 10;
		}

		hasSleep = true;

		for (int i = 0; i < 10; i++) {
			if (collect[i] == 0) {
				hasSleep = false;
			}
		}
	}

	return num;
}

int main(void) {

	ifstream inputFile("A-large.in");
	int numOfCases;
	inputFile >> numOfCases;
	int *number = new int[numOfCases];
	for (int i = 0; i < numOfCases; i++) {
		inputFile >> number[i];
	}
	inputFile.close();

	ofstream outputFile("A_large_output.txt");
	for (int i = 0; i < numOfCases; i++) {
		outputFile << "Case #" << i + 1 << ": ";
		if (number[i] == 0) {
			outputFile << "INSOMNIA" << endl;
		}
		else {
			outputFile << calculate(number[i]) << endl;
		}
	}
	outputFile.close();
	delete[] number;

	return 0;
}

