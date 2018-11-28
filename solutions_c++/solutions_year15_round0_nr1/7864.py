// ConsoleApplication1.cpp : main project file.

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// Split functions taken from:
// http://stackoverflow.com/questions/236129/split-a-string-in-c
std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
	std::stringstream ss(s);
	std::string item;
	while (std::getline(ss, item, delim)) {
		elems.push_back(item);
	}
	return elems;
}

std::vector<std::string> split(const std::string &s, char delim) {
	std::vector<std::string> elems;
	split(s, delim, elems);
	return elems;
}

int Solve(string line)
{
	std::vector<std::string> x = split(line, ' ');

	int maxShyness = atoi(x.at(0).c_str());
	string audience = x.at(1);

	int reqPpl = 0;


	int requiredShynessLevel = audience.size() - 1;
	int pplAttending = 0;
	int pplStanding = 0;
	int curShynessLevel = 0;
	for (int i = 0; i < audience.size(); i++)
	{
		if ((audience.at(i) - '0') > 0)
		{
			pplAttending += audience.at(i) - '0';
		}

		if (pplStanding >= i)
		{
			if ((audience.at(i) - '0') > 0)
			{
				pplStanding += audience.at(i) - '0';
			}			
		}
		else if ((audience.at(i) - '0') > 0)
		{
			reqPpl += i - pplStanding;
			pplStanding += audience.at(i) - '0' + (i - pplStanding);
		}
		curShynessLevel = i * (audience.at(i) - '0');		
	}

	
	return reqPpl;
}

int main(array<System::String ^> ^args)
{
	string line;
	ifstream input("input.txt");
	ofstream output;
	output.open("output.txt");

	int caseNumber = 1;
	int testCases = 0;
	string caseLabel = "Case #";

	if (input.is_open())
	{
		while (getline(input, line))
		{
			if (testCases == 0)
			{
				testCases = atoi(line.c_str());
			}
			else
			{
				output << caseLabel << caseNumber << ": " << Solve(line) << '\n';
				caseNumber++;
			}
		}
		input.close();
	}
	output.close();

	return 0;
}


