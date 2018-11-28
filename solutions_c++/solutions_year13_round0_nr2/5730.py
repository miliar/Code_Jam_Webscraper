// Lawn.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace std;

ifstream input;
ofstream output;

bool solve()
{
	short lawn[100][100];
	bool checked[100][100];

	int n,m;
	int min = 999999;

	input >> n >> m;
	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
		{
			input >> lawn[i][j];
			checked[i][j] = false;

			if(min > lawn[i][j])
				min = lawn[i][j];
		}

	for(int i = 0; i < n; i++)
	{
		bool line = true;
		for(int j = 0; j < m; j++)
			if(min != lawn[i][j])
			{
				line = false;
				break;
			}
		
		if(line)
			for(int j = 0; j < m; j++)
				checked[i][j] = true;
	}

	for(int j = 0; j < m; j++)
	{
		bool line = true;
		int same = lawn[0][j];
		for(int i = 0; i < n; i++)
			if(min != lawn[i][j])
			{
				line = false;
				break;
			}

		if(line)
			for(int i = 0; i < n; i++)
				checked[i][j] = true;
	}

	bool result = true;
	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < m; j++)
			if(!checked[i][j] && lawn[i][j] == min)
				result = false;
	}

	return result;
}

int _tmain(int argc, _TCHAR* argv[])
{
	input.open("input.txt");
	output.open("output.txt");

	short t;
	input >> t;

	for(short i = 0; i < t; i++)
		output << "Case #" << i + 1 << ": " << (solve() ? "YES" : "NO") << endl;

	input.close();
	output.close();

	return 0;
}

