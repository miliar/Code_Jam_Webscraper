// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <math.h>
#include <string>

using namespace std;

void readCRLF(std::ifstream& fin)
{
	//char newline;
	//fin >> newline >> newline;
}

bool check(string s, __int64 n)
{
	string vowels = "aeiou";
	__int64 length = s.size();
	__int64 countV = 0, countS = 0, count = 0;
	for (string::const_iterator idx=s.begin(); idx!=s.end(); ++idx)
	{
		bool isV = false;
		for (string::const_iterator idxVowels=vowels.begin(); idxVowels!=vowels.end(); ++idxVowels)
		{
			if (*idx == *idxVowels)
			{
				isV = true;
				countS = 0;
				break;
			}
		}
		if (!isV)
		{
			countS++;
			if (countS >= n)
				return true;
		}
	}
	return false;
}

void processPuzzle(int index, string& name, __int64 n)
{
	std::cout << "Case #" << index << ": ";


	string vowels = "aeiou";

	__int64 L = name.size();

	__int64 countV = 0, countS = 0, count = 0;

	//for (string::const_iterator idx=name.begin(); idx!=name.end(); ++idx)
	//{
	//	for (string::const_iterator idxVowels=vowels.begin(); idxVowels!=vowels.end(); ++idxVowels)
	//	{
	//		if (*idx == *idxVowels)
	//			countV++;
	//	}
	//}

	//countS = L - countV;

	for (__int64 length = n; length <= L; ++length)
	{
		for (__int64 idx=0; idx <= L - length; ++idx)
		{
			string substr = name.substr(idx, length);
			if (check(substr, n))
			{
				//std::cout << substr << ",";
				count++;
			}
		}
	}
	std::cout << count << std::endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin(argv[1], ios::binary);

	int cases = 0;
	fin >> cases;

	for (int i = 0; i<cases; ++i)
	{
		__int64 n = 0;
		string name;
		
		fin >> name >> n;
		readCRLF(fin);

		processPuzzle(i+1, name, n);

		if (i != cases-1)
			readCRLF(fin);
	}
}

