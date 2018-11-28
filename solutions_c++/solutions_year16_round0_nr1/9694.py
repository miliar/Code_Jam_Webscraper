#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ifstream fin("file.in");
	ofstream fout("file.out");
	int CASES;
	fin >> CASES;

	for (int CASE = 1; CASE <= CASES; CASE++)
	{
		fout << "Case #" << CASE << ": ";
		int a;
		fin >> a;

		int counter = 0;
		if (a == 0)
		{
			fout << "INSOMNIA" << endl;
			continue;
		}
		else
		{
			vector<int> numberofdigits;
			bool digits[10];
			for (int i = 0; i < 10; i++)
			{
				digits[i] = false;
			}
			
			while (numberofdigits.size() < 10)
			{
				counter++;
				int acopy = a*counter;
				while (acopy != 0)
				{
					int d = acopy % 10;
					acopy /= 10;
					if (digits[d] == false)
					{
						digits[d] = true;
						numberofdigits.push_back(0);
					}
				}
			}
		}
		fout << a*counter << endl;

	}




	return 0;
}