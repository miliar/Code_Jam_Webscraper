// Round1A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

void readCRLF(std::ifstream& fin)
{
	//char newline;
	//fin >> newline >> newline;
}

void processPuzzle(__int64 index, __int64 r, __int64 t)
{
	std::cout << "Case #" << index << ": ";

	__int64 left = t, count = 0;
	while (left > 0)
	{
		__int64 required = 4*count + 2*r +1;
		if (left >= required)
		{
			left -= required;
			count++;
		}
		else
			break;
	}

	std::cout << count << std::endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin(argv[1], ios::binary);

	__int64 cases = 0;
	fin >> cases;

	for (__int64 i = 0; i<cases; ++i)
	{
		__int64 r = 0, t = 0;
		
		fin >> r >> t;
		readCRLF(fin);

		processPuzzle(i+1, r, t);

		if (i != cases-1)
			readCRLF(fin);
	}
}

