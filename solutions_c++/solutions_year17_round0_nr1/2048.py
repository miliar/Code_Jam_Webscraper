// 2017_Qualification_A_OversizedPancakeFlip.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

std::ifstream input("A-large.in");
std::ofstream output("Results-large.txt");

void flip(char& a)
{
	if (a == '+')
		a = '-';
	else
		a = '+';
}

int solve()
{
	std::string pancakes;
	int k;
	input >> pancakes >> k;
	int fpos = pancakes.size() - k + 1;
	int flipcount = 0;

	for (int i = 0; i < fpos; i++)
	{
		if (pancakes[i] == '-')
		{
			flipcount++;
			for (int j = i; j < i + k; j++)
				flip(pancakes[j]);
		}
	}

	bool foundMinus = false;
	for (int index = pancakes.size(); index >= fpos; index--)
	if (pancakes[index] == '-')
		foundMinus = true;

	if (foundMinus)
		return -1;
	else
		return flipcount;
}

int main()
{
	int T;
	input >> T;
	
	for (int cas = 1; cas <= T; cas++)
	{
		int sol = solve();
		if (sol == -1)
		{
			std::cout << "Case #" << cas << ": " << "IMPOSSIBLE\n";
			output << "Case #" << cas << ": " << "IMPOSSIBLE\n";
		}
		else
		{
			std::cout << "Case #" << cas << ": " << sol << "\n";
			output << "Case #" << cas << ": " << sol << "\n";
		}
	}
}
