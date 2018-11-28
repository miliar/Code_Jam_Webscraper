#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <istream>
#include <sstream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <string>
#include <iomanip>

std::string inFile = "cookie.in.txt";
std::ifstream iFile(inFile.c_str());

int readInt()
{
	int choice;

	std::string line;
	std::getline(iFile, line);

	std::istringstream in(line);
	if (!(in >> choice))
	{
		std::cout << "error while reading user choice" << std::endl;
		exit(1);
	}

	return choice;
}

int _tmain(int argc, _TCHAR* argv[])
{
	// number_of_test_cases
	int t = readInt();
	long double R0 = 2.0000000;

	for (int i = 1; i<=t; i++)
	{
		long double C, F, X;

		// read C, F and X
		std::string line;
		std::getline(iFile, line);
		std::istringstream in(line);
		in >> C >> F >> X;

		// set precision to width 7
		std::cout.precision(7);
		std::cout.setf(std::ios::fixed, std::ios::floatfield);

		if (X <= C)
		{
			std::cout << "Case #" << i << ": " << X / R0 << std::endl;
		}
		else
		{
			long double mintime = X / R0;
			int farmBuyCount = 1;

			while (true)
			{
				long double tempTime = 0.0;

				for (int j = 0; j <= farmBuyCount - 1; j++)
				{
					tempTime += C / (R0 + j*F);
				}

				tempTime += (X / (R0 + farmBuyCount * F));

				if ( tempTime > mintime)
				{
					std::cout << "Case #" << i << ": " << mintime << std::endl;
					break;
				}
				else
				{
					mintime = tempTime;
					farmBuyCount += 1;
				}
			}
		}
	}
	
	iFile.close();
	return 0;
}
