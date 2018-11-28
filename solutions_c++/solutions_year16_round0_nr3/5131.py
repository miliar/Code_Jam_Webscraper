/*
 * COIN JAM
 * Google Code Jam 2016 - Qualification Round (Problem C)
 * 	by Yago González
 * 
 * */
 
#include <iostream>
#include <fstream>
#include <math.h>
#include <string>

using namespace std;

/**
 * toDecimal - Transforms an array of 1's and 0's in a specific base to
 * 			   a decimal number
 * 
 * @param bool[] in		Array with ones and zeros to convert
 * 						(max length: 64)
 * @param short	base	Base (or radix) of the numeral system provided
 * 						in the in array
 * 
 * @returns The decimal value of the inputed array
 */
long toDecimal(bool in[], unsigned short base, unsigned short size) {
	long dec = 0;
	
	for(short i = size - 1; i >= 0 ; i--) {
		dec += in[i] * pow(base, size - (i + 1));
	}
	
	return dec;
}

/**
 * decToBin - Converts a number from decimal to binary
 * 
 * @param long num	Number to pass to binary
 * 
 * @returns String with the binary equivalent of num
 */
string decToBin(long num) {
	string binary;
    
	for(int i = 0; num > 0; i++) {
		binary.insert(0, (num % 2) ? "1" : "0");
		num /= 2;
	}
    
    return binary;
}

int main() {	
	// Open the input/output files
	ifstream input ("in.txt");
	ofstream output ("out.txt");

	short coinSize = 0, reqAmount = 0;
	
	// Identify size and amount of jamcoins from the input
	input >> coinSize;
	input >> coinSize;	// Twice on purpose (first one is T)
	input >> reqAmount;

	bool* jamcoin = new bool[coinSize]();
	
	jamcoin[0] = 1;
	jamcoin[coinSize - 1] = 1;

	short count = 0;
	bool valid = true;

	output << "Case #1:\n";

	while(count < reqAmount) {
		short b = 2;
		valid = true;
		long factors[9] = { 0 };
		
		// Make sure it isn't prime
		long transBase = 0;
		while(valid && b <= 10) {
			transBase = toDecimal(jamcoin, b, coinSize);
			valid = false;
			
			if(!(transBase % 2)) {	// Number is pair
					factors[b - 2] = 2;
					valid = true;
			} else {	// Look for other divisor
				for(long i = 3; i < sqrt(transBase); i += 2) {
					if(!(transBase % i)) {	// Found a divisor
						factors[b - 2] = i;
						valid = true;
					}
				}
			}

			b++;
		}
		
		// Check if the result was a valid jamcoin
		if(valid && b > 10) {
			for(short i = 0; i < coinSize; i++) {
				output << jamcoin[i];
			}
			for(short i = 0; i < 9; i++) {
				output << " " << factors[i];
			}
			output << "\n";
			count++;
		}
		
		// Get next coin to test
		string coin = decToBin(toDecimal(jamcoin, 2, coinSize) + 2);
		// Decimal to binary conversion
		for(short i = 0; i < coinSize; i++) {
			if(coin.at(i) == '1') {
				jamcoin[i] = 1;
			} else {
				jamcoin[i] = 0;
			}
		}
	}

	delete[] jamcoin;

	input.close();
	output.close();

	return 0;
}
