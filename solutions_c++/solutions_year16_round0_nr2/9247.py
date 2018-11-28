// ConsoleApplication5.cpp : Definiert den Einstiegspunkt für die 
Konsolenanwendung.
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
#include <array>
using namespace std;

//typedef long long LL;

int main() {
	ifstream inputFile;
	ofstream outputFile;
	inputFile.open("B-large.in");
	outputFile.open("B-large.out");

	int N;
	string deBuggerString;
	int nbrOfCases;
	char sign;
	


	string pancakePile;
	char lastPancake;
	int flips;
	inputFile >> nbrOfCases;


	for (size_t i = 1; i <= nbrOfCases; i++)
	{


		inputFile >> pancakePile;
		
		pancakePile = pancakePile.append("+");


		lastPancake = pancakePile[0];
		flips = 0;
		for (size_t j = 0; j < pancakePile.length(); j++)
		{
			if (lastPancake != pancakePile[j])
			{
				flips++;
			}
			lastPancake = pancakePile[j];
		}
		
		outputFile << "Case #" << i << ": " << flips << "\n";
	}

	inputFile.close();
	outputFile.close();
	return 0;
}