// problem_b.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <queue>
#include <algorithm>
#include <functional>

int r(std::vector<int>& stacks, int D)
{
	int deapth = 0;
	int subdivisions = 0;
	for (deapth = D; deapth > 1; deapth--)
	{
		if (int num = stacks[deapth])
		{
			int steps = deapth;
			for (int i = 1; i < deapth - 1; ++i)
			{
				int d1 = i;
				int d2 = deapth - i;

				std::vector<int> divided = stacks;
				divided[deapth] = 0;
				divided[d1] += num;
				divided[d2] += num;

				steps = std::min(steps, r(divided, deapth) + num);
			}

			return steps;
		}
	}

	return deapth;
}

int Case(std::ifstream& in)
{
	int s = 0;
	in >> s;

	std::vector<int> stacks;
	stacks.resize(1001, 0);

	int deapth = 0;
	for (int i = 0; i < s; i++)
	{
		in >> deapth;
		stacks[deapth]++;
	}

	return r(stacks, 1000);
}

int Case1(std::ifstream& in)
{
	int s = 0;
	in >> s;

	std::vector<int> diners;

	int deapth = 0;
	for (int i = 0; i < s; i++)
	{
		in >> deapth;
		diners.push_back(deapth);
	}

	std::sort(diners.begin(), diners.end(), std::greater<int>());

	int iterations = 0;
	while (diners.size() > 0)
	{
		int d = diners[0] / 2;
		if (diners[0] > (int)diners.size())
		{
			diners.push_back(diners[0] - d);
			diners[0] = d;
			std::sort(diners.begin(), diners.end(), std::greater<int>());
		}
		else
		{
			for (auto& v : diners)
				--v;
			diners.erase(std::remove(diners.begin(), diners.end(), 0), diners.end());
		}
		iterations++;
	}

	return iterations;
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
	for (int i = 0; i < cases; ++i)
		output << "Case #" << i+1 << ": " << res[i] << "\n";
	output.close();
}

int _tmain(int argc, _TCHAR* argv[])
{
	Run("B-small-attempt4.in", "output_b");
	return 0;
}

