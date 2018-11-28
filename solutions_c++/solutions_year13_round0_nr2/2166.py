#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include<fstream>
#include <limits>

int main()
{
	std::ofstream outFile;
	outFile.open("a.out");

	std::ifstream inFile;
	inFile.open("a.in");

	int NN;
	inFile >> NN;
	inFile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	for (int N=1; N<=NN; ++N)
	{
		int R, C, n;
		inFile >> R >> C;
		char board[100][100];
		char minV = 100, maxV = 1;
		inFile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
		for (int r=0; r<R; ++r)
		{
			for (int c=0; c<C; ++c)
			{
				inFile >> n;
				board[r][c] = n;
				if (minV > n) minV = n;
				if (maxV < n) maxV = n;
			}
			inFile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
		}

		// solution
		bool bYes = R == 1 || C == 1;
		if (!bYes)
		{
			for (int r=0; r<R; ++r)
			{
				for (int c=0; c<C; ++c)
				{
					for (int i=0; i<C; ++i)
					{
						if (board[r][c] < board[r][i])
						{
							for (int j=0; j<R; ++j)
							{
								if (board[r][c] < board[j][c])
								{
									goto END_SOLUTION;
								}
							}
							break;
						}
					}
				}
			}
			bYes = true;
		}

END_SOLUTION:

		// output result
		outFile << "Case #" << N << ": ";
		if (bYes)
		{
			 outFile << "YES";
		}
		else
		{
			outFile << "NO";
		}
		outFile << std::endl;
	}

	inFile.close();
	outFile.close();
	return 0;
}