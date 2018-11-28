#include "stdio.h"
#include <iostream>
#include <string>

using namespace std;

int main()
{
	int probNum = 0;
	const string xWon = "X won";
	const string oWon = "O won";
	const string draw = "Draw";
	const string notComp = "Game has not completed";
	string outputStr = "";

	// Problem Num
	cin >> probNum;

	for(int i = 0; i < probNum; ++i)
	{
		int xNumRow[4]={0,0,0,0};
		int xNumCol[4]={0,0,0,0};
		int xNumDia[2]={0,0};
		int oNumRow[4]={0,0,0,0};
		int oNumCol[4]={0,0,0,0};
		int oNumDia[2]={0,0};
		int dotNum = 0;

		for(int j = 0; j < 4; ++j)
		{
			string rowStr = "";
			cin >> rowStr;
			for(int k = 0; k < 4; ++k)
			{
				if(j == k)
				{
					if('X' == rowStr[k])
					{
						xNumDia[0]++;
					}
					else if('O' == rowStr[k])
					{
						oNumDia[0]++;
					}
					else if('T' == rowStr[k])
					{
						xNumDia[0]++;
						oNumDia[0]++;
					}
				}

				if(3 == j + k)
				{
					if('X' == rowStr[k])
					{
						xNumDia[1]++;
					}
					else if('O' == rowStr[k])
					{
						oNumDia[1]++;
					}
					else if('T' == rowStr[k])
					{
						xNumDia[1]++;
						oNumDia[1]++;
					}
				}

				if('X' == rowStr[k])
				{
					xNumRow[j]++;
					xNumCol[k]++;
				}
				else if('O' == rowStr[k])
				{
					oNumRow[j]++;
					oNumCol[k]++;
				}
				else if('T' == rowStr[k])
				{
					xNumRow[j]++;
					xNumCol[k]++;
					oNumRow[j]++;
					oNumCol[k]++;
				}
				else if('.' == rowStr[k])
				{
					dotNum++;
				}
			}
		}
		if(0 == dotNum)
		{
			outputStr = draw;
		}
		else
		{
			outputStr = notComp;
		}
		for( int l = 0; l < 4; ++l)
		{
			if(4 == xNumRow[l] || 4 == xNumCol[l])
			{
				outputStr = xWon;
				break;
			}
			else if(4 == oNumRow[l] || 4 == oNumCol[l])
			{
				outputStr = oWon;
				break;
			}
		}
		if(4 == xNumDia[0] || 4 == xNumDia[1])
		{
			outputStr = xWon;
		}
		if(4 == oNumDia[0] || 4 == oNumDia[1])
		{
			outputStr = oWon;
		}
		cout << "Case #" << i+1 << ": " << outputStr << endl;
	}
}
