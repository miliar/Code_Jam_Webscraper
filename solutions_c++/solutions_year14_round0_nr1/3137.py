#include <algorithm>
#include <cmath>
#include <cstdio>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

int nbTests;
int lig;
int val[16];
int curCase;

void computeAnswer()
{
	for(int iTest = 0; iTest < nbTests; ++iTest)
	{
		for(int i = 0; i < 16; ++i)
			val[i] = 0;
		for(int i = 0; i < 2; ++i)
		{
			scanf("%d", &lig);
			for(int iLig = 0; iLig < 4; ++iLig)
			{
				for(int iCol = 0; iCol < 4; ++iCol)
				{
					scanf("%d", &curCase);
					if(iLig == lig-1)
						++val[curCase-1];
				}
			}
		}
		int nbDouble = 0, iDouble;
		for(int i = 0; i < 16; ++i)
		{
			if(val[i] == 2)
			{
				++nbDouble;
				iDouble = i+1;
			}
		}
		if(nbDouble == 0)
			printf("Case #%d: Volunteer cheated!\n", iTest+1);
		else if(nbDouble == 1)
			printf("Case #%d: %d\n", iTest+1, iDouble);
		else
			printf("Case #%d: Bad magician!\n", iTest+1);
	}
}

void readInput()
{
	//*
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	//*/
	scanf("%d", &nbTests);
}

int main()
{
	readInput();
	computeAnswer();
	return 0;
}
