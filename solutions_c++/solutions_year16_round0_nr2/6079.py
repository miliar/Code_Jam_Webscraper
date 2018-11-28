// RevengeOfThePanCakes.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool ReadInput(string& istrInputFile, std::vector<string>& oInputs)
{
	bool bSuccess = false;

	string line;
	ifstream inputFile (istrInputFile);
	if (inputFile.is_open())
	{
		while ( getline (inputFile,line) )
		{
			oInputs.push_back(line);
		}
		inputFile.close();
		bSuccess = true;
	}

	return bSuccess;
}

int ChangePos(string& strInput)
{
	int nPos = -1;
	int nSize = (int)strInput.length();
	for (int j= 0; j < nSize -1; j++)
	{
		if(strInput[j] == strInput[j+1])
			continue;
		else
		{
			nPos = j;
			break;
		}
	}

	return nPos;
}

bool IsHappy(string& strInput)
{
	bool bHappy = false;
	int nSize = (int)strInput.size();
	if(nSize > 0)
	{
		if(strInput[0] == '+')
			bHappy = true;
	}

	return bHappy;
}

void FlipPancakes(int nPos, string& ioStrInput)
{
	string tempString = ioStrInput;
	for(int i = 0; i < nPos + 1; i++)
	{
		if(tempString[i] == '+')
			tempString[i] = '-';
		else
			tempString[i] = '+';
	}

	for(int i = 0; i < nPos + 1; i++)
	{
		ioStrInput[i] = tempString[nPos - i];
	}
}

void ComputeMinFlips(int i ,  string& input, ofstream& outFile)
{
	int nFlips = 0;
	string tempString = input;
	bool bContinueFlips = true;

	while(bContinueFlips)
	{
		int nPos = ChangePos(tempString);
		if(-1 == nPos)
		{
			bool bHappy = IsHappy(tempString);
			if(false == bHappy)
			{
				nFlips = nFlips + 1;
			}
			bContinueFlips = false;
			break;
		}
		else
		{
			FlipPancakes(nPos, tempString);
			nFlips = nFlips + 1;
		}
	}

	outFile << "Case #" << i <<": " << nFlips << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	string strInputFile;
	cout << "Enter input file path" <<endl;
	cin >>  strInputFile;

	std::vector<string> vecInputs;
	bool bRead = ReadInput(strInputFile, vecInputs);

	if(bRead)
	{
		ofstream outFile;
		outFile.open("RevengeOfThePanCakesOutput.txt");
		int nSize = (int)vecInputs.size();
		if(nSize > 0)
		{
			int T = stoi(vecInputs[0]);
			for (int i = 1; i < nSize; i++)
			{
				 ComputeMinFlips(i, vecInputs[i], outFile);
			}
		}
		outFile.close();
	}
   else
   {
	   cout << "Failed to read input file"; 
   }

	return 0;
}

