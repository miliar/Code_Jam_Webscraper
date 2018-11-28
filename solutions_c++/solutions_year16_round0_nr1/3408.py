// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <iomanip>
#include <algorithm>
#include <list>
#include <set>
#include <unordered_set>
#include <utility>
#include <tuple>
#include <limits>

using namespace std;

static const bool bConsoleOut = false;

void SolveIt(int iRound, fstream& inputFile, ostream& output, ostream& error);

string ReadString(fstream& input, bool bIsEOL = false)
{
	string line;
	if (bIsEOL)
		getline(input, line);
	else
		getline(input, line, ' ');

	return line;
}

int ReadInt(fstream& input, bool bIsEOL = false)
{
	return atoi(ReadString(input, bIsEOL).c_str());
}

double ReadDouble(fstream& input, bool bIsEOL = false)
{
	return atof(ReadString(input, bIsEOL).c_str());
}

int _tmain(int argc, _TCHAR* argv[])
{
	fstream inputFile;
	fstream outputFile;

	ostream& output = bConsoleOut ? cout : outputFile;
	ostream& error = cerr;
	if (!bConsoleOut)
	{
		outputFile.open("..\\output.txt", ios::out);
		if (!outputFile.is_open())
		{
			cout << "Meh!";
			return 1;
		}
	}

	inputFile.open(argv[1]);

	if (!inputFile.is_open())
	{
		cout << "Meh!";
		return 1;
	}

	string sLine;
	getline(inputFile, sLine);
	int nCases = atoi(sLine.c_str());

	output << std::setprecision(16);

	for (int iCase = 0 ; iCase < nCases; iCase++)
	{
		output << "Case #" << (iCase + 1) << ": ";
		SolveIt(iCase + 1, inputFile, output, error);
	}

	if (!bConsoleOut)
		outputFile.close();

	if (bConsoleOut)
	{
		cout << endl << "Done...";
		cin.get();
	}

	return 0;
}

void collect_digits(std::set<int>& digits, unsigned long num)
{
	if (num > 9)
	{
		collect_digits(digits, num / 10);
	}
	digits.insert(num % 10);
}
#undef max
void SolveIt(int iCase, fstream& inputFile, ostream& output, ostream& error)
{
	unsigned long N;
	inputFile >> N; // ReadInt(inputFile, true);

	if (N == 0)
	{
		output << "INSOMNIA" << endl;
		return;
	}

	set<int> numbersSeen;
	unsigned long i = N;
	int iters = 0;
	while (true)
	{
		// decompose i
		//stringstream ss;
		//ss << i;
		//string s = ss.str();
		//for (char c : s)
		//	numbersSeen.insert(c - '0');
		
		collect_digits(numbersSeen, i);
		
		if (numbersSeen.size() == 10)
		{
			output << i << endl;
			return;
		}

		// stop condition
		if (/*++iters > 100000 ||*/ i >= std::numeric_limits<unsigned long>::max() - N)
			break;

		i += N;
	}
	output << "INSOMNIA" << endl;
}
