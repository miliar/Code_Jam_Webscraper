/*
 * magictrick.cpp
 *
 *  Created on: Apr 11, 2014
 *      Author: kamalsharma
 */

#include <iostream>
#include <string>
#include <sstream>
#include <stdio.h>

using namespace std;

void readRow(int *rowArray)
{
	int rowNo;
	string ignore;

	scanf("%d\n",&rowNo);
	for(int j=0; j<4; j++)
	{
		if(j==(rowNo-1))
			scanf("%d %d %d %d\n", &rowArray[0], &rowArray[1], &rowArray[2], &rowArray[3]);
		else
			getline (cin,ignore);
	}
}

void compareRows(int *firstRow, int *secondRow, int caseNo)
{
	int count = 0;
	int curVal, matchVal=0;
	for(int j=0; j<4 && count<2; j++)
	{
		curVal = firstRow[j];
		if(!(curVal^secondRow[0])) count++;
		if(!(curVal^secondRow[1])) count++;
		if(!(curVal^secondRow[2])) count++;
		if(!(curVal^secondRow[3])) count++;
		if(count==1 && !matchVal) matchVal = curVal;
	}

	switch(count)
	{
		case 0: printf("Case #%d: Volunteer cheated!\n", caseNo); break;
		case 1: printf("Case #%d: %d\n",caseNo, matchVal); break;
		default: printf("Case #%d: Bad magician!\n", caseNo); break;
	}

	return;
}

int main()
{
	int noTests = 0, caseNo = 0;
	int firstRow[4], secondRow[4];

	scanf("%d\n",&noTests);
	for(int i=0, caseNo=1; i<noTests; i++, caseNo++)
	{
		readRow(firstRow);
		readRow(secondRow);
		compareRows(firstRow,secondRow, caseNo);
	}
}
