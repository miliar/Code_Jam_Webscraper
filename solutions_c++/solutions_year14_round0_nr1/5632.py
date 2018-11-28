// magic.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int compareCards(int firstLine[], int secondLine[])
{
	int count = 0;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (firstLine[i] == secondLine[j] && count == 0)
				count = firstLine[i];

			else if (firstLine[i] == secondLine[j] && count != 0)
				count = -1; // Multiple cards match
		}
	}
	return count;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ofstream fout("A-small-attempt0.out");
	ifstream fin("A-small-attempt0.in");

	int cases;
	fin >> cases;

	for (int i = 1; i <= cases; i++) {
		int firstLine;
		int secondLine;
		fin >> firstLine;
		int cards[4][4];
		int firstLineCards[4];

		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				fin >> cards[j][k];
			}
		}

		for (int j = 0; j < 4; j++) {
			firstLineCards[j] = cards[firstLine - 1][j];
		}

		int secondLineCards[4];
		fin >> secondLine;

		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				fin >> cards[j][k];
			}
		}

		for (int j = 0; j < 4; j++) {
			secondLineCards[j] = cards[secondLine - 1][j];
		}

		fout << "Case #" << i << ": ";

		int count = compareCards(firstLineCards, secondLineCards);
		if (count > 0) fout << count << '\n';
		else if (count == 0) fout << "Volunteer cheated!\n";
		else fout << "Bad magician!\n";
	}
}

