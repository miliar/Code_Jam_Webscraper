// CodeJam2016B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;
int minFlips(char * input)
{
	int res = 0;
	int start = 0;
	int i = start;
	int len = strlen(input);
	char k;
	while(start < len)
	{
		k = input[start];
		i = start;
		while(i < len && input[i] == k)
			i++;

		if(i == len)
		{
			//handle case where array ends
			if(k == '-')
				res++;
		}
		else
		{
			res++;
		}
		start = i;
	}
	return res;
}


int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	FILE* fout;
	char input[110];
	cin >> t;
	freopen_s(&fout, "output.txt","w",stderr);
	for(int i  = 1; i <= t; i++)
	{
		cin >> input;
		int res = minFlips(input);
		fprintf_s(fout, "Case #%d: %d\n",i, res);
	}
	return 0;
}

