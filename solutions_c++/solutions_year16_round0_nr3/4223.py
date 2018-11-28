#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#pragma warning(disable:4996)

typedef unsigned _int64 uint64;

void generateNextBinary(vector<uint64>& binaryVec, uint64 length)
{
	unsigned int binaryCount = binaryVec.size() - 2;
	for (; binaryCount > 0; --binaryCount)
	{
		if (binaryVec[binaryCount] == 0)
		{
			binaryVec[binaryCount] = 1;
			++binaryCount;
			while (binaryCount < binaryVec.size() - 1)
			{
				binaryVec[binaryCount] = 0;
				++binaryCount;
			}
			break;
		}
	}
}

uint64 powerOf(uint64 base, uint64 power)
{
	uint64 value = 1;
	while (power > 0)
	{
		value *= base;
		--power;
	}
	return value;
}

uint64 getOriginalValue(const vector<uint64>& binaryVec, uint64 base)
{
	uint64 originalValue = 0;
	unsigned int binaryCount = binaryVec.size();
	for (unsigned int i = 0; i < binaryCount; ++i)
	{
		originalValue += binaryVec[binaryCount - 1 - i] * powerOf(base, i);
	}
	return originalValue;
}

uint64 calculateNDValues(uint64 value)
{
	uint64 nDvalue = 2;
	uint64 lastFactor = value;
	for (; nDvalue < lastFactor; ++nDvalue)
	{
		if (value%nDvalue == 0)
			return nDvalue;

		lastFactor = value / nDvalue;
	}

	return 1;
}

bool checkWhetherJamCoinOrNot(const vector<uint64>& binaryVec, vector<uint64>& ndVec)
{
	for (unsigned int i = 2; i < 11; ++i)
	{
		uint64 nDValue = calculateNDValues(getOriginalValue(binaryVec, i));
		if (nDValue == 1)
			return false;
		ndVec[i-2] = nDValue;
	}
	return true;
}

void printBinaryVector(const vector<uint64>& binaryVec)
{
	for_each(begin(binaryVec), end(binaryVec), [](uint64 val){
		cout << val;
	});
}

void printNDVector(const vector<uint64>& ndVec)
{
	for_each(begin(ndVec), end(ndVec), [](uint64 val){
		cout << " " << val;
	});
	cout << endl;
}

int main()
{
	freopen("C:\\Users\\Dilum\\Desktop\\SingaJob\\GoogleCodeJam_2016\\Debug\\input.in", "r", stdin);
	freopen("C:\\Users\\Dilum\\Desktop\\SingaJob\\GoogleCodeJam_2016\\Debug\\output.txt", "w", stdout);

	uint64 xyt = 1000000000110011;

	uint64 testCases;
	cin >> testCases;
	uint64 caseNumber = 1;

	vector<uint64> ndVec(9, 1);
	ndVec.reserve(9);

	while (caseNumber <= testCases)
	{
		cout << "Case #" << caseNumber << ": "<< endl;

		unsigned int N, J;
		cin >> N;
		cin >> J;

		vector<uint64> binaryVec(N, 0);
		binaryVec.reserve(N);
		binaryVec[0] = 1;
		binaryVec[N - 1] = 1;

		uint64 coinCount = 0;
		bool jamCoin;
		
		jamCoin = checkWhetherJamCoinOrNot(binaryVec, ndVec);
		if (jamCoin)
		{
			printBinaryVector(binaryVec);
			printNDVector(ndVec);
			++coinCount;
		}

		while (coinCount < J)
		{
			generateNextBinary(binaryVec, N);
			jamCoin = checkWhetherJamCoinOrNot(binaryVec, ndVec);
			if (jamCoin)
			{
				printBinaryVector(binaryVec);
				printNDVector(ndVec);
				++coinCount;
			}
		}

		++caseNumber;
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}