#include <fstream>
#include <stdio.h>
#include <stdlib.h>
using std::ifstream;

int main(int argc, char *argv[])
{
	int MAX_CASE = 10;
	ifstream inputFile("A-small-attempt0.in");
	string line = "";
	getline(inputFile, line);
	int nNumofTestCase = atoi(line.c_str());
	int *pnArray = new int[MAX_CASE];
	for(int i = 0; i < nNumofTestCase; i++)
	{
		string strTestCase;
		getline(inputFile, strTestCase);
		int nPos = strTestCase.find_first_of(' ');
		string strMaxShyness = strTestCase.substr(0, nPos);
		string strArray = strTestCase.substr(nPos + 1, strTestCase.length() - nPos - 1);

		int nMaxShyness = atoi(strMaxShyness.c_str());

		for(int j = 0; j <= nMaxShyness; j++)
		{
			pnArray[j] = (int)strArray[j] - (int)'0';
		}


		int nPrefixSum = 0;
		int nNumofFriend = 0;
		nPrefixSum = pnArray[0];
		for(int j = 1; j < nMaxShyness; j++)
		{
			if(nPrefixSum >= j)
				nPrefixSum += pnArray[j];
			else
			{
				nNumofFriend += j - nPrefixSum;
				nPrefixSum += pnArray[j] + j - nPrefixSum;;
			}
		}
		if(nPrefixSum < nMaxShyness)
		{
			nNumofFriend++;
		}

		cout << "Case #" << i + 1 << ": " << nNumofFriend << endl;
	}

	return 1;
}
