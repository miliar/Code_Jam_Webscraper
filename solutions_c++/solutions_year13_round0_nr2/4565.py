#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include "Lawn.h"

using namespace std;

Lawn::Lawn(int aInitSize) : mRows(0), mCols(0), mInitSize(aInitSize)
{
	mLawn = new int*[aInitSize];
	for(int i = 0; i < aInitSize; ++i)
		mLawn[i] = new int[aInitSize];
	mRowMax = new int[aInitSize]; 
	mColMax = new int[aInitSize];
}

Lawn::~Lawn()
{
	for(int i = 0; i < mInitSize; ++i)
		delete[] mLawn[i];
	delete[] mLawn;
	delete[] mRowMax;
	delete[] mColMax;
}

void Lawn::ReadLawn(fstream& aFile,int aRows, int aCols)
{
	mRows = aRows;
	mCols = aCols;
	string line;
	for(int i = 0; i < mRows; ++i)
	{
		getline(aFile,line);
		stringstream input_row(line);
		mRowMax[i] = 0;
		for(int j = 0; j < mCols; ++j)
		{
			input_row >> mLawn[i][j];
			if(mLawn[i][j] > mRowMax[i])
				mRowMax[i] = mLawn[i][j];
		}
	}
	for(int i = 0; i < mCols; ++i)
	{
		mColMax[i] = 0;
		for(int j = 0; j < mRows; ++j)
		{
			if(mLawn[j][i] > mColMax[i])
				mColMax[i] = mLawn[j][i];
		}
	}
}

bool Lawn::IsPossible()
{
	int lastcol = mCols - 1;
	int lastrow = mRows - 1;
	for(int i = 0; i < mRows; ++i)
		for(int j = 0; j < mCols; ++j)
		{
			if(mLawn[i][j] < mRowMax[i] && mLawn[i][j] < mColMax[j])
				return false;
		}
	
	return true;
}

void Lawn::OutputLawn()
{
	cout << "Current lawn: " << endl;
	for(int i = 0; i < mRows; ++i)
	{
		for(int j = 0; j < mCols; ++j)
			cout << mLawn[i][j] << " ";
		cout << endl;
	}
}
