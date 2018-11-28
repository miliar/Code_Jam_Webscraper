// problem_d.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <queue>
#include <algorithm>
#include <functional>


const char* Case(std::ifstream& in)
{
	int X = 0;
	in >> X;

	int Row = 0;
	in >> Row;

	int Col = 0;
	in >> Col;

	if (X >= 7)
		return "RICHARD";

	if (std::max(Col, Row) < X)
		return "RICHARD";

	if (std::min(Col, Row) < (X/2 + X%2))
		return "RICHARD";

	if ((Col * Row) % X)
		return "RICHARD";

	if (std::min(Col, Row) == 3 && X == 6)
		return "RICHARD";

	if (std::min(Col, Row) == 2 && X == 4)
		return "RICHARD";
	
	return "GABRIEL";
}

void Run(const char* in, const char* out)
{
	std::ifstream input;
	input.open(in);

	int cases = 0;
	input >> cases;

	std::vector<const char*> res;
	for (int i = 0; i < cases; ++i)
	{
		res.push_back(Case(input));
		std::cout << i << "\n";
	}

	input.close();

	std::ofstream output;
	output.open(out);
	for (int i = 0; i < cases; ++i)
		output << "Case #" << i + 1 << ": " << res[i] << "\n";
	output.close();
}

int _tmain(int argc, _TCHAR* argv[])
{
	Run("D-small-attempt1.in", "output_d");
	return 0;
}

