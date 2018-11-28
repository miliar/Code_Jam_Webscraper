// ConsoleApplication3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	int testCases;
	int Smin, Smax, index, friends;

	string sShy;
	
	cin >> testCases; 

	for (int i = 0; i < testCases; i++)
	{
		cin >> Smax >> sShy;

		Smin = index = friends = 0;
		
		int Shy[1000];

		for (int j = 0; j < sShy.length(); j++)
		{
			Shy[j] = sShy[j] - '0';
		}

		while (Smin < Smax)
		{
			if (Shy[index] > 0)
			{
				Smin = Smin + Shy[index];
				index++;
			}

			else
			{
				while (Shy[index] == 0)
				{
					friends++;
					Smin++;
					index++;
				}
			}
		}

		cout << "Case #" << i + 1 << ": " << friends << endl;
	//	cerr << "Case #" << i + 1 << ": " << friends << endl;
	}


	
	return 0;
}

