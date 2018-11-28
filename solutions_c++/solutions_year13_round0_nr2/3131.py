#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <cmath>
#include <string>

using namespace std;

bool checkRow(int temp, int row, int p[][101], int M)
{
	for (int k = 0; k < M; k++)
		{
		if (p[row][k] > temp)
			{
			return false;
			}
		}
	return true;
}

bool checkCol(int temp, int col, int p[][101], int N)
{
	for (int k = 0; k < N; k++)
		{
		if (p[k][col] > temp)
			{
			return false;
			}
		}
	return true;
}

int main()
{
	ifstream inData;
	ofstream outData;
	inData.open("B-large.in.txt");
	outData.open("output.txt");
	
	int T, N, M, j, k, s, temp, row, col, temp1, temp2, rowsum, tempsum, colsum;
	int p[101][101], completed[101][101];
	int crap;
	inData >> T;
	
	for (int i = 0; i < T; i++)
		{
		memset(p, 0, sizeof(p[0][0])*101*101);
		memset(completed, 0, sizeof(completed[0][0])*101*101);
		inData >> N >> M;
		if (N == 1 || M == 1)
			{
			outData << "Case #" << i + 1 << ": YES" << endl;
			for (j = 0; j < N; j++)
				for (k = 0; k < M; k++)
					{
					inData >> crap;
					}
			goto done;
			}
		for (j = 0; j < N; j++)
			{
			for (k = 0; k < M; k++)
				{
				inData >> p[j][k];
				}
			}
		
		again:
		temp = 101;
		for (j = 0; j < N; j++)
			for (k = 0; k < M; k++)
				{
				if (completed[j][k] == 0 && p[j][k] < temp)
					{
					temp = p[j][k];
					}
				}

		for (j = 0; j < N; j++)
			for (k = 0; k < M; k++)
				{
				if (p[j][k] == temp)
					{
					if (checkRow(temp, j, p, M))
						{
						for (s = 0; s < M; s++)
							{
							completed[j][s] = 1;
							}
						continue;
						}
					else if (checkCol(temp, k, p, N))
						{
						for (s = 0; s < N; s++)
							{
							completed[s][k] = 1;
							}
						continue;
						}
					else
						{
						outData << "Case #" << i + 1 << ": NO" << endl;
						goto done;
						}
					}
				}
		tempsum = 0;
		for (j = 0; j < N; j++)
			for (k = 0; k < M; k++)
				tempsum += completed[j][k];
		if (tempsum != M*N)
			goto again;
		
		YES:
		outData << "Case #" << i + 1 << ": YES" << endl;
		done:;
		}
	
	inData.close();
	outData.close();
}





