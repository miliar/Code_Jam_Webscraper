/*
 * Main.cpp
 *
 *  Created on: 11.04.2015
 *      Author: David
 */

#include <iostream>
#include <fstream>

using namespace std;

int friends(int maxShyness, int* numberPeople) {
	int result = 0;
	int sum = 0;
	for (int i = 0; i <= maxShyness; i++) {
		if (result < i - sum)
			result = i - sum;
		sum += numberPeople[i];
	}
	return result;
}

int main() {
	ifstream infile("A_large.txt");
	ofstream outfile("output.txt");
	int tests = 0;
	infile >> tests;
	for (int i = 0; i < tests; i++) {
		int maxShyness = 0;
		infile >> maxShyness;
		int* numberPeople = new int[maxShyness + 1];
		for (int j = 0; j <= maxShyness; j++) {
			char in = 'a';
			infile >> in;
			numberPeople[j] = in - '0';
		}
		outfile << "Case #" << (i + 1) << ": "
				<< friends(maxShyness, numberPeople) << endl;
	}
	return 0;
}

