#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
#include<functional>
using namespace std;

void recursive(int idx, int nSize, vector<string>& aTemp ) {

	string str;
	str.resize(nSize, '1');
	int nDigit = 1;

	for (int i = 0; i < nSize * nSize *nSize*nSize; i++) {

		bool bDone = next_permutation(str.begin() + 1, str.end() - 1);
		
		bool bExist = false;
		for (int i = 0; i < aTemp.size(); ++i) {
			if (aTemp[i] == str) {
				bExist = true;
				break;
			}
		}
		if (!bExist) {
			aTemp.push_back(str);
		}

		if (!bDone && nDigit < str.size() - 1 ) {
			str[nDigit++] = '0';
			sort(str.begin() + 1, str.end() - 1);
		}
	}
	sort(aTemp.begin(), aTemp.end());
}

int LowMinority(unsigned __int64 nNum ) {
	int nLastNum = 0;

	for (unsigned __int64 i = 2; i < nNum; ++i) {
		if (nNum % i == 0) {
			nLastNum = i;
		}

		if (i > 26 && nLastNum ) {
			break;
		}

		if (i > 100000000)
			break;
	}

	return nLastNum;
}

__int64 Pow(__int64 nNum, int nCount)
{
	unsigned __int64 nPow = 1;
	for (int i = 0; i < nCount; ++i) {
		nPow *= nNum;
	}
	return nPow;
}

__int64 GetJamNumber(string sInput, int nNum )
{
	int nCount = 0;
	unsigned __int64 nJamNumber = 0;
	int nStrIter = sInput.size();
	while (1) {
		int nCalcNum = sInput[--nStrIter] - '0';

		if (nCalcNum != 0) {
			nJamNumber += Pow(nNum, nCount);
		}

		if (nStrIter <= 0) {
			break;
		}
		nCount++;
	}
	// if (nJamNumber > 2000000000) return 0;
	// nJamNumber;// 
	__int64 nLowMinority = LowMinority(nJamNumber);
	return nLowMinority;
}

int main()
{
	int nNumberCount = 0;
	int nCount = 0;
	
	int nTotalCount = 0;

	fstream file;
	file.open("C-small-attempt2.in");

	file >> nTotalCount;

	vector<int> aNumberCount;
	vector<int> aCount;
	for (int jamCase = 0; jamCase < nTotalCount; ++jamCase) {
		file >> nNumberCount;
		file >> nCount;

		aNumberCount.push_back(nNumberCount);
		aCount.push_back(nCount);

	}
	file.close();
	ofstream fileOut;
	fileOut.open("result3.txt", ios::out);
	for (int jamCase = 0; jamCase < aNumberCount.size(); ++jamCase ) {

		nNumberCount = aNumberCount[ jamCase ];
		nCount = aCount[ jamCase ];

		vector<string> aNumberList;

		recursive(0, nNumberCount, aNumberList);

		vector<vector<__int64>> aaResult;
		vector<string> asResult;
		for (int nInputList = 0; nInputList < aNumberList.size(); ++nInputList) {

			vector<__int64> aRightNum;
			bool bAllRight = true;
			for (int i = 2; i <= 10; ++i) {
				__int64 nNum = GetJamNumber(aNumberList[nInputList], i);
				if (nNum == 0) {
					bAllRight = false;
					break;
				}
				aRightNum.push_back(nNum);
			}
			
			if (bAllRight) {
				aaResult.push_back(aRightNum);
				asResult.push_back(aNumberList[nInputList]);
			}
			if (aaResult.size() >= nCount)
				break;
		}

		fileOut << "Case #" << jamCase + 1 << ":" << endl;
		for (int i = 0; i < aaResult.size(); ++i) {
			fileOut << asResult[i];
			vector<__int64> aResult = aaResult[i];
			for (int k = 0; k < aResult.size(); ++k) {
				fileOut << " " << aResult[k] ;
			}
			fileOut << endl;
		}
		fileOut << endl;
	}
	fileOut.close();
}