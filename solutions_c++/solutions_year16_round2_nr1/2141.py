// CodeJamTemplate.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <sstream>
#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

class MyInput
{
public:
	MyInput(std::ifstream &file)
	{
		//get firstLine of the testCase
		//std::string line;
		std::getline(file, m_inputString);
		/*
		std::istringstream iss(line);
		iss >> n;
		std::getline(file, line);
		std::istringstream iss2(line);
		for (int i = 0; i < n; ++i)
		{
			int bff;
			iss2 >> bff;
			bffs.push_back(bff);
		}
		*/
	};
	std::string solve()
	{
		int nbZ = 0, nbW = 0, nbU = 0, nbX = 0, nbG = 0, nbH = 0, nbF = 0, nbS = 0, nbI = 0,nbO = 0;
		for (int i = 0; i < m_inputString.size(); ++i)
		{
			switch (m_inputString[i])
			{
			case 'Z':
				nbZ++;
				break;
			case 'W':
				nbW++;
				break;
			case 'U':
				nbU++;
				break;
			case 'X':
				nbX++;
				break;
			case 'G':
				nbG++;
				break;
			case 'H':
				nbH++;
				break;
			case 'F':
				nbF++;
				break;
			case 'S':
				nbS++;
				break;
			case 'I':
				nbI++;
				break;
			case 'O':
				nbO++;
				break;
			}
		}
		int nbZero = nbZ;
		int nbTwo = nbW;
		int nbFour = nbU;
		int nbSix = nbX;
		int nbEight = nbG;
		int nbThree = nbH - nbEight;
		int nbFive = nbF - nbFour;
		int nbSeven = nbS - nbSix;
		int nbOne = nbO - nbZero - nbTwo - nbFour;
		int nbNine = nbI - nbFive - nbSix - nbEight;



		std::stringstream ss;
		ss << ' ';
		for (int i = 0; i < nbZero; ++i)
		{
			ss << '0';
		}
		for (int i = 0; i < nbOne; ++i)
		{
			ss << '1';
		}
		for (int i = 0; i < nbTwo; ++i)
		{
			ss << '2';
		}
		for (int i = 0; i < nbThree; ++i)
		{
			ss << '3';
		}
		for (int i = 0; i < nbFour; ++i)
		{
			ss << '4';
		}
		for (int i = 0; i < nbFive; ++i)
		{
			ss << '5';
		}
		for (int i = 0; i < nbSix; ++i)
		{
			ss << '6';
		}
		for (int i = 0; i < nbSeven; ++i)
		{
			ss << '7';
		}
		for (int i = 0; i < nbEight; ++i)
		{
			ss << '8';
		}
		for (int i = 0; i < nbNine; ++i)
		{
			ss << '9';
		}
		return ss.str();

	};


private:
	std::string m_inputString;

};




int main()
{
	std::ifstream file("C:\\Users\\Noob\\Downloads\\A-large.in");
	std::ofstream outputFile("C:\\Users\\Noob\\Downloads\\output.txt");
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

