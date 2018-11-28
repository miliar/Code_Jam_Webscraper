/*
 * PracticeProblem1.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: Tala
 */

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include<stack>
using namespace std;

int main () {

	ifstream inFile;
	ofstream outFile;

	inFile.open("A-large.in");
	outFile.open("outputALarge.txt");

	int T = 0;
	inFile>>T;

	int N = 0;

	for (int i=1; i<= T; i++) {
		bool A[10] = { false, false, false, false, false, false, false, false, false, false};
		//counter to check if we've seen all 10 digits
		int counter = 0;
		inFile>>N;
		int multiplier = 1;

		if (N == 0) {
			outFile<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
			continue;
		}

		while (counter<10) {
		int multipliedValue = multiplier*N;
		int digits = log10((float)multipliedValue) + 1;

		for (int j =  1; j<= digits; j++) {
				int val = multipliedValue%10;
				if (!A[val]) {
					A[val] = true;
					counter++;
					if (counter == 10) {
						outFile<<"Case #"<<i<<": "<<multiplier*N<<endl;
						break;
					}
				}
				multipliedValue = multipliedValue/10;
			}
		multiplier++;
		}
	}
	inFile.close();
	outFile.close();
	return 0;
}
