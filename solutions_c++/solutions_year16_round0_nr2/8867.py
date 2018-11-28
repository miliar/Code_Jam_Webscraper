// pancakes.cpp : main project file.

#include "stdafx.h"
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

string negate(string b)
{
	for (int i = 0; i < b.length(); i++)
	{
		if (b[i] == '+')
		{
			b[i] = '-';
		}
		else
		{
			b[i] = '+';
		}
	}return b;
}

int solve(string b)
{
	if (b == "+")
	{
		return 0;
	}
	else if (b == "-")
	{
		return (1);
	}
	else if (b[b.length() - 1] == '+')
	{
		return solve(b.substr(0, b.length() - 1));
	}
	else if (b[b.length() - 1] == '-')
	{
		return solve(negate(b).substr(0, b.length() - 1)) + 1;
	}
}

int main()
{
	int t;
	ifstream fcin;
	fcin.open("B-large.in");
	ofstream fcout;
	fcout.open("outl.txt");
	fcin >> t;
	for (int i = 0; i < t; i++)
	{
		string b;
		fcin>>b;
		fcout << "Case #" << i + 1 << ": " << solve(b) << endl;
	}
	fcout.close();
	return 0;
}
