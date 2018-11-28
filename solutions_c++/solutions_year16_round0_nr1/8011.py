// problem_a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int Case(std::ifstream& in)
{
	int N = 0;
	in >> N;

	if (N == 0)
		return -1;

	int result = 0;
	for (int j = 0; j < 10; ++j)
		result |= 1 << j;

	int curr = 0;
	int i = 0;
	while (curr != result)
	{
		++i;
		int L = N * i;
		while (L > 0)
		{
			int d = L % 10;
			L /= 10;
			curr |= 1 << d;
		}
	}
	return i * N;
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
	{
		output << "Case #" << i + 1 << ": " <<
			(res[i] <= 0 ? "INSOMNIA" : std::to_string(res[i]).c_str()) << "\n";
	}
	output.close();
}

int _tmain(int argc, _TCHAR* argv[])
{
	Run("A-large.in", "output");
	return 0;
}

