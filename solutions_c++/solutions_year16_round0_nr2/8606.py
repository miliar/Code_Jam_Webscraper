// ConsoleApplication1.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

bool P[100];
int Len = 0;

void Solve2(int TID)
{

	int count = 0;
	bool last = P[0];
	for (int i = 1; i < Len; i++)
	{
		if (last!=P[i])
		{
			count++;
			last = P[i];
		}
	}
	if (!P[Len-1]) count++; 
	printf("Case #%d: %d\n", TID, count);
}

int main()
{
	string input_line;
	unsigned long long int  T;
	scanf_s("%lld", &T);
	std::getline(std::cin, input_line);

	for (int i = 1; i <= T; i++)
	{
		std::getline(std::cin,input_line);
		Len = input_line.length();
		for (int j = 0; j < Len; j++)
		{
			P[j] = (input_line[j] == '+');
		}
		Solve2(i);
	}
	return 0;
}


