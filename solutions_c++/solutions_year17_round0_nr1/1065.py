// Pancake Flipper.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

int GetAmountOfFlips(std::string pancakes, int flippersize)
{
	int flips = 0;
	for (int i = 0; i < pancakes.length(); i++)
	{

		if (pancakes[i] == *"-")
		{
			if (i > pancakes.length() - flippersize)
			{
				return -1;
			}
			flips += 1;
			for (int j = 0; j < flippersize; j++)
			{
				(pancakes[i + j] == *"+") ? pancakes[i + j] = *"-" : pancakes[i + j] = *"+";
			}
		}
	}
	return flips;
}


int _tmain(int argc, _TCHAR* argv[])
{
	int nootests;
	std::cin >> nootests;
	for (int i = 1; i <= nootests; i++)
	{
		std::string pancakes;
		int flippersize;
		int steps;
		std::cin >> pancakes >> flippersize;
		//std::cout << pancakes << " " << flippersize << std::endl;
		steps = GetAmountOfFlips(pancakes, flippersize);
		if (steps == -1)
		{
			std::cout << "Case #" << i << ": " << "IMPOSSIBLE" << std::endl;
		}
		else
		{
			std::cout << "Case #" << i << ": " << steps << std::endl;
		}
	}
	return 0;
}

