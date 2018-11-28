// CoinJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include<string>

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

void ComputeNumbers(int N, std::vector<string>& oTestNumbers)
{
	//generate first test number 10...01
	string strNumber = "1";
	for (int i = 1; i < N-1; i++)
	{
		strNumber.append("0");
	}
	strNumber.append("1");
	oTestNumbers.push_back(strNumber);
	
	for (int j = 1; j <  N-1; j++)////replace  jth digit with 0 & 1 for every test number
	{
		int nNumbers = (int)oTestNumbers.size();
		for (int k = 0; k < nNumbers; k++)
		{
			 string testString = oTestNumbers[k];
			 
			 string str1 = testString;
			 str1[j] = '0';
			 
			 std::vector<string>::iterator iter1 = std::find(oTestNumbers.begin(), oTestNumbers.end(), str1);
			  if(iter1 == oTestNumbers.end())
			  {
				  oTestNumbers.push_back(str1);
			  }
			  
			 string str2 = testString;
			  str2[j] = '1';
			
			  std::vector<string>::iterator iter2 = std::find(oTestNumbers.begin(), oTestNumbers.end(), str2);
			  if(iter2 == oTestNumbers.end())
			  {
				  oTestNumbers.push_back(str2);
			  }
		}
	}
}

unsigned long long int ComputeBaseNumber(string& iStrNumber, int b)
{
	unsigned long long int baseNumber = 0;
	int nSize = (int)  iStrNumber.length();

	for (int i = 0; i < nSize; i++)
	{
		char arr[] = "C";
        arr[0] = iStrNumber[i];
		int digit = atoi(arr);
	    baseNumber = baseNumber + (digit * (pow(b, (nSize-1-i))));
	}
	return baseNumber;
}

bool  CheckPrime(unsigned long long int& Num, unsigned long long int& divisor)
{/*
	bool bPrime = true;
	for(unsigned long long int i=2;i<=Num/2;++i)
	{
		if(Num%i == 0)
		{
			divisor = i;
			bPrime=false;
			break;
		}
	}

	return bPrime;*/

	if((Num==2)||(Num==3)) return true;

  if(Num %3 == 0) 
  {
	  divisor = 3;
	  return false;
  }

  unsigned long long int limit = (unsigned long long int )sqrt((Num));
  for(unsigned long long int i=4; i<= limit ; i++)
  {
      if( Num % i==0) 
	  {
		  divisor = i;
		  return false;
	  }
  }

  return true;
}

void TestCoinJam(int i, int J, std::vector<string>& TestNumbers,ofstream& outFile)
{
	int nJamCoins = 0;
	int nSize =(int) TestNumbers.size();
	for (int i = 0; i < nSize; i++)
	{
		if(nJamCoins >= J)
			break;

		string strNumber = TestNumbers[i];
		bool bValid = true;
		std::vector<unsigned long long int> divisors;
		for (int j = 2; j < 11; j++)
		{
			unsigned long long int baseNum = ComputeBaseNumber(strNumber, j);
			unsigned long long int divisor = 0;
			bool bPrime = CheckPrime(baseNum, divisor);
			if(bPrime)
			{
				bValid = false;
				break;
			}
			else
			{
				divisors.push_back(divisor);
			}
		}//j
		if(bValid)
		{
			nJamCoins++;
			outFile<<strNumber<< "\t" << divisors[0] << "\t" <<divisors[1] << "\t" <<divisors[2] << "\t" <<divisors[3] << "\t" <<divisors[4] << "\t" <<divisors[5] << "\t" <<divisors[6] << "\t" <<divisors[7] << "\t" <<divisors[8] << "\t" <<endl;
		}
	}//i
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
		int nSize = (int)vecInputs.size();
		if(nSize > 0)
		{
			int T = stoi(vecInputs[0]);

			ofstream outFile;
			outFile.open("CoinJamOutput.txt");
			for (int i = 1; i < nSize; i++)
			{
				string input = vecInputs[i];
				std::size_t pos = input.find(" ");
				string strN = input.substr (0,pos);
				string strJ = input.substr (pos+1);
				
				int N = stoi(strN);
				int J = stoi(strJ);
				std::vector<string> TestNumbers;
				ComputeNumbers(N, TestNumbers); 
				outFile<< "Case #"<<i<<":"<<endl;
				TestCoinJam(i, J, TestNumbers,outFile);
			}
			outFile.close();
		}
	}
   else
   {
	   cout << "Failed to read input file"; 
   }

	

	return 0;
}

