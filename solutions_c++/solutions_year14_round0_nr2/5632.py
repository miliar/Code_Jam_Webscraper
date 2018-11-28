// cookieclicker.cpp : Defines the entry point for the console application.
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
	//ofstream fout("B-small-attempt0.out");
	ifstream fin("B-large.in");

	FILE * pFile;
	pFile = fopen("B-large.out", "w");

	int cases;
	fin >> cases;

	for (int i = 1; i <= cases; i++) {
		double cost;
		double farm;
		double goal;
		double cps = 2.0; // Cookies per second

		fin >> cost >> farm >> goal;

		bool found = false;
		double lastTime = goal / cps;
		double currTime = cost / cps;

		while (!found) {
			cps += farm; // Buy a farm.
			currTime += goal / cps;

			if (currTime > lastTime)
				found = true;

			else {
				lastTime = currTime;
				currTime = currTime - goal / cps + cost / cps;
			}
		}

		fprintf(pFile, "Case #%i: %9.7f\n", i,lastTime);
	}
	fclose(pFile);
}


