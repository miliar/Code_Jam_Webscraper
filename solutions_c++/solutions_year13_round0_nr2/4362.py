// P_A.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include <iostream>
using namespace std;

void test(int n)
{
	int A[4][4];
	char c;
	bool empty = false;

	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			cin >> c;
			switch(c)
			{
			case 'X':
				A[i][j] = 100;
				break;
			case 'O':
				A[i][j] = 500;
				break;
			case '.':
				A[i][j] = 10000;
				empty = true;
				break;
			case 'T':
				A[i][j] = 0;
				break;
			}
		}
	}

	for (int i=0;i<4;i++)
	{
		int s = A[i][0] + A[i][1] + A[i][2] + A[i][3];
		if (s == 400 || s == 300)
			goto X_WIN;
		if (s == 1500 || s == 2000)
			goto Y_WIN;
	}

	for (int i=0;i<4;i++)
	{
		int s = A[0][i] + A[1][i] + A[2][i] + A[3][i];
		if (s == 400 || s == 300)
			goto X_WIN;
		if (s == 1500 || s == 2000)
			goto Y_WIN;
	}

	{
		int s = A[0][0] + A[1][1] + A[2][2] + A[3][3];
		if (s == 400 || s == 300)
			goto X_WIN;
		if (s == 1500 || s == 2000)
			goto Y_WIN;
	}

	{
		int s = A[3][0] + A[2][1] + A[1][2] + A[0][3];
		if (s == 400 || s == 300)
			goto X_WIN;
		if (s == 1500 || s == 2000)
			goto Y_WIN;
	}

	if (empty)
		goto NOT_COMPLETE;

	goto DRAW;

	return;
X_WIN:
	printf("Case #%d: X won\n", n+1);
	return;
Y_WIN:
	printf("Case #%d: O won\n", n+1);
	return;
DRAW:
	printf("Case #%d: Draw\n", n+1);
	return;
NOT_COMPLETE:
	printf("Case #%d: Game has not completed\n", n+1);
	return;


}

#include <vector>
void test2(int n)
{
	int M, N;

	cin >> M;
	cin >> N;

	vector<vector<int>> A(M, vector<int>(N));
	for(int i=0;i<M;i++)
	{
		for(int j=0;j<N;j++)
		{
			cin >> A[i][j];
		}
	}

	for(int i=0;i<M;i++)
	{
		for(int j=0;j<N;j++)
		{
			int t = A[i][j];
			bool b1 = true;
			bool b2 = true;

			for(int k=0;k<M;k++)
			{
				if (t<A[k][j])
				{
					b1 = false;
					break;
				}
			}

			for(int k=0;k<N;k++)
			{
				if (t<A[i][k])
				{
					b2 = false;
					break;
				}
			}

			if (b1 == false && b2 == false)
			{
				printf("Case #%d: NO\n", n+1);
				return;
			}
		}
	}

	printf("Case #%d: YES\n", n+1);
}

int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	cin >> t;

	for(int i=0;i<t;i++)
	{
		test2(i);
	}

	return 0;
}

