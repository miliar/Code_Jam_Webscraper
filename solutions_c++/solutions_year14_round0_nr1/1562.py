#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

#define forl(i,a,b) for(int i = a; i < b; ++i)


int main()
{
	int numCases;
	cin >> numCases;

	forl(caseNo, 1, numCases+1)
	{
		int temp;
		int rowA[4];
		int rowB[4];
		int rowNumA;
		int rowNumB;
		cin >> rowNumA;
		forl(i,1,5)
		{
			if (i == rowNumA)
			{
				cin >> rowA[0] >> rowA[1] >> rowA[2] >> rowA[3];
			}
			else
			{
				cin >> temp >> temp >> temp >> temp;
			}
		}
		cin >> rowNumB;
		forl(i,1,5)
		{
			if (i == rowNumB)
			{
				cin >> rowB[0] >> rowB[1] >> rowB[2] >> rowB[3];
			}
			else
			{
				cin >> temp >> temp >> temp >> temp;
			}
		}

		int numSame = 0;
		int answer = 0;
		forl(i,0,4)
		{
			forl(j,0,4)
			{
				//cerr << "Checking " << rowA[i] << " vs " << rowB[j] << "(" << i <<"," << j << ")" << endl;
				if (rowA[i] == rowB[j])
				{
					answer = rowA[i];
					numSame++;
				}
			}
		}

		cout << "Case #" << caseNo << ": ";
		if (numSame == 0)
		{
			cout << "Volunteer cheated!" << endl;
		}
		else if (numSame > 1)
		{
			cout << "Bad magician!" << endl;
		}
		else
		{
			cout << answer << endl;
		}
	}
	return 0;
}
