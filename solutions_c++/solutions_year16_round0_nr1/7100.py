// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <bitset>


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
	bitset<10> digits;
	for (int n = 1; n <= cases; ++n)
	{
		int number;
		input >> number;
		if (number == 0)
		{
			output << "Case #" << n << ": " << "INSOMNIA" << endl;
			continue;
		}

		digits.reset();
		int test;
		int i;
		for (i = 1; digits.all() == false; ++i)
		{
			result = test = number * i;
			while (test != 0)
			{
				digits.set(test % 10);
				test /= 10;
			}
		}
		output << "Case #" << n << ": " << result << endl;
	}

	return 0;
}

