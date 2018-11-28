// problem_a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>

int Case(std::ifstream& in)
{
	int Smax = 0;
	in >> Smax;
	Smax++;

	std::vector<int> queue;
	queue.reserve(Smax);

	for (int i = 0; i < Smax; i++)
	{
		unsigned char si = 0;
		in >> si;
		queue.push_back(si - '0');
	}

	int S = 0;
	int F = 0;
	for (int i = 0; i < Smax; i++)
	{
		if (queue[i])
		{
			if (S < i)
			{
				F += i - S;
				S += F;
			}
			S += queue[i];
		}
	}
	return F;
}

void Run(const char* in, const char* out)
{
	std::ifstream input;
	input.open(in);

	int cases = 0;
	input >> cases;

	std::vector<int> res;
	for (int i = 0; i < cases; ++i)
		res.push_back(Case(input));

	input.close();

	std::ofstream output;
	output.open(out);
	for (int i = 1; i <= cases; ++i)
		output << "Case #" << i << ": " << res[i-1] << "\n";
	output.close();
}

int _tmain(int argc, _TCHAR* argv[])
{
	Run("A-small-attempt0.in", "output");
	return 0;
}

