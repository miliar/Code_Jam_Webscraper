// CountingSheep.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>

using namespace std;

bool ReadInput(string& istrInputFile,  std::vector<int>& oVecNumber)
{
	bool bSuccess = false;

	string line;
	ifstream inputFile (istrInputFile);
	if (inputFile.is_open())
	{
		while ( getline (inputFile,line) )
		{
			int Num = stoi(line);
			oVecNumber.push_back(Num);
		}
		inputFile.close();
		bSuccess = true;
	}

	return bSuccess;
}

void populateDigits(long iNumber, std::list<int>& ioDigits)
{
	do{
		int digit = iNumber % 10;
		std::list<int>::const_iterator iter = std::find(ioDigits.begin(), ioDigits.end(), digit);
		if(iter == ioDigits.end())
			ioDigits.push_back(digit);
		iNumber /= 10;
	}
	while( iNumber > 0);
}

void ComputeLargestNumber(int i , int N, ofstream& outFile)
{
	string strNum;
	if(0 == N)
	{
		strNum = "INSOMNIA";
		outFile << "Case #" << i <<": " << "INSOMNIA" << endl;
	}
	else
	{
		bool bFind = true;
		int count =1;
		long largestNum = N;
		std::list<int> digits;
		while(bFind)
		{
			largestNum = count*N;
			populateDigits(largestNum, digits);
			digits.unique();
			int nDigits = (int)digits.size();
			if(nDigits ==10)
			{
				bFind = false;
				break;
			}
			else
			{
				count++;
			}
		}//while
		outFile << "Case #" << i <<": " << largestNum << endl;
	}//else
}

int _tmain(int argc, _TCHAR* argv[])
{
	string strInputFile;
	cout << "Enter input file path" <<endl;
	cin >>  strInputFile;

	std::vector<int> vecNumber;
	bool bRead = ReadInput(strInputFile, vecNumber);

	if(bRead)
	{
		ofstream outFile;
		outFile.open("CountingSheepOutput.txt");
		int nSize = (int)vecNumber.size();
		if(nSize > 0)
		{
			int T = vecNumber[0];
			for (int i = 1; i < nSize; i++)
			{
				 ComputeLargestNumber(i, vecNumber[i], outFile);
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

