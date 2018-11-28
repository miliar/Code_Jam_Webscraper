// CodeJamTemplate.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <sstream>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

class MyInput
{
public:
	MyInput(std::ifstream &file)
	{
		//get firstLine of the testCase
		std::string line;
		std::getline(file, line);
		std::istringstream iss(line);
		iss >> originalSequenceLength;
		iss >> complexity;
		iss >> nbStudents;
	};
	std::string solve()
	{
		bool isPossible = false; 
		std::stringstream ss;
		if (complexity == 1)
		{
			isPossible = nbStudents == originalSequenceLength;
			if (!isPossible)
			{
				return std::string(" IMPOSSIBLE");
			}
			for (int i = 0; i < nbStudents; ++i)
			{
				ss << ' '<< i + 1;
			}
		}
		else
		{
			bool isOdd = originalSequenceLength % 2 != 0;
			isPossible = nbStudents >= (originalSequenceLength+1) / 2 ;
			if (!isPossible)
			{
				return std::string(" IMPOSSIBLE");
			}
			for (int i = 0; i < nbStudents && i<originalSequenceLength/2; ++i)
			{
				ss << ' ' << 2 + 2 *i * (originalSequenceLength +1);
			}
			if (isOdd)
			{
				ss << ' ' << originalSequenceLength;
			}
		}
		return ss.str();
	};

private:
	int originalSequenceLength, complexity , nbStudents;

};




int main()
{
	std::ifstream file("C:\\Users\\Noob\\Downloads\\D-small-attempt0.in");
	std::ofstream outputFile("C:\\Users\\Noob\\Downloads\\D-small-attempt0.out");
	std::string line;
	int nbCases = 0;
	std::getline(file, line);
	std::istringstream iss(line);
	iss >> nbCases;
	for (int i = 0; i < nbCases; ++i)
	{
		MyInput myInput(file);
		outputFile << "Case #" << i+1 << ":"<<myInput.solve() << std::endl;
	}
	file.close();
	outputFile.close();
    return 0;
}

