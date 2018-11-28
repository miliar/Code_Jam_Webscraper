// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int function(string input);
string flip(string input, int position);


//int function1(int input);
//int checkIfSeen(int number, int check);
//int numDigits(int x);


int main() {
	ofstream fout("output.txt");
	ifstream file;
	file.open("B-large.in", ios::in);    // open file

	int T;  // number of test cases
	file >> T;
	
	
	for (int i = 1; i <= T; i++)
	{
		string input;
		file >> input;

		int output = function(input);
		
		fout << "Case #" << i << ": " << output << endl;
	}
	

	fout.close();
	file.close();
	return 0;
}


int function(string input)
{
	int len = input.length();
	int position = 0;
	int flipcount = 0;




	for (int n = 0; ; n++)
	{
		if (input[0] == '+') // if starts with +
		{
			position = 1;
			for (int i = 1; i < len + 1 ; i++)   // checking how many + in a row
			{

				if (position == len)  // if all are + we are done
					return flipcount;

				if (input[i] == '-')
					break;
				else
					position++;

			}

			input = flip(input, position); // fliping all the + in the front
			flipcount++;
		}
		else  // starts with -
		{
			position = len;
			for (int i = len - 1; i > 0; i--)
			{
				if (input[i] == '-')
					break;
				else
					position--;
			}
			input = flip(input, position);
			flipcount++;
		}
	}

	return flipcount;
}


string flip(string input, int position)
{
	for (int i = 0; i < position; i++)
	{
		if (input[i] == '+')
			input[i] = '-';
		else
			input[i] = '+';
	}

	return input;
}


/*
int function1(int input)
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
*/