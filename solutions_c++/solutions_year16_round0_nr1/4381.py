// CountingSheep.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <set>

using namespace std;

bool notevery(set<int> &digits, int y)
{
	string s = to_string(y);
	for (unsigned int i = 0; i < s.length(); i++)
	{
		digits.erase(s[i] - '0');
		if (digits.empty())
			return false;
	}
	return true;
}

int main()
{
	ifstream input("input.in");
	if (input.is_open())
	{
		int T, N, y;
		ofstream output("output.out");
		input >> T;
		for (int i = 1; i <= T; i++)
		{
			input >> N;
			if (N == 0)
			{
				output << "Case #" << i << ": INSOMNIA" << endl;
			}
			else
			{
				
				set<int> digits = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
				int x = 0;
				do
				{
					x++;
					y = x * N;
				} while (notevery(digits, y));
				output << "Case #" << i << ": " << y << endl;
			}
		}
		input.close();
		output.close();
	}
	return 0;
}