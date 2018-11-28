#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <list>
#include <stack>
#include <algorithm>
#include <queue>
#include <map>
#include <cstdlib>
#include <set>
#include <string>
#include <cstring>
#include <memory>
using namespace std;

//ofstream fout("C:\\Users\\Administrator\\Desktop\\B.out");
#define fout cout

class B
{
public:
	void Run();

private:
	void Input();
	void Do();
	void Output();
	bool TryRow();
	bool TryCol();

private:
	static const int MAX_ROW_NUM = 100, MAX_COL_NUM = 100;
	int caseNum, caseIndex;
	int rowNum, colNum;
	int board[MAX_ROW_NUM][MAX_COL_NUM];
	int rowMax[MAX_ROW_NUM], rowMin[MAX_ROW_NUM];
	int colMax[MAX_COL_NUM], colMin[MAX_COL_NUM];
	int maxCol, maxRow;
	bool result;
};

void B::Run()
{
	scanf("%d", &caseNum);
	for(caseIndex = 1; caseIndex <= caseNum; ++caseIndex)
	{
		Input();
		Do();
		Output();
	}
}

void B::Input()
{
	scanf("%d %d", &rowNum, &colNum);
	for(int row = 0; row < rowNum; ++row) for(int col = 0; col < colNum; ++col)
		scanf("%d", &board[row][col]);
}

void B::Do()
{
	maxRow = maxCol = 0;
	for(int row = 0; row < rowNum; ++row) for(int col = 0; col < colNum; ++col)
	{
		if(board[row][col] > board[maxRow][maxCol])
		{
			maxRow = row;
			maxCol = col;
		}
	}

	for(int row = 0; row < rowNum; ++row)
	{
		rowMax[row] = rowMin[row] = board[row][0];
		for(int col = 1; col < colNum; ++col)
		{
			rowMax[row] = max(rowMax[row], board[row][col]);
			rowMin[row] = min(rowMin[row], board[row][col]);
		}
	}
	for(int col = 0; col < colNum; ++col)
	{
		colMax[col] = colMin[col] = board[0][col];
		for(int row = 1; row < rowNum; ++row)
		{
			colMax[col] = max(colMax[col], board[row][col]);
			colMin[col] = min(colMin[col], board[row][col]);
		}
	}

	if(TryRow() || TryCol()) result = true;
	else result = false;
}

bool B::TryCol()
{
	for(int col = 0; col < colNum; ++col)
	{
		for(int row = 0; row < rowNum; ++row)
		{
			if(board[row][col] > board[row][maxCol]) return false;
			else if(board[row][col] < board[row][maxCol] && board[row][col] < colMax[col]) return false;
		}
	}
	return true;
}


bool B::TryRow()
{
	for(int row = 0; row < rowNum; ++row)
	{
		for(int col = 0; col < colNum; ++col)
		{
			if(board[row][col] > board[maxRow][col]) return false;
			else if(board[row][col] < board[maxRow][col] && board[row][col] < rowMax[row]) return false;
		}
	}
	return true;
}

void B::Output()
{
	fout << "Case #" << caseIndex << ": " << (result ? "YES" : "NO") << endl;
	//printf("Case #%d: %s\n", caseIndex, result ? "YES" : "NO");
}

B instance;
int main()
{
	instance.Run();
	return 0;
}
