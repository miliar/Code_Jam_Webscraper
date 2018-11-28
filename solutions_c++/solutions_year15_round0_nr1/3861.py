// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>


int getAnumber(int length, char *string)
{
	int result = 0;
	int sum = 0;
	int added = 0;
	for(int i = 0; i <= length; i++)
	{
		int number = string[i] - '0';
		if(number == 0)
			continue;
		if(sum < i)
		{
			added = i - sum;
			sum += number + added;
			result += added;
		}
		else
		{
			sum += number;
		}
	}
	return result;
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fp;
	fopen_s(&fp, "c:\\A-large.in", "r");


	int count = 0;
	fscanf(fp, "%d", &count);
	int length = 0;
	char buff[1024];

	for(int i = 0; i < count; i++)
	{
		fscanf(fp, "%d %s", &length, buff);
		printf("Case #%d: %d\n", i+1, getAnumber(length, buff));
	}
}


