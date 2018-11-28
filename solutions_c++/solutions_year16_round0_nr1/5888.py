// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>

using namespace std;

int function(int input);
int checkIfSeen(int number, int check);
int numDigits(int x);


int main() {
	ofstream fout("output.txt");
	ifstream file;
	file.open("A-large.in", ios::in);    // open file

	int T;  // number of test cases
	file >> T;
	
	
	for (int i = 1; i <= T; i++)
	{
		int input;
		file >> input;
		
		int output = function(input);

		if (output < 0)
			fout << "Case #" << i << ": " << "INSOMNIA" << endl;
		else
			fout << "Case #" << i << ": " << output << endl;
	}
	

	/*
	fout << 1000000 << endl;
	for (int i = 1; i <= 1000000; i++)
	{
		fout << i << endl;
	}
	*/

	fout.close();
	file.close();
	return 0;
}

int function(int input)
{
	int check = 0;
	int number = input;
	int multiply = 2;
	
	if (input == 0)
		return -1;



	
	while (1)
	{
		check = checkIfSeen(number, check);
		//cout << "number is " << number << " and check is " << check << endl;

		if (check == 1023)
		{
			//cout << "number of multiplications" << multiply << "for number" << input << endl;
			return number;
		}

		number = input * multiply;
		multiply++;
		if (multiply > 500) //magic number
			return -1;
	}
	

	return 0;
}

int checkIfSeen(int number, int check)
{
	int digit;
	int numberDigits = numDigits(number);
	//cout << "number of digits is " << numberDigits << " and number is " << number << endl;


	for (int i = 0; i < numberDigits; i++)
	{
		digit = number % 10;
		//cout << "number is " << number << " and digit is " << digit << endl;
		check = check | (1 << digit); // bitwise shift + or
		number = number / 10;
		//cout << "check is " << check << " and digit is " << digit << endl;

	}
	return check;
}


int numDigits(int x)
{
	if (x >= 10000) {
		if (x >= 10000000) {
			if (x >= 100000000) {
				if (x >= 1000000000)
					return 10;
				return 9;
			}
			return 8;
		}
		if (x >= 100000) {
			if (x >= 1000000)
				return 7;
			return 6;
		}
		return 5;
	}
	if (x >= 100) {
		if (x >= 1000)
			return 4;
		return 3;
	}
	if (x >= 10)
		return 2;
	return 1;
}
