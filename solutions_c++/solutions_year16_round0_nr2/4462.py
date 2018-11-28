// Revenge.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int compute(string s)
{
	int y = 0;
	int i = 0;
	char last = s.at(i);
	while (i < s.length())
	{
		if (s.at(i) != last)
			y++;
		last = s.at(i);
		i++;
	}
	if (s.at(i - 1) == '-')
		y++;
	return y;
}

int main()
{
	ifstream input("input.in");
	if (input.is_open())
	{
		int T;
		ofstream output("output.out");
		input >> T;
		for (int i = 1; i <= T; i++)
		{
			string S;
			input >> S;
			int y = compute(S);
			output << "Case #" << i << ": " << y << endl;
		}
		input.close();
		output.close();
	}
	return 0;
}