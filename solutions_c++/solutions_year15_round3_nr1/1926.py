// Problem1.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
#include <vector>
#include <iostream>
#include<algorithm>
#include <string>
#include <set>
#include <fstream>
#include <cassert>
#include <sstream>
using namespace std;

std::vector<int> ConvertSpacedInts(std::string& line)
{
	std::vector<int> integers;
	std::istringstream iss(line);
	int n;
	while (iss >> n)
	{
		integers.push_back(n);
	}
	return integers;
}

int lowestscore(int C, int W)
{

	int Minscore = 0;

	if (C == W) return C;
	if (C >= 2*W)
	{
		C = C - W;
		Minscore++;
		//if (lowestscore(2 * W - 1, W) < lowestscore(C, W))
		//{
		//	return Minscore + lowestscore(2 * W - 1, W);
		//}
		//else
		//{
		//	return Minscore + lowestscore(C, W);
		//}
		return 1 + lowestscore(C, W);
	}
	else
	{
		return W + 1;
		// choose to remove the 

	}

}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream input("A-small-attempt0.in");

	ofstream output("output.txt");



	std::string Line;
	//std::getline(input, Line);
	//std::vector<int> line = ConvertSpacedInts(Line);

	int T = 4;

	 input>>T;

	int R = 1;
	int C = 5;

	int W = 1;

	for (int i = 0; i < T; i++)
	{
		input >> R;
		input >> C;
		input >> W;

		output << "Case #" << i+1 << ": " << R*lowestscore(C, W) << std::endl;
		std::cout << "Case #" << i+1 << ": " << R*lowestscore(C, W) << std::endl;
	}



	return 0;
}

