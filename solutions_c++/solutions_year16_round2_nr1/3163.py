//============================================================================
// Name        : task1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <array>
#include <iostream>
#include <fstream>
#include <map>
#include <stdint.h>
#include <string>
#include <vector>

std::vector<std::string> cf = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int nc(std::string& s, char c)
{
	int count = 0;
	for (int n = 0; n < s.size(); ++n)
	{
		if (s[n] == c)
		{
			count ++;
		}
	}
	return count;
}

void subc(int* abc, int z, int k)
{
	for (int n = 0; n < cf[z].size(); ++n)
	{
		char c = cf[z][n];
		abc[c - 'A'] -= k;
	}
}

int main()
{
	std::fstream f;
	f.open("A-large.in");

	int T = 0;
	f >> T;

	for (int i = 0; i < T; ++i)
	{
		std::string word;
		f >> word;

		int abc[26] = {0};
		for (int n = 0; n < 26; ++n)
		{
			abc[n] = nc(word, n + 'A');
		}

		int nn[10] = {0};

		nn[0] = abc['Z' - 'A'];
		subc(abc, 0, nn[0]);

		nn[2] = abc['W' - 'A'];
		subc(abc, 2, nn[2]);
		
		nn[4] = abc['U' - 'A'];
		subc(abc, 4, nn[4]);

		nn[6] = abc['X' - 'A'];
		subc(abc, 6, nn[6]);

		nn[8] = abc['G' - 'A'];
		subc(abc, 8, nn[8]);

		nn[1] = abc['O' - 'A'];
		subc(abc, 1, nn[1]);

		nn[3] = abc['R' - 'A'];
		subc(abc, 3, nn[3]);

		nn[5] = abc['F' - 'A'];
		subc(abc, 5, nn[5]);

		nn[7] = abc['S' - 'A'];
		subc(abc, 7, nn[7]);

		nn[9] = abc['E' - 'A'];
		subc(abc, 9, nn[9]);

		std::cout << "Case #" << (i+1) << ": ";

		for (int k = 0; k < 10; ++k)
		{
			for (int f = 0; f < nn[k]; ++f)
			{
				std::cout << k;
			}
		}

		std::cout << std::endl;

//		break;
	}
}












