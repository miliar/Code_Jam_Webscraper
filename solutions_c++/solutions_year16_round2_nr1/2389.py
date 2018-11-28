// digits.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
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

	string result;
	string word;
	for (int n = 1; n <= cases; ++n)
	{
		result = "";
		input >> word;
		while (word.length() != 0)
		{
			if (word.find('Z') != string::npos)
			{
				word.erase(word.find('Z'), 1);
				word.erase(word.find('E'), 1);
				word.erase(word.find('R'), 1);
				word.erase(word.find('O'), 1);
				result += "0";
				continue;
			}
			if (word.find('W') != string::npos)
			{
				word.erase(word.find('T'), 1);
				word.erase(word.find('W'), 1);
				word.erase(word.find('O'), 1);
				result += "2";
				continue;
			}
			if (word.find('U') != string::npos)
			{
				word.erase(word.find('F'), 1);
				word.erase(word.find('O'), 1);
				word.erase(word.find('U'), 1);
				word.erase(word.find('R'), 1);
				result += "4";
				continue;
			}
			if (word.find('X') != string::npos)
			{
				word.erase(word.find('S'), 1);
				word.erase(word.find('I'), 1);
				word.erase(word.find('X'), 1);
				result += "6";
				continue;
			}
			if (word.find('G') != string::npos)
			{
				word.erase(word.find('E'), 1);
				word.erase(word.find('I'), 1);
				word.erase(word.find('G'), 1);
				word.erase(word.find('H'), 1);
				word.erase(word.find('T'), 1);
				result += "8";
				continue;
			}
			if (word.find('O') != string::npos)
			{
				word.erase(word.find('O'), 1);
				word.erase(word.find('N'), 1);
				word.erase(word.find('E'), 1);
				result += "1";
				continue;
			}
			if (word.find('S') != string::npos)
			{
				word.erase(word.find('S'), 1);
				word.erase(word.find('E'), 1);
				word.erase(word.find('V'), 1);
				word.erase(word.find('E'), 1);
				word.erase(word.find('N'), 1);
				result += "7";
				continue;
			}
			if (word.find('N') != string::npos)
			{
				word.erase(word.find('N'), 1);
				word.erase(word.find('I'), 1);
				word.erase(word.find('N'), 1);
				word.erase(word.find('E'), 1);
				result += "9";
				continue;
			}
			if (word.find('F') != string::npos)
			{
				word.erase(word.find('F'), 1);
				word.erase(word.find('I'), 1);
				word.erase(word.find('V'), 1);
				word.erase(word.find('E'), 1);
				result += "5";
				continue;
			}
			if (word.find('T') != string::npos)
			{
				word.erase(word.find('T'), 1);
				word.erase(word.find('H'), 1);
				word.erase(word.find('R'), 1);
				word.erase(word.find('E'), 1);
				word.erase(word.find('E'), 1);
				result += "3";
				continue;
			}
		}
		sort(result.begin(), result.end());

		output << "Case #" << n << ": " << result << endl;
	}

	return 0;
}

