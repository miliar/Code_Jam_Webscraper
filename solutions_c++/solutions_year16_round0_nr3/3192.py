// CodeJamTemplate.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <sstream>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>


static std::vector<long long> maxSqrtValue;

static std::vector<long long> primeNumbers;

static long long maxPrimeNumber = 5* pow(10,7);

void initPrimeNumbers()
{
	primeNumbers = { 2,	3,	5,	7,	11,	13,	17,	19,	23,	29
		,31,	37	,41, 43,	47,	53,	59,	61,	67,	71
		,73,	79	,83	,89,97,	101	,103,107,109,113
		,127,	131	,137,139,149,151,157,163,167,173
		,179,	181	,191,193,197,199,211,223,227,229
		,233,	239	,241,251,257,263,269,271,277,281
		,283,	293	,307,311,313,317,331,337,347,349
		,353,	359	,367,373,379,383,389,397,401,409
		,419,	421	,431,433,439,443,449,457,461,463
		,467,	479	,487,491,499,503,509,521,523,541
		,547,	557	,563,569,571,577,587,593,599,601
		,607,	613	,617,619,631,641,643,647,653,659
		,661,	673	,677,683,691,701,709,719,727,733
		,739,	743	,751,757,761,769,773,787,797,809
		,811,	821	,823,827,829,839,853,857,859,863
		,877,	881	,883,887,907,911,919,929,937,941
		,947,	953	,967,971,977,983,991,997,1009,1013
		,1019,	1021 ,1031,	1033,1039,1049,1051,1061,1063,1069
		,1087,	1091 ,1093	,1097,1103,1109,1117,1123,1129,1151
		,1153,	1163 ,1171	,1181,1187,1193,1201,1213,1217,1223 };
}

bool isPrime(long long number)
{
	for (auto it = primeNumbers.begin(); it < primeNumbers.end(); ++it)
	{
		if (number%*it == 0)
		{
			return false;
		}
		if ((*it) * (*it) > number)
		{
			return true;
		}
	}
}

long long pow(int i, int power)
{
	return power == 0? 1: i*pow(i, power - 1);
}


long long translateToBase(const std::vector<int> &digits, int base)
{
	long long number = 0;
	for (int i = digits.size()-1, currentRank = 0; i >= 0; --i, ++currentRank)
	{
		if (digits[i] != 0)
		{
			number += pow(base, currentRank);
		}
	}
	return number;
}


long long getMaxNumber(int base, int size)
{
	if (maxSqrtValue[base] == 0)
	{
		std::vector<int> maxDigitsValue;
		for (int i = 0; i < size; i++)
		{
			maxDigitsValue.push_back(1);
		}
		maxSqrtValue[base] = std::sqrt(translateToBase(maxDigitsValue, base));
	}
	return maxSqrtValue[base];
}

bool addNbPrimeNumbers(int nbMax)
{
	bool morePrimeNumberToAdd = true;
	long long currentNumber = primeNumbers.back();
	while (currentNumber < nbMax)
	{
		currentNumber++;
		if (isPrime(currentNumber))
		{
			primeNumbers.push_back(currentNumber);
		}
	}
	if (nbMax == maxPrimeNumber)
	{
		primeNumbers.push_back(maxPrimeNumber);
		morePrimeNumberToAdd = false;
	}
	return morePrimeNumberToAdd;
}



int getDivisor(long long transformedNumber)
{
	int i = 0;
	bool morePrimeNumberToAdd = true;
	while (morePrimeNumberToAdd && primeNumbers[i]* primeNumbers[i]< transformedNumber)
	{
		if (transformedNumber%primeNumbers[i] == 0)
		{
			return primeNumbers[i];
		}
		else if (i == primeNumbers.size() -1 && morePrimeNumberToAdd)
		{
			morePrimeNumberToAdd = addNbPrimeNumbers(std::min(maxPrimeNumber, 2*primeNumbers[i]));
		}
		i++;
	}
	return 0;
}


class MyInput
{
public:
	MyInput(std::ifstream &file)
	{
		//get firstLine of the testCase
		std::string line;
		std::getline(file, line);
		std::istringstream iss(line);
		iss >> size;
		iss >> numberToProduce;
		//iss >> numberToProduce;
		for (int i = 0; i < size; i++)
		{
			currentCoinJam.push_back(0);
			maxSqrtValue.push_back(0);
		}
		currentCoinJam[0] = 1;
		currentCoinJam[size -1] = 1;
		initPrimeNumbers();

	};
	std::string solve()
	{
		std::stringstream ss;
		int nbCoinFound = 0;
		while (nbCoinFound < numberToProduce)
		{
			bool coinJamFound = false;
			std::stringstream temp;
			for (int i = 0; i < size; i++)
			{
				temp <<currentCoinJam[i];
			}
			for (int i = 2; i <= 10; ++i)
			{
				long long transformedNumber = translateToBase(currentCoinJam, i);
				int divisor = getDivisor(transformedNumber);
				if (divisor == 0)
				{
					break;
				}
				temp << ' '<< divisor;
				if (i == 10)
				{
					coinJamFound = true;
					ss << ' '<< temp.str()<<"\n";
					++nbCoinFound;
				}

			}
			getNextCodeJam();
		}

		return ss.str();
	};

private:
	std::vector<int>currentCoinJam;
	int size, numberToProduce;

	void getNextCodeJam()
	{
		int i = size-2;
		while (currentCoinJam[i] != 0)
		{
			currentCoinJam[i] = 0;
			--i;
		}
		currentCoinJam[i] = 1;
	}

};




int main()
{
	std::ifstream file("C:\\Users\\Noob\\Downloads\\C-small-attempt0.in");
	std::ofstream outputFile("C:\\Users\\Noob\\Downloads\\C-large-attempt2.out");
	std::string line;
	int nbCases = 0;
	std::getline(file, line);
	std::istringstream iss(line);
	iss >> nbCases;
	for (int i = 0; i < nbCases; ++i)
	{
		MyInput myInput(file);
		outputFile << "Case #" << i+1 << ":\n"<<myInput.solve() << std::endl;
	}
	file.close();
	outputFile.close();
    return 0;
}

