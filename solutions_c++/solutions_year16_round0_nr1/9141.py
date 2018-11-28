// ConsoleApplication5.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//

#include "stdafx.h"

#include <stdio.h>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <array>
using namespace std;

//typedef long long LL;

int main() {
	ifstream inputFile;
	ofstream outputFile;
	inputFile.open("exampleLarge.in");
	outputFile.open("exampleLarge.out");
	int nbrOfCases;
	int N;
	int currentNumber;
	int tempNumber;
	int numberLength;
	string deBuggerString;

	string numberString;
	int remainderTen;

	std::array<int, 10> digits = { 0,0,0,0,0,0,0,0,0,0 }; // digits 0-9 appeared yet
	std::array<int, 10> zeros = { 0,0,0,0,0,0,0,0,0,0 };
	std::array<int, 10> ones = { 1,1,1,1,1,1,1,1,1,1 };
	
	inputFile >> nbrOfCases; 
	cout << nbrOfCases << "\n";
	for (size_t i = 1; i <= nbrOfCases; i++)
	{
		inputFile >> N; 
		//cout << N << "    N  \n";
		currentNumber = 0;
		

			if (N==0)
			{
				outputFile << "Case #1: INSOMNIA" << "\n";

			}
			else
			{
				while (digits != ones)
				{
					currentNumber = currentNumber + N;
					tempNumber = currentNumber;
					while (tempNumber != 0)
					{
						remainderTen = (tempNumber) % 10;
						tempNumber = (tempNumber - remainderTen) / 10;
						if (digits[remainderTen] == 0)
						{
							digits[remainderTen] = 1;
						}
					}

				}
				outputFile << "Case #" << i << ": " << currentNumber << "\n";
				digits = zeros;
			}


	}
	//myfile << "Writing this to  a file.\n";
	//cin >> N;
	inputFile.close();
	outputFile.close();
	return 0;
}