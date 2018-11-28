// problem_b.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

void maneuver(std::vector<bool>& stack, int p)
{
	for (int i = 0; i < (p / 2); ++i)
	{
		bool tmp = !stack[i];
		stack[i] = !stack[p - i - 1];
		stack[p - i - 1] = tmp;
	}
	if (p % 2)
	{
		stack[p / 2] = !stack[p / 2];
	}
}

int Case(std::ifstream& in)
{
	std::string s;
	in >> s;

	std::vector<bool> stack;
	stack.reserve(s.length());

	for (char c : s)
	{
		stack.push_back(c == '+');
	}

	int res = 0;
	int last = stack.size() - 1;

	while (last >= 0)
	{
		if (stack[last])
		{
			--last;
		}
		else
		{
			int p = 0;
			while (p < last && stack[p])
				++p;

			if (p > 0)
			{
				maneuver(stack, p);
				++res;
			}

			maneuver(stack, last + 1);
			++res;
		}
	}

	return res;
}

void Run(const char* in, const char* out)
{
	std::ifstream input;
	input.open(in);

	int cases = 0;
	input >> cases;

	std::vector<int> res;
	for (int i = 0; i < cases; ++i)
	{
		res.push_back(Case(input));
		std::cout << i << "\n";
	}

	input.close();

	std::ofstream output;
	output.open(out);
	for (int i = 0; i < cases; ++i)
		output << "Case #" << i+1 << ": " << res[i] << "\n";
	output.close();
}

int _tmain(int argc, _TCHAR* argv[])
{
	Run("B-large.in", "output_l");
	return 0;
}

