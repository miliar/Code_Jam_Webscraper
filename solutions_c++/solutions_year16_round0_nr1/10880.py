// CountingSheep.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
#include "cstdio"
#include <fstream>
#include <iterator>
#include <bitset> 
int main()
{
	std::ifstream input;
	input.open("input.in");
	std::ofstream output;
	output.open("output.txt");
	int T;
	uint32_t num;
	uint32_t checkNum;
	uint32_t caseNum = 1;
	uint32_t iter = 0;
	uint32_t tempNum = 0;
	input >> T;
	std::bitset<10> checkBit(std::string("0000000000"));
	while (input >> num)
	{
		checkBit = 0;
		if (num == 0)
		{
			output << "Case #" << caseNum << ":" << " INSOMNIA" << std::endl;
			caseNum++;
			continue;
		}
		iter = 1;
		while (~checkBit != 0)
		{
			checkNum = num * iter;
			tempNum = 10;
			while (tempNum <= checkNum *10)
			{
				checkBit |= 1 << (checkNum%tempNum/(tempNum/10));
				tempNum *= 10;
			}
			iter++;
		}
		output << "Case #" << caseNum << ": " << checkNum << std::endl;
		caseNum++;
	}

    return 0;
}

