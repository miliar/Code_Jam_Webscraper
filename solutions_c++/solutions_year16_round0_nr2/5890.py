// GCJ.cpp : Defines the entry point for the console application.
//
#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <string>
#include <math.h>
#include <functional>

//#define verbose

using namespace std;

int main()
{
	// First let's read the file
	freopen("gcj.in", "r", stdin);
	freopen("gcj.out", "w", stdout);

	int i, j, k, Ncases;
	char *pancakes = new char[101];

	cin >> Ncases;

	// Test cases
	for (i=0; i<Ncases; i++)
	{
		int minFlips = 0;
		memset(pancakes, 0x00, 101);
		cin >> pancakes;
		j = strlen(pancakes) - 1;
		bool happy = (pancakes[j--] == '+');
		bool lastHappy = happy;
		if (!happy)
			minFlips++;

		while (j >= 0)
		{
			happy = (pancakes[j--] == '+');
			if (happy != lastHappy)
			{
				lastHappy = happy;
				minFlips++;
			}
		}


		cout << "Case #" << i + 1 << ": " << minFlips << endl;
	}

	return 0;
}

