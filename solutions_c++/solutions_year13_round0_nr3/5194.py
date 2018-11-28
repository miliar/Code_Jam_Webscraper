#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <sstream>
#include <math.h>
using namespace std;

// FUNCTION PROTOTYPES:
bool isPalindrome(const string& number);
bool isSquareOfPalindrome(unsigned long long int number);
/** END FUNCTION PROTOTYPES **/

// Check if this number is a palindrome:
bool isPalindrome(const string& number) {

	bool isP = true;

	unsigned long long int length = number.length();

    unsigned long long int midpoint = length / 2;
    //cout << "midpoint is: " << midpoint << endl;

	// 1 Length Strings are palindromes:
	if(length == 1) {
		isP = true;
	} else {
		// Even length number:
		for(unsigned long long int i = 0; i < midpoint; i++) {
			if(number[i] != number[length - 1 - i]) {
				isP = false;
				break;
			}
		}
	} 

	return isP;

} /** END FUNCTION isPalindrome **/

// Check if this number is a square of a palindrome:
bool isSquareOfPalindrome(unsigned long long int number) {
	
	bool isSquare = false;	

	double square = sqrt(double(number));

	unsigned long long int intSquare = int(square);

	if(square == intSquare) {
	
		// Convert intSquare into a string:
		string convertedSquare;
		stringstream out;
		out << intSquare;
		convertedSquare = out.str();

		// Check if the square is a palindrome:
		if(isPalindrome(convertedSquare)) {
			isSquare = true;
		}
	}
	

	return isSquare;
	
} /** END FUNCTION isSquareOfPalindrome **/

int main(int argc, char* argv[]) {

	if(argc != 2) {
		cout << "Usage: ./fair_and_square <filename>" << endl;
		exit(1);
	}

	
	ifstream input;
	input.open(argv[1]);

	bool firstLineRead = false;
	unsigned long long int numberOfTestCases;

	vector<string> cases;

	string nextLine;
	while(input >> nextLine) {
		
		//cout << "nextLine is " << nextLine << endl;

		if(!firstLineRead) {
			numberOfTestCases = atoi(nextLine.c_str());
			firstLineRead = true;
		} else {
			cases.push_back(nextLine);			
		}

	}
	input.close();

	ofstream output;
	output.open("results2.txt");

	unsigned long long int nextCaseData = 0;
	// Debug only:
	for(unsigned long long int i = 0; i < numberOfTestCases; i++) {
		//cout << "Case " << i+1 << ": " << cases[nextCaseData] << "," << cases[nextCaseData+1] << endl;
	
		unsigned long long int lowerBoundary = atoi(cases[nextCaseData].c_str());
		unsigned long long int upperBoundary = atoi(cases[nextCaseData+1].c_str());

		// DEBUG ONLY
		//cout << "lowerBoundary: " << lowerBoundary << " upperBoundary: " << upperBoundary << endl;

		unsigned long long int numberOfFAS = 0;

		for(unsigned long long int j = lowerBoundary; j <= upperBoundary; j++) {
			
			// Convert i to a string:
			string nextNum;
			stringstream out;
			out << j;
			nextNum = out.str();
			//cout << "nextNum is: " << nextNum << endl;

			// Check if the i is a palindrome:
			if(isPalindrome(nextNum) && isSquareOfPalindrome(j)) {
				//cout << nextNum << " is a fair and square number! " << endl;
				numberOfFAS++;
			}
			
		}

		output << "Case #" << i + 1 << ": " << numberOfFAS << endl;

		nextCaseData += 2;
	}

	output.close();

	return 0;

}
