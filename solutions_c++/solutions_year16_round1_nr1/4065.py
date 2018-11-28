// ConsoleApplication5.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//

#include "stdafx.h"

#include <stdio.h>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>
#include <array>
using namespace std;

//typedef long long LL;










int main() {
	ifstream inputFile;
	ofstream outputFile;
	inputFile.open("large1.in");
	outputFile.open("large1.out");

	int N =0;
	string deBuggerString;
	int nbrOfCases;
	string word;
	string newWord;
	int diff;

	int length;
	
	inputFile >> nbrOfCases;


	for (size_t i = 1; i <= nbrOfCases; i++)
	{
		//cout << "Case #" << i << ": ";
		//outputFile << "Case #" << i << ":";
		inputFile >> word;
		newWord = word;
		//cout << word << "\n";

		length = word.length();
		//cout << length << "\n";

		int delLetter[1000] = {};
		int maxLetterPos = 0;
		int counter = 0;

		for (size_t j = 0; j < length; j++)
		{

			diff = word[maxLetterPos] - word[j];
			//cout << maxLetterPos << "\n";
			if (diff <=  0)
			{
				maxLetterPos = j;
				delLetter[j] = 1;
				
			}
		}
		
		for (size_t j = 0; j < length; j++)
		{

			if (delLetter[length-j-1] == 1)
			{
				newWord[counter] = word[length - j - 1];
				counter = counter + 1;

			}
		}		
		
		for (size_t j = 0; j < length; j++)
		{

			if (delLetter[j] == 0)
			{
				newWord[counter] = word[j];
				counter = counter + 1;

			}
		}

		//cout << "Case #" << i << ": " << newWord << "\n";

		outputFile << "Case #" << i << ": " << newWord << "\n";

		//outputFile << "\n";
		//outputFile << "Case #" << i << ": " << flips << "\n";
	}
	cin >> N;
	inputFile.close();
	outputFile.close();
	return 0;
}