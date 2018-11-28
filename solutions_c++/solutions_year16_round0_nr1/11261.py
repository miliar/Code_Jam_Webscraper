// CountingSheep.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <string>


int processInputString(std::string inputString);

int main(int nNumberofArgs, char* pszArgs[])
{
	std::cout << nNumberofArgs << std::endl;

	std::ifstream myReadFile;
	std::ofstream myWriteFile;
	myWriteFile.open("sheep.txt");
	if (!myWriteFile.is_open())
		std::cout << "fail to open file";

	std::cout << pszArgs[1] << std::endl;

	myReadFile.open(pszArgs[1]);
	char output[100];
	std::string str;
	int inputCount;

	if (myReadFile.is_open()) 
	{
		std::getline(myReadFile, str);	//nombre d'input
		inputCount = std::atoi(str.c_str());

		int lineCount = 1;
		while (!myReadFile.eof() && lineCount<=inputCount) 
		{
			std::getline(myReadFile, str);			

			int processedValue = processInputString(str);

			std::cout << "Case #" << lineCount << ": ";
			myWriteFile << "Case #" << lineCount << ": ";

			if (processedValue == -1) 
			{
				std::cout << "INSOMNIA" << std::endl;
				myWriteFile << "INSOMNIA" << std::endl;
			}
			else
			{
				std::cout << processedValue << std::endl;
				myWriteFile << processedValue << std::endl;
			}

			lineCount++;
		}
	}
	myReadFile.close();
	myWriteFile.close();
	while (1);

    return 0;
}

int processInputString(std::string inputString)
{
	int inputInt = std::atoi(inputString.c_str());
	int currentInt = inputInt;
	std::string currentString = inputString;
	bool digitFound[10] = { false };
	bool allDigitFound = false;
	bool insomnia = false;
	int sheepCount = 1;

	if (inputInt == 0)
		return -1;

	while (!allDigitFound && !insomnia)
	{		

		//pour chaque digit de l'input
		for (int i = 0; i < currentString.length();i++)
		{
			//on passe le digitFound corespondant a true
			char currentChar = currentString.at(i);
			//std::cout << (int)currentChar - 48 << std::endl;
			digitFound[(int)currentChar - 48] = true;			
		}
		
		//on recalcule allDigitFound
		allDigitFound = true;
		for (int i = 0; i < 10; i++)
		{
			if (!digitFound[i])
			{
				allDigitFound = false;
				break;
			}
		}

		if (allDigitFound) {
			//std::cout << "Output: " << currentInt << std::endl;
			return currentInt;
		}

		if(sheepCount > 100)
		{
			std::cout << "insomnia?" << std::endl;
			
			for (int i = 0; i < 10; i++)
				std::cout << digitFound[i];
			std::cout << std::endl;
			return -1;
		}

		/*
		std::cout << "dealt with: " << currentInt << " " << currentString << " /";
		for (int i = 0; i < 10; i++)
			std::cout << digitFound[i];
		std::cout << std::endl;
		*/

		sheepCount++;
		currentInt = sheepCount * inputInt;
		currentString = std::to_string(currentInt);
	}
}

