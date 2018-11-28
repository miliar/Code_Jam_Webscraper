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

#include <iomanip>
#include <locale>
#include <sstream>
#include <string>
using namespace std;

//typedef long long LL;










int main() {
	ifstream inputFile;
	ofstream outputFile;
	inputFile.open("A-large.in");
	outputFile.open("A-large.out");

	int N =0;
	string deBuggerString;
	int nbrOfCases;
	string word;
	string newWord;
	int diff;

	int length;
	int width;
	
	inputFile >> nbrOfCases;

	int counter0[10] = { 0,0,0,0,0,0,0,0,0,0 };

	for (int i = 1; i <= nbrOfCases; i++)
	{
		//cout << "Case #" << i << ": ";
		//outputFile << "\n";
		inputFile >> word;

		//cout << word << "\n";

		length = word.length();
		//cout << length << "\n";



		int counter0[10] = { 0,0,0,0,0,0,0,0,0,0 };

		for (int j = 0; j < length; j++)
		{
			if (word[j] == 'Z'){counter0[0]++;	counter0[1]--;	}

			if (word[j] == 'O'){ counter0[1]++;}

			if (word[j] == 'W'){ counter0[2]++; counter0[1]--;}

			if (word[j] == 'H'){ counter0[3]++;}

			if (word[j] == 'U') { counter0[4]++; counter0[5]--; counter0[1]--;  counter0[9]++;}

			if (word[j] == 'F') { counter0[5]++; counter0[9]--; }

			if (word[j] == 'X') { counter0[6]++; counter0[7]--;	counter0[9]--;	}

			if (word[j] == 'S'){ counter0[7]++;}

			if (word[j] == 'G'){ counter0[8]++;	counter0[3]--;	counter0[9]--;	}

			if (word[j] == 'I'){ counter0[9]++;	}

		}
		
		int width = 0;
		outputFile << "Case #" << i << ": ";
		for (size_t k= 0; k < 10; k++)
		{
			for (size_t j = 0; j < counter0[k]; j++)
			{
				outputFile << k;
				if (k == 1 || k == 2 || k == 6) {
					width += 3;
				}
				else{
				if (k == 7 || k == 8 ||  k==3) { width += 5; }
				else
				{
					width += 4;
				}
				
				}

			}

		}

		if (length != width)
		{
			outputFile << "  FALSE!";
		}
		outputFile  << "\n";

		
	}
	//cin >> N;
	//outputFile << "\n";
	inputFile.close();
	outputFile.close();
	return 0;
}