#include <iostream>
#include <vector>
#include <fstream>
#include <string>
using namespace std;
const int nMaxCount = 1000000;
bool aCheckNum[10] = { 0, };

bool IsAllRightNum(int nNum)
{
	while (1) {
		int nCheckNum = nNum % 10;
		aCheckNum[nCheckNum] = 1;
		nNum /= 10;
		if (nNum == 0)
			break;
	}
	bool bAllRight = true;

	for (int i = 0; i < 10; ++i) {
		if (aCheckNum[i] == 0) {
			bAllRight = false;
			break;
		}
	}

	return bAllRight;
}

int GetSleepCount(int nNum)
{
	for (int i = 0; i < 10; ++i) {
		aCheckNum[i] = 0;
	}
	
	int nCount = 1;
	int nCheckNum = 0;
	while (1)
	{
		nCheckNum = nCount * nNum;
		bool bOk = IsAllRightNum(nCheckNum);
		if (bOk) {
			break;
		}
		if (nCheckNum < 0 || nCount >= nMaxCount ) {
			nCheckNum = 0;
			break;
		}

		nCount++;
	}
	return nCheckNum;
}

int main()
{
	//int nInputCount = 0;
	//vector<int> aInput;

	//cin >> nInputCount;

	//for (int i = 0; i < nInputCount; ++i) {
	//	int nNum = 0;
	//	cin >> nNum;
	//	aInput.push_back(nNum);
	//}

	fstream file;
	file.open("A-large.in");

	int nInputCount = 0;
	file >> nInputCount;

	vector<int> aInput;

	for (int i = 0; i < nInputCount; ++i) {
		int nNum = 0;
		file >> nNum;
		aInput.push_back(nNum);
	}

	file.close();

	ofstream fileOut;
	fileOut.open("result.txt", ios::out);

	for (unsigned i = 0; i < aInput.size(); ++i) {
		int nNum = GetSleepCount(aInput[i]);
		if (nNum == 0) {
			fileOut << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
		}
		else {
			fileOut << "Case #" << i + 1 << ": " << nNum << endl;
		}
	}

	fileOut.close();		
}