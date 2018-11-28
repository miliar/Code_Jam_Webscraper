#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream fin("standingovation.in");
	ofstream fout("standingovation.out");
	int CASES;
	fin >> CASES;
	for (int CASENUMBER = 1; CASENUMBER <= CASES; CASENUMBER++)
	{
		int max;
		fin >> max;

		char asdf;
		fin >> asdf;
		asdf = (asdf + 1 - '1');

		int sum = asdf;
		int extraneeded = 0;

		for (int i = 1; i <= max; i++)
		{
			fin >> asdf;
			asdf = (asdf + 1 - '1');
			if (asdf == 0)
			{
				continue;
			}
			if (sum < i)
			{
				extraneeded += (i - sum);
				sum = i;
			}
			sum += asdf;
		}

		fout << "Case #" << CASENUMBER << ": " << extraneeded << endl;

	}
}
