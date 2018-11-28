// Lawnmower.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <tchar.h>
#include <iostream>

using namespace std;

unsigned int getHigher(unsigned int A[100][100], unsigned int row, unsigned int numRow,  unsigned int numCol)
{
	unsigned int Res = A[row][0];
	for(unsigned int i=0; i<numCol; i++)
	{
		unsigned int val = A[row][i];
		if(val > Res)
		{
			Res = val;
		}
	}
	return Res;
}

bool isHigher(unsigned int val, unsigned int A[100][100], unsigned int col, unsigned int numRow, unsigned int numCol)
{
	bool isHigher = true;
	for(unsigned int i=0; ((i<numRow) && isHigher); i++)
	{
		if(A[i][col] > val)
		{
			isHigher = false;
		}
	}
	return isHigher;
}


int _tmain(int argc, _TCHAR* argv[])
{
	unsigned int T, N, M;
	unsigned int A[100][100];
	cin >> T;

	for(unsigned int i=0; i<T; i++)
	{
		cin >> N;
		cin >> M;

		for(unsigned int k=0; k<N; k++)
		{
			for(unsigned int l=0; l<M; l++)
			{
				cin >> A[k][l];
			}
		}

		bool bPossible = true;
		for(unsigned int k=0; ((k<N) && bPossible); k++)
		{
			unsigned int h = getHigher(A, k, N, M);

			for(unsigned int l=0; ((l<M) && bPossible); l++)
			{
				unsigned int val = A[k][l];
				if(val < h)
				{
					if(!isHigher(val, A, l, N, M))
					{
						bPossible = false;
					}
				}
			}

		}
		cout << "Case #" << i+1 << ": " << (bPossible?"YES":"NO") <<endl;
	}


	return 0;
}

