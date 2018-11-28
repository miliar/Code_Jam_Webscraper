//============================================================================
// Name        : task1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <stdint.h>
#include <string>

bool checkn(uint64_t n, uint64_t& flags)
{
	do
	{
		uint64_t num = n % 10;
		flags |= 1 << num;
		if ((flags & 0x3ff) == 0x3ff)
		{
			//std::cout << flags << std::endl;
			return true;
		} 
		n /= 10; 
	}
	while (n > 0);

	return false;
}

int main()
{
	std::fstream f;
	f.open("A-large.in");

	int T = 0;
	f >> T;

	for (int i = 0; i < T; ++i)
	{
		uint64_t N = 0;
		f >> N;

		int limit = 10000000;
		uint64_t flags = 0;
		uint64_t NN = N;
		bool found = false;
		while (limit --> 0)
		{
			if (checkn(NN, flags))
			{
				std::cout << "Case #" << (i + 1) << ": " << NN << std::endl;
				found = true;
			}

			if (found)
			{
				break;
			}

			NN += N;
		} 

		if (not found)
		{
			std::cout << "Case #" << (i + 1) << ": INSOMNIA" << std::endl; 
		}
	}
}












