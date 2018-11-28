// GoogleCJ1Prob1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>

using namespace std;

const string inputFileName = "C:\\Users\\Karan\\Desktop\\A-large.in";
const string outputFileName = "C:\\Users\\Karan\\Desktop\\outputlarge.txt";

char *outcomeX = "X won";
char *outcomeO = "O won";
char *outcomeDraw = "Draw";
char *outcomeNone = "Game has not completed";

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin(inputFileName);
	ofstream fout(outputFileName, ios::trunc);
	int T;
	char matrix[4][4];

	fin>>T;

	for (int testCase = 1; testCase <= T; testCase++)
	{
    	char *result;
	    bool resultFound = false;
		// Input matrix
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				fin>>matrix[i][j];
			}
		}

		// Check rows
		for (int i = 0; i < 4; i++)
		{
			int j;
			char rowStd = matrix[i][0];
			if (rowStd == 'T')
			{
				rowStd = matrix[i][1];
			}

			if (rowStd == '.')
			{
				continue;
			}
			cout<<"Rowstd is "<<rowStd<<endl;

			for (j = 0; j < 4; j++)
			{
				if (matrix[i][j] != rowStd &&
					matrix[i][j] != 'T')
				{
					break;
				}
			}

			if (j == 4)
			{
				resultFound = true;
				cout<<"Result found in row "<<i<<endl;
				if (rowStd == 'X')
				{
					result = outcomeX;
				}
				else
				{
					result = outcomeO;
				}
			}
		}

		//Check columns
		if (!resultFound)
		{
			for (int i = 0; i < 4; i++)
			{
				char colStd = matrix[0][i];
				int j;
				if (colStd == 'T')
				{
					colStd = matrix[1][i];
				}
    			if (colStd == '.')
	    		{
		    		continue;
			    }
    			cout<<"Colstd is "<<colStd<<endl;

				for (j = 0; j < 4; j++)
				{
					if (matrix[j][i] != colStd &&
						matrix[j][i] != 'T')
					{
						break;
					}
				}

				if (j == 4)
				{
					resultFound = true;
     				cout<<"Result found in col "<<i<<endl;
					if (colStd == 'X')
					{
						result = outcomeX;
					}
					else
					{
						result = outcomeO;
					}
					break;
				}
			}
		}

		// Diagonals

		// DiagSimple
		if (!resultFound)
		{
			int j = 0;
			char diagStd = matrix[0][0];
			if (diagStd == 'T')
			{
				diagStd = matrix[1][1];
			}
			cout<<"Diagstd is "<<diagStd<<endl;

			if (diagStd == 'X' || diagStd == 'O')
			{
				for (j = 0; j < 4; j++)
				{
					if (matrix[j][j] != diagStd &&
						matrix[j][j] != 'T')
					{
						break;
					}
				}

				if (j == 4)
				{
					resultFound = true;
					cout<<"Result found in diag 1."<<endl;

					if (diagStd == 'X')
					{
						result = outcomeX;
					}
					else
					{
						result = outcomeO;
					}
				}
			}
		}

		// Diag Other
		if (!resultFound)
		{
			int j = 0;
			char diagStd = matrix[0][3];
			if (diagStd == 'T')
			{
				diagStd = matrix[1][2];
			}
			cout<<"Diagstd is "<<diagStd<<endl;

			if (diagStd == 'X' || diagStd == 'O')
			{
				for (j = 0; j < 4; j++)
				{
					if (matrix[j][3 - j] != diagStd &&
						matrix[j][3 - j] != 'T')
					{
						break;
					}
				}

				if (j == 4)
				{
					resultFound = true;
					cout<<"Result found in diag 1."<<endl;
					if (diagStd == 'X')
					{
						result = outcomeX;
					}
					else
					{
						result = outcomeO;
					}
				}
			}
		}

		// Check for Draw
		if (!resultFound)
		{
			for (int i = 0; i < 4; i++)
			{
				for (int j = 0; j < 4; j++)
				{
					if (matrix[i][j] == '.')
					{
						resultFound = true;
						cout<<". found at "<<i<<","<<j<<endl;
						break;
					}
				}

				if (resultFound)
				{
					break;
				}
			}
			cout<<"Draw check result: "<<resultFound<<endl;
			if (resultFound)
			{
				result = outcomeNone;
			}
			else
			{
				result = outcomeDraw;
			}
		}

		cout<<"---------------------Case #"<<testCase<<": "<<result<<endl;
		fout<<"Case #"<<testCase<<": "<<result<<endl;
	}
	
	
	
	// The END
	getchar();
	return 0;
}

