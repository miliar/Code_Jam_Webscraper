// ConsoleApplication3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <vector>

using namespace std;


int playWar(int numBlocks, vector<double> naomiArray, vector<double> kenArray)
{
	int score = 0;
	for (int i = numBlocks - 1; i >= 0; i--)
	{
		for (int j = 0; j < numBlocks; j++)
		{
			if (kenArray[j] > naomiArray[i])
			{
				kenArray.erase(kenArray.begin() + j);
				naomiArray.erase(naomiArray.begin() + i);
				break;
			}
			if (j == numBlocks - 1)
			{
				score++;
				kenArray.erase(kenArray.begin());
				naomiArray.erase(naomiArray.begin() + i);
				//remove kenarray[0] and naomiarray[i]
				break;
			}
		}
		numBlocks--;
	}
	return score;
}

int playDWar(int numBlocks, vector<double> naomiArray, vector<double> kenArray)
{
	int score = 0;
	for (int i = numBlocks - 1; i >= 0; i--)
	{
		if (naomiArray[i] > kenArray[i])
		{
			score++;
			kenArray.erase(kenArray.begin() + i);
			naomiArray.erase(naomiArray.begin() + i);
		}
		else
		{
			kenArray.erase(kenArray.begin() + i);
			naomiArray.erase(naomiArray.begin());
		}
		numBlocks--;
	}
	return score;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int numGames;
	int numBlocks;


	in >> numGames;

	for (int i = 1; i <= numGames; i++)
	{
		in >> numBlocks;
		vector<double> naomiArray(numBlocks);
		vector<double> kenArray(numBlocks);
		for (int j = 0; j < numBlocks; j++)
		{
			in >> naomiArray[j];
		}
		for (int j = 0; j < numBlocks; j++)
		{
			in >> kenArray[j];
		}
		sort(naomiArray.begin(), naomiArray.end());
		sort(kenArray.begin(), kenArray.end());
		int warScore = playWar(numBlocks, naomiArray, kenArray);
		int dwarScore = playDWar(numBlocks, naomiArray, kenArray);
		out << "Case #" << i << ": " << dwarScore << " " << warScore << endl;
	}

	return 0;
}

