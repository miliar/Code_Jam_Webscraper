#include <fstream>
#include <algorithm>
#include <climits>
using namespace std;

#define MAX_MOTES_NUM	100

unsigned int SolveMotesInMin(unsigned int* pGameMotes , unsigned int nSize, unsigned int nIntialSize)
{
	unsigned int unIndex = 0, nAddCost, nRemoveCost, nInitialSizeAdded;
		
	while ((unIndex < nSize) && (nIntialSize > pGameMotes[unIndex]))
	{
		nIntialSize += pGameMotes[unIndex++];
	}

	if (unIndex < nSize)
	{
		if ((unIndex + 1) > nSize)
		{
			return 1;	
		}
		else
		{
			nInitialSizeAdded = (nIntialSize << 1) - 1;
			nAddCost = 0;
			
			while ((nInitialSizeAdded > 1) && (nInitialSizeAdded <= pGameMotes[unIndex]))
			{
				++nAddCost;	
				nInitialSizeAdded <<= 1;
				--nInitialSizeAdded;
			}
			
			if (nInitialSizeAdded == 1)
				nAddCost = INT_MAX;
			else
				nAddCost += SolveMotesInMin(pGameMotes + unIndex + 1, nSize - unIndex - 1, nInitialSizeAdded + pGameMotes[unIndex]);
				
			nRemoveCost = SolveMotesInMin(pGameMotes + unIndex + 1, nSize - unIndex - 1, nIntialSize);

			if (nAddCost < nRemoveCost)
				return nAddCost + 1;
			else return nRemoveCost + 1;
		}
	}
	else return 0;
}

int main()
{
	ifstream		InFile("A-large.in");
	ofstream		OutFile("A-large.out", ios_base::ate || ios_base::out);
	unsigned int	nCases, nArminSize, nTstCaseIndx, nMoteIndex, nMotesNum;
	unsigned int	GameMotes[MAX_MOTES_NUM];

	if (OutFile.is_open())
	{
		InFile >> nCases;

		nTstCaseIndx = 0;

		while (nCases--)
		{
			InFile >> nArminSize >> nMotesNum;

			nMoteIndex = 0;

			while (nMoteIndex < nMotesNum)
			{
				InFile >> GameMotes[nMoteIndex++];
			}
			
			sort(GameMotes, GameMotes + nMotesNum);
			
			OutFile << "Case #" << ++nTstCaseIndx << ": " << SolveMotesInMin(GameMotes, nMotesNum ,nArminSize) << endl;
		}
	}

	return 0;
}