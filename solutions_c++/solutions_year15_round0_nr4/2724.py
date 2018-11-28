// Ominous.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

string getWinner(int X, int R, int C)
{
	string winner = "";
	if (X == 1)
	{
		winner = "GABRIEL";
		goto weHaveAWinner;
	}
	if (X > 6)
	{
		winner = "RICHARD";
		goto weHaveAWinner;
	}


	if (R*C % X != 0)	
		winner = "RICHARD";	
	else if (X > R && X > C) winner = "RICHARD";
	else if ((X > 2 * C - 1 || X > 2 * R - 1) && X >= 3) winner = "RICHARD";
	else
	{
		int minim = min(R, C);
		if (X == 2 * minim - 1)
		{
			int maxi = max(R, C);
			winner = "RICHARD";
			if (minim == 2)
			{						
				for (int i = 0; i < maxi; i++)
				{
					if ((2 * i + 1) % 3 == 0)
					{
						winner = "GABRIEL";
						break;
					}
				}
			}
			else {
				for (int i = 0; i < maxi; i++)
				{
					if (3 * +2 % 5 == 0)
					{
						winner = "GABRIEL";
						break;
					}
				}
			}
		}
		else
			winner = "GABRIEL";
	}

	weHaveAWinner:

	return winner;
}

int main()
{
	ifstream input;
	ofstream output;

	input.open("Ominous.in");
	output.open("Ominous.out");

	int Tests = 0;
	int X;
	int R, C;
	input >> Tests;

	for (int i = 1; i <= Tests; i++)
	{
		
		input >> X >> R >> C;

		string result = getWinner(X, R, C);
	
		output << "Case #" << i << ": " << result << "\n";
	}

	input.close();
	output.close();
	return 0;
}

