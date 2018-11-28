// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <Windows.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void ConvertIntoDigits(DWORDLONG N, int& result)
{
	int SetBit = 1;
	while (N)
	{
		result = result | (SetBit << (N % 10));
		 N /= 10;
	}
}

DWORDLONG CountingSheep(DWORDLONG N)
{
	int result=0;
	for (int i = 1; i < 10000; i++)
	{
		ConvertIntoDigits(N*i, result);
		if (result == 1023)
			return(N*i);
	}
	return(0);
}

int _tmain(int argc, _TCHAR* argv[])
{
	int casen = 1;
	DWORDLONG N=0;
	char temp[512];
	std::ifstream oInput(L"input.txt");
	std::string  text;
	ofstream resultfile;
	resultfile.open("output.txt");
	while (getline(oInput, text))
	{
		sscanf_s(text.c_str(), "%ld", &N);
		if(CountingSheep(N) == 0)
			sprintf_s(temp, "Case #%d: INSOMNIA\n", casen++);
		else
			sprintf_s(temp, "Case #%d: %d\n", casen++, CountingSheep(N));

		resultfile << temp;
	}
	resultfile.close();
	oInput.close();
	return 0;
}
