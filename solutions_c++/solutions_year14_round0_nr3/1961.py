/*
 * mines.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: kamalsharma
 */

#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

int ** allocate(int row, int col)
{
	int **board;
	board = (int**) malloc(row * sizeof(int*));
	for(int i = 0; i < row; ++i)
		board[i] = (int*) malloc(col * sizeof(int));

	return board;
}

void init(int **board, int row, int col)
{
	for(int i=0; i<row; i++)
		for(int j=0; j<col; j++)
			board[i][j] = -1;
}

void getNeighbourPos(int row, int col, int neighbourNo , int *neighbourRow, int *neighbourCol)
{
	switch(neighbourNo)
	{
	case 0: *neighbourRow = row-1; *neighbourCol=col-1; break;
	case 1: *neighbourRow = row-1; *neighbourCol=col; break;
	case 2: *neighbourRow = row-1; *neighbourCol=col+1; break;
	case 3: *neighbourRow = row; *neighbourCol=col-1; break;
	case 4: *neighbourRow = row; *neighbourCol=col+1; break;
	case 5: *neighbourRow = row+1; *neighbourCol=col-1; break;
	case 6: *neighbourRow = row+1; *neighbourCol=col; break;
	case 7: *neighbourRow = row+1; *neighbourCol=col+1; break;
	}
}

bool isValidPos(int row, int col, int noRows, int noCols)
{
	if(row>=0 && row<noRows && col>=0 && col<noCols)
		return true;
	return false;
}

void revertBoard(int **board, int row, int col, int setBits)
{
	for(int i=0; i<8; i++)
		if(setBits & (1<<i))
		{
			int neighbourRow=-1, neighbourCol=-1;
			getNeighbourPos(row, col, i, &neighbourRow, &neighbourCol);
			board[neighbourRow][neighbourCol] = -1;
		}
	return;
}

bool checkBoard(int **board, int row, int col, int noRows, int noCols, int emptyPoints)
{
	if(!isValidPos(row, col, noRows, noCols))
		return false;

	if(board[row][col] <0)
		return false;

	board[row][col] = 0;
	int setBits = 0;
	int count = 0;
	for(int i=0; i<8; i++)
	{
		int neighbourRow=-1, neighbourCol=-1;
		getNeighbourPos(row, col, i, &neighbourRow, &neighbourCol);
		if(isValidPos(neighbourRow, neighbourCol, noRows, noCols))
		{
			if(board[neighbourRow][neighbourCol]<0)
			{
				board[neighbourRow][neighbourCol] = 1;
				setBits = setBits | (1<<i);
				count++;
			}
		}
	}

	emptyPoints = emptyPoints - count;
	if(emptyPoints < 0)
	{
		revertBoard(board, row, col, setBits);
		return false;
	}
	if(emptyPoints == 0)
		return true;

	// Check Neighbours
	for(int i=0; i<8; i++)
	{
		if(setBits & (1<<i))
		{
			int neighbourRow=-1, neighbourCol=-1;
			getNeighbourPos(row, col, i, &neighbourRow, &neighbourCol);
			if(checkBoard(board, neighbourRow, neighbourCol, noRows, noCols, emptyPoints ))
				return true;
		}
	}

	// Revert
	revertBoard(board, row, col, setBits);

	return false;
}

void printBoard(int **board, int noRows, int noCols)
{
	bool firstZero = true;

	for(int i=0; i<noRows; i++)
	{
		for(int j=0; j<noCols; j++)
		{
				if(board[i][j] <0)
					printf("*");
				else if(firstZero && board[i][j] == 0)
				{
					printf("c");
					firstZero = false;
				}
				else
					printf(".");
		}
		printf("\n");
	}
}

void deallocate(int **board, int rows)
{
	for (int i = 0; i < rows; i++)
	{
	  free(board[i]);
	}
	free(board);
}

int main()
{
	int noTests = 0, caseNo = 0;
	int noRows, noCols, mines;

	int **board;
	board = allocate(50, 50);

	scanf("%d\n",&noTests);
	for(int i=0, caseNo=1; i<noTests; i++, caseNo++)
	{
		scanf("%d %d %d\n", &noRows, &noCols, &mines);
		printf("Case #%d:\n", caseNo);

		int emptyPoints = noRows*noCols-mines;

		init(board, noRows, noCols);
		if(emptyPoints == 1)
		{
			board[0][0] = 0;
			printBoard(board, noRows, noCols);
			continue;
		}

		board[0][0] = 0;
		if(!checkBoard(board, 0, 0, noRows, noCols, emptyPoints-1))
			printf("Impossible\n");
		else
			printBoard(board, noRows, noCols);
	}
	deallocate(board, 50);
}
