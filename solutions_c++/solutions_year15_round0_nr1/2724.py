// AStandingOvation.cpp : Defines the entry point for the console application.
//

#include "tchar.h"
#include<iostream>
#include<fstream>
#include<vector>
#include <cassert>
#include<string>
#include <sstream>

int NumberNewPeopleRequired(const std::vector<int>& shynessLevels, int& currentShyness, int& NumbStanding)
{
	assert(currentShyness<shynessLevels.size()-1);

	int NumbAtCurrLevel = shynessLevels[currentShyness];
	assert(NumbStanding >= currentShyness);
	NumbStanding += NumbAtCurrLevel;
	//int numbAtNextLevel = shynessLevels[currentShyness+1];
	int NumbNewPeopleRequired = currentShyness+1 - NumbStanding;
	if (NumbNewPeopleRequired < 0)
	{
		NumbNewPeopleRequired = 0;
	}

	NumbStanding += NumbNewPeopleRequired;
	currentShyness++;
	return NumbNewPeopleRequired;

}

int TotalNewRequired(const int nMaxShyness, const std::vector<int>& shynessLevels)
{

	int currentShyness = 0;
	int NumbStanding = 0;
	int TotalNumberNewRequired = 0;
	while (currentShyness < nMaxShyness)
	{
		TotalNumberNewRequired += NumberNewPeopleRequired(shynessLevels, currentShyness, NumbStanding);
	}
	return TotalNumberNewRequired;
}

std::vector<int> ConvertSpacedInts(std::string& line)
{
	std::vector<int> integers;
	std::istringstream iss(line);
	int n;
	while (iss >> n)
	{
		integers.push_back(n);
	}
	return integers;
}



std::vector<int> ConvertInts(std::string& line)
{
	std::vector<int> integers;

	std::istringstream iss(line);
	int n;

	iss >> n;
	integers.push_back(n);
	std::string nextbit;
	iss >> nextbit;

	char buffer;
	const char *p = nextbit.c_str();
		while (*p != '\0')
		{
			if (*p == ' ')
			{
				p++;
			}
			buffer = *p++;
			int numb = buffer-'0';
			integers.push_back(numb);
		}
			
		return integers;

}

int SolveCase(std::vector<int> Case)
{
	const int nMaxShyness = Case[0];
	std::vector<int> shynessLevels(Case.begin()+1, Case.end());
	return TotalNewRequired(nMaxShyness, shynessLevels);
}

int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream file("A-large.in");
	std::string line;
	std::getline(file, line);
	int nNumbCases = ConvertInts(line)[0];
	std::vector < std::vector<int>> cases;
	int nCount = 0;

	std::vector<int> solutions;
	while (nCount<nNumbCases)
	{
		std::getline(file, line);
		cases.push_back(ConvertInts(line));
		nCount++;
	}
	assert(nNumbCases = cases.size());
	/*
	for (int i = 0; i < nNumbCases; i++)
	{
		std::cout << "Case #" << (i + 1) << ": " << SolveCase(cases[i]) << std::endl;
	}
	*/
	std::ofstream output_test("output_large.txt");

	for (int i = 0; i < nNumbCases; i++)
	{
		output_test << "Case #" << (i + 1) << ": " << SolveCase(cases[i]) << std::endl;
	}

	


	return 0;
}

