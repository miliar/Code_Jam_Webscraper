// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	int p[] = {0x111, 0x021, 0x041, 0x281, 0x012, 0x122,0x242,0x082,0x014,0x224,0x144,0x084,0x218,0x028,0x048,0x188};
	//char* s = "OOXXOXXXOX.TO..O";

	int t = 0;
	cin >> t;

	char ignore[100];
	cin.getline(ignore, 100);

	for (int n = 0 ; n < t; n++)
	{
		char buffer[255];
		cin.getline(buffer, 255);
		cin.getline(buffer+4, 255);
		cin.getline(buffer+8, 255);
		cin.getline(buffer+12, 255);
		cin.getline(buffer+16, 255);

		char* s = buffer;

		int x = 0x3FF;
		int o = 0x3FF;
		bool completed = true;

		for (int i=0; i<16; ++i)
		{
			char c = s[i];

			if (c == 'X')
				o &= ~p[i];
			else if (c == 'O')
				x &= ~p[i];
			else if (c == '.')
			{o &= ~p[i]; x &= ~p[i]; completed = false;};
		}

		printf("Case #%d: ", n+1);

		if (x > 0) 
			printf("X won");
		else if (o > 0)
			printf("O won");
		else if (completed)
			printf("Draw");
		else
			printf("Game has not completed");

		printf("\n");

	}

	return 0;
}

