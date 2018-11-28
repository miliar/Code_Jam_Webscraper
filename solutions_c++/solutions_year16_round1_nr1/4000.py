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
		int len = line.length();
		string word = "";
		string lastWord = "";
		char last = line[0];

		for(int i = 0; i < len; i++)
		{
			string temp = "";
			temp += line[i];

			if(line[i] >= last)
			{
				word.insert(0,temp);
				last = line[i];
			}
			else
			{
				word += temp;
			}
		}

		outputVec.push_back(word);
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
