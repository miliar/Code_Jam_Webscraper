// CodeJamTemplate.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

void initialize()
{
}

std::string& boardString(vector<char> board)
{
	std::string boardRep;
	for(auto c : board)
	{
		boardRep.push_back(c);
	}

	return boardRep;
}

char checkByPos(vector<char> board, int rows, int columns, int x, int y)
{
	if(columns * y + x >= 0 &&
	   columns * y + x < rows * columns)
		return board[columns * y + x];
	return '.';
}

int getPos(vector<char> board, int rows, int columns, int x, int y)
{
	return columns * y + x;
}

int clickCount(vector<char> board, int rows, int columns, int x, int y)
{
	int mines = 0;
	// Upper left
	if(x > 0 && y > 0 &&
		checkByPos(board, rows, columns, x-1, y-1) == '*')
		mines++;
	// Upper
	if(y > 0 && checkByPos(board, rows, columns, x, y-1) == '*')
		mines++;
	// Upper right
	if(y > 0 && x < columns - 1 &&
		checkByPos(board, rows, columns, x+1, y-1) == '*')
		mines++;
	// left
	if( x > 0 && checkByPos(board, rows, columns, x-1, y) == '*')
		mines++;
	// right
	if(x < columns - 1 && checkByPos(board, rows, columns, x+1, y) == '*')
		mines++;
	// lower left
	if(x > 0 && y < rows - 1 && checkByPos(board, rows, columns, x-1, y+1) == '*')
		mines++;
	// lower
	if(y < rows - 1 &&  checkByPos(board, rows, columns, x, y+1) == '*')
		mines++;
	// lower right
	if(y < rows - 1 && x < columns - 1 && checkByPos(board, rows, columns, x+1, y+1) == '*')
		mines++;
	
	return mines;
}


bool oneClick(vector<char> board, int rows, int columns)
{
	map<int, bool> covered;
	stack<int> currentFlow;
	int currentPos;

	for(int i = 0; i < board.size(); i++)
	{
		if(board[i] == 'c')
		{
			currentPos = i;
			covered[i] = true;
		}
		else if(board[i] == '.')
		{
			covered[i] = true;
		}
		else
		{
			covered[i] = false;
		}
	}

	currentFlow.push(currentPos);

	while(!currentFlow.empty())
	{
		currentPos = currentFlow.top();
		currentFlow.pop();

		if(currentPos < 0 || currentPos >= board.size())
			continue;

		if(covered[currentPos] == false)
			continue;

		covered[currentPos] = false;

		int curX, curY;

		curX = currentPos % columns;
		curY = currentPos / columns;

		if(clickCount(board, rows, columns, currentPos % columns, currentPos / columns) == 0)
		{
			// Push neighbors.
			// Upper left
			if(curX > 0 && curY > 0)
				currentFlow.push(currentPos - columns - 1);
			// upper
			if(curY > 0)
				currentFlow.push(currentPos - columns);
			if(curX < columns - 1 && curY > 0)
				currentFlow.push(currentPos - columns + 1);
			if(curX > 0 )
				currentFlow.push(currentPos - 1);
			if(curX < columns - 1)
				currentFlow.push(currentPos + 1);
			if(curX > 0 && curY < rows - 1)
				currentFlow.push(currentPos + columns - 1);
			if(curY < rows - 1)
				currentFlow.push(currentPos + columns);
			if(curX < columns - 1 && curY < rows - 1)
				currentFlow.push(currentPos + columns + 1);
		}
	}

	auto iter = covered.begin();
	while (iter != covered.end())
	{
		if(iter->second == true)
			return false;
		iter++;
	}

	return true;
}

void printBoard(vector<char> board, int rows, int columns)
{
	for(int i = 0; i < rows; i++)
	{
		for(int j = 0; j < columns; j++)
		{
			cout << board[columns * i + j];
		}
		cout << endl;
	}
}

void solve_case(int test_case)
{
	int rows, columns, mines;

	cin >> rows;
	cin >> columns;
	cin >> mines;

	vector<char> board;

	// Init board
	board.push_back('c');
	
	for(int i = 0; i < mines; i++)
		board.push_back('*');

	for(int i = mines; i < rows * columns - 1; i++)
		board.push_back('.');

	cout << "Case #" << test_case << ":" << endl;
	std::sort(board.begin(), board.end());

	do {
	    if(oneClick(board, rows, columns))
		{
			printBoard(board, rows, columns);
			return;
		}
	} while ( std::next_permutation(board.begin(), board.end()));
	cout << "Impossible" << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	initialize();

	int iCases;
	cin >> iCases;

	for (int i = 1; i <= iCases; i++)
		solve_case(i);

	return 0;
}
