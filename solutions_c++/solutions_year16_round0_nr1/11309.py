// again.cpp : Defines the entry point for the console application.
// 0409codejam.cpp : Defines the entry point for the console application.

#include "stdafx.h"
#include <fstream>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout

using namespace std;

void main() {
	int t;
	int n[200];
	int fallasleep;
	int falldigit;
	int number;

	//int bitmask  =  0; //
	int digit[10] = { 0, };
	int end = 0;
	int fi;

	ifstream inFile("A-small-attempt4.in");
	ofstream outFile("A-small-attempt4.out");

	while (!inFile.eof()) {
		inFile >> t;  // read t. cin knows that t is an int, so it reads it as such.
		for (int i = 0; i < t; i++) {
			inFile >> n[i];
		}
	}
	inFile.close();

	for (int i = 0; i < t; i++) {
		//count until the all the digits are shown
		//split and check to the digit. 
		if (n[i] == 0) {  //또 언제 불면증이징..?!
			outFile << "Case #" << i + 1 << ": INSOMNIA\n";
		}
		else {
			for (int j = 1; end < 10; j++) {
				//interate through 
				fallasleep = j * n[i];
				//seperate and check the digit
				//and operation of fallasllep (by digits)
				number = fallasleep;
				while (number > 0) {
					falldigit = number % 10;
					number = number / 10;
					digit[falldigit] = 1;
				}

				//sequence for escape
				end = 0;
				for (int k = 0; k < 10; k++) {
					end += digit[k];
				}
			}
			outFile << "Case #" << i + 1 << ": " << fallasleep << "\n";
			//re-initialization
			end = 0;
			for (int k = 0; k < 10; k++) {
				digit[k] = 0;
			}
		}
	}
	outFile.close();
}

