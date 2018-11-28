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
		if (!(iss >> n)) 
		{ 
			throw; 
		}
	};
	std::string solve() const
	{
		std::vector<int> missingDigits;
		for (int digit = 0; digit < 10; ++digit)
		{
			missingDigits.push_back(digit);
		}
		bool isPossible = n!=0 ;
		int currentNumber = 0;
		while (isPossible && !missingDigits.empty())
		{
			currentNumber += n;
			int tempNumber = currentNumber;
			do {	
				missingDigits.erase(std::remove(missingDigits.begin(), missingDigits.end(), tempNumber % 10), missingDigits.end());
				tempNumber /= 10;
			} while (tempNumber > 0);
		}
		std::stringstream ss;
		if (isPossible)
		{
			ss << ' ' << currentNumber;
		}
		else
		{
			ss << ' ' <<"INSOMNIA";
		}
		return ss.str();
	};

private:
	int n;
	int resultat;

};




int main()
{
	std::ifstream file("C:\\Users\\Noob\\Downloads\\A-large.in");
	std::ofstream outputFile("C:\\Users\\Noob\\Downloads\\A-large.out");
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

