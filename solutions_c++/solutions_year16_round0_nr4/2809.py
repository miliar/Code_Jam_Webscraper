// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

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
#include <bitset>

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

int main(int argc, char* argv[])
{
	cout << "primes" << endl;

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

#undef max


void SolveIt(int iCase, fstream& inputFile, ostream& output, ostream& error)
{
	int K, C, S;
	inputFile >> K;
	inputFile >> C;
	inputFile >> S;

	if (K != S)
		throw "??";

	for (int i = 1; i <= K; ++i)
		output << i << " ";

	output << endl;
}
