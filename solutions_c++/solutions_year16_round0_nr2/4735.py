#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int FindLowMinusIdx(vector<bool>& aPancake)
{
	int nIdx = 0;
	for (int i = 0; i < aPancake.size(); ++i) {
		if (!aPancake[i]) {
			nIdx = i;
			break;
		}
	}
	return nIdx;
}

void flip( vector<bool>& aPancake, int nIdx )
{
	for (int i = nIdx; i < aPancake.size(); ++i) {
		aPancake[i] = !aPancake[i];
	}	
}

bool IsAllPlus(vector<bool>& aPancake)
{
	bool bAllPlus = true;
	for (int i = 0; i < aPancake.size(); ++i) {
		if (!aPancake[i]) {
			bAllPlus = false;
			break;
		}
	}
	return bAllPlus;
}

int GetAllPlusCount(vector<bool>& aPancake)
{
	int nCount = 0;
	while (1) {
		if (IsAllPlus(aPancake)) {
			break;
		}
		int nFindLowMinusIdx = 0;
		nFindLowMinusIdx = FindLowMinusIdx(aPancake);

		flip(aPancake, nFindLowMinusIdx);
		nCount++;

		if (IsAllPlus(aPancake)) {
			break;
		}		
	}
	return nCount;
}

int main()
{
	fstream file;
	file.open("B-large.in");

	int nInputCount = 0;
	file >> nInputCount;
	vector<string> aStr;
	for (int nCase = 0; nCase < nInputCount; ++nCase) {
		string str;
		file >> str;
		aStr.push_back(str);
	}
	file.close();

	ofstream fileOut;
	fileOut.open("result2.txt", ios::out);

	for (int i = 0; i < aStr.size(); ++i) {
		string str = aStr[i];
		vector<bool> aPancake;
		for (int i = 0; i < str.size(); ++i) {
			bool bPlus = str[i] == '+';
			aPancake.insert(aPancake.begin(), bPlus);
		}
		int nCount = GetAllPlusCount(aPancake);

		fileOut << "Case #" << i + 1 << ": " << nCount << endl;;
	}
	fileOut.close();
}