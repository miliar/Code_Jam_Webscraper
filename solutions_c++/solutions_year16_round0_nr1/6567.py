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
		long long number = atol(line.c_str());
		int digitsFound = 0;
		int allDigitsArr[10] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
		string lastNumber = "";

		for(int i = 1; i <= 10000; i++)
		{
			if(number == 0.0)
			{
				lastNumber = "INSOMNIA";
				break;
			}
			else
			{
				string numberStr = ToString(number * i);
				lastNumber = numberStr;
				int numberStrLen = numberStr.length();

				for(int j = 0; j < numberStrLen; j++)
				{
					int digit = -1;
					string digitStr(1, numberStr[j]);
					if(!IsDigit(digitStr))
						continue;
					else
						digit = atoi(digitStr.c_str());

					if(digitsFound == 10)
					{
						break;
					}
					else if(allDigitsArr[digit] == -1)
					{
						digitsFound++;
						allDigitsArr[digit] = digit;
					}
				}
			}

			if(digitsFound == 10)
				break;
			else
				lastNumber = "INSOMNIA";
		}

		outputVec.push_back(lastNumber);
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
