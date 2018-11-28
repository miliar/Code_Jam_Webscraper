/*
 * Main.cpp
 *
 *  Created on: Feb 23, 2016
 *      Author: dillip
 */
#include "Utils.h"

void WriteOutput(ofstream& outputFileStream, vector<string>& outputVec)
{
	int totalCase = outputVec.size();

	for(int i = 0; i < totalCase; i++)
	{
		outputFileStream << "Case #" << i+1 << ": " << outputVec[i] << endl;
	}
}

void Engine(ifstream& inputFileStream, vector<string>& outputVec)
{
	string line = "";

	getline(inputFileStream, line); //total no. of test case 1st line.

	while(getline(inputFileStream, line))
	{
		int totalFlips = 0;
		int totalChars = line.length();
		if(totalChars < 1)
			continue;
		char prev = line[0];
		char firstChar = prev;
		char curr = NULL;
		int plusCount = 0;
		int minusCount = 0;

		if(prev == '+')
			plusCount = 1;
		else
			minusCount = 1;
		for(int i = 1; i < totalChars; i++)
		{
			curr = line[i];

			if(curr != prev && curr == '+')
			{
				prev = curr;
				plusCount++;
			}
			else if(curr != prev && curr == '-')
			{
				prev = curr;
				minusCount++;
			}
		}

		totalChars = plusCount + minusCount;
		if(totalChars % 2 != 0)
		{
			if(plusCount > minusCount)
				totalFlips = 2 * plusCount - 2;
			else
				totalFlips = 2 * minusCount - 1;
		}
		else
		{
			if(plusCount % 2 == 0 && firstChar == '+')
				totalFlips = 2 * plusCount;
			else if(plusCount % 2 == 0 && firstChar == '-')
				totalFlips = 2 * minusCount - 1;
			else if(plusCount % 2 != 0 && firstChar == '+')
				totalFlips = 2 * plusCount;
			else if(plusCount % 2 != 0 && firstChar == '-')
				totalFlips = 2 * minusCount - 1;
		}

		outputVec.push_back(ToString(totalFlips));
	}
}

int main(int argc, char* argv[])
{
	if(argc != 3)
	{
		cout << "invalid arguments, it should be like - \"executable inputFullFilePath outputFullFilePath\"" << endl;
		return 0;
	}

	string inputFile = argv[1];
	string outputFile = argv[2];

	vector<string> outputVec;

	ifstream inputFileStream(inputFile.c_str());
	ofstream outputFileStream(outputFile.c_str());

	Engine(inputFileStream, outputVec);
	WriteOutput(outputFileStream, outputVec);

	//Close files
	inputFileStream.close();
	outputFileStream.close();

	return 0;
}
