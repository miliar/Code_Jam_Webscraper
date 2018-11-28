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
		for (int i = 0; i < line.size(); ++i)
		{
			char c;
			iss >> c;
			side.push_back(c == '+'? 1:-1);
		}
	};
	std::string solve()
	{
		int nbMove = 0;
		for (int i = side.size()-1; i >= 0; --i)
		{
			if (side[i] == -1)
			{
				int j = i -1;
				while (j >= 0 && side[j] == -1)
				{
					--j;
				}
				nbMove += flip(j,i);
			}
		}
		std::stringstream ss;
		ss << ' ' << nbMove;
		return ss.str();
	};

private:
	std::vector<int>side;
	int flip(int debut, int fin)
	{
		int nbMove =1;
		int i = 0;
		while (side[i] == 1)
		{
			side[i] = -1;
			++i;			
		}
		if (i > 0)
		{
			++nbMove;
		}
		std::vector<int> aux = side;
		for (int i = 0; i <= fin; i++)
		{
			side[i] = -aux[fin - i];
		}
		return nbMove;
	}

};




int main()
{
	std::ifstream file("C:\\Users\\Noob\\Downloads\\B-large.in");
	std::ofstream outputFile("C:\\Users\\Noob\\Downloads\\B-large.out");
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

