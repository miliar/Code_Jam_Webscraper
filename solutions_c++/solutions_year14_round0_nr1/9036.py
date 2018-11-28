// codejam2014.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"

using namespace std;

int CommonCount, Answer;

void DoMagicTrick()
{
	int firstRow, secondRow,i,j;
	int firstArangement[4][4], secondArangement[4][4];
	int firstPick[4], secondPick[4];
	CommonCount = Answer = 0;
	////Accepting row numbers and arrangements
	cin>>firstRow;
	for(i=0; i<4; i++)
	{
		for(j=0; j<4; j++)
			cin>>firstArangement[i][j];
	}
	cin>>secondRow;
	for(i=0; i<4; i++)
	{
		for(j=0; j<4; j++)
			cin>>secondArangement[i][j];
	}

	//Storing row of first arrangement
	for(i=0; i<4; i++)
		firstPick[i]=firstArangement[firstRow-1][i];

	//Storing row of second arrangement
	for(i=0; i<4; i++)
		secondPick[i]=secondArangement[secondRow-1][i];

	//doing linear search of element in first array in 2nd array
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (secondPick[j] == firstPick[i])
			{
				CommonCount++;
				Answer = firstPick[i];
			}
		}
	}
}
int main()
{
	int T, i;
	cin>>T;
	for (int i = 1; i <= T; i++)
	{
		DoMagicTrick();
		if (CommonCount == 0)
		{
			cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		}
		else if (CommonCount > 1)
		{
			cout<<"Case #"<<i<<": Bad magician!"<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": "<<Answer<<endl;
		}
		
	}
	return 0;
}
