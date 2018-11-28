// pancakes.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>


int main(int argc, char * argv[])
{
	using namespace std;

	if (argc < 2)
	{
		cerr << "Usage: " << argv[0] << " file.in" << endl;
		return 1;
	}
	const string inputName = argv[1];

	ifstream input;
	input.open(inputName);
	if (!input)
	{
		cerr << "Couldn't open input file " << inputName << endl;
		return 2;
	}

	string outputName(inputName, 0, inputName.rfind(".in"s));
	outputName += ".out";

	ofstream output;
	output.open(outputName);
	if (!output)
	{
		cerr << "Couldn't open output file " << outputName << endl;
		return 3;
	}

	int cases;
	input >> cases;

	int result;
	for (int n = 1; n <= cases; ++n)
	{
		vector<char> pancakes;
		string line;
		input >> line;
		for (auto c : line) pancakes.push_back(c);
		result = 0;
		while (true)
		{
			auto it = pancakes.end() - 1;
			while (it > pancakes.begin() && *it == '+') --it;
			if (it == pancakes.begin() && *it == '+') break;
			else if (it == pancakes.begin())
			{
				++result;
				break;
			}
			++result;
			if (*pancakes.begin() == '+') while (*it != '+') --it;
			transform(pancakes.begin(), it + 1, pancakes.begin(), [](char c) { return (c == '+') ? '-' : '+'; });
			reverse(pancakes.begin(), it + 1);
		}
		output << "Case #" << n << ": " << result << endl;
	}

	return 0;
}

