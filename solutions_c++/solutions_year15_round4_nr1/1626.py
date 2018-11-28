// jam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
typedef __int64 LONGLONG;

int calR4(int R, int C)
{
	if (C%3==0)
	{
		if (R < 4)
		{
			return 2;
		}
		else if (R < 6)
		{
			return 3;
		}
		return 4;
	}
	if (R < 3)
	{
		return 1;
	}
	else if (R < 4)
	{
		return 2;
	}
	else if (R < 6)
	{
		return 1;
	}
	return 2;
}

int checkDir(vector<vector<char>>& nArr, int i, int j, char dir)
{
	if (dir == '<')
	{
		for (int k = 0; k < j; k++)
		{
			if (nArr[i][k] != '.')
			{
				return true;
			}
		}
		return false;
	}
	if (dir == '>')
	{
		for (int k = j+1; k < nArr[i].size(); k++)
		{
			if (nArr[i][k] != '.')
			{
				return true;
			}
		}
		return false;
	}
	if (dir == '^')
	{
		for (int k = 0; k < i; k++)
		{
			if (nArr[k][j] != '.')
			{
				return true;
			}
		}
		return false;
	}
	for (int k = i+1; k < nArr.size(); k++)
	{
		if (nArr[k][j] != '.')
		{
			return true;
		}
	}
	return false;

}

int calR(vector<vector<char>>& nArr)
{
	int nR = 0;
	for (int i = 0; i < nArr.size(); i++)
	{
		for (int j = 0; j < nArr[i].size(); j++)
		{
			if (nArr[i][j] == '.')
			{
				continue;
			}
			if (checkDir(nArr, i, j, nArr[i][j]))
			{
				continue;
			}

			if (!checkDir(nArr, i, j, '>')&&!checkDir(nArr, i, j, '<')&&!checkDir(nArr, i, j, '^')&&!checkDir(nArr, i, j, 'v'))
			{
				return -1;
			}

			nR += 1;
		}
	}
	return nR;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int nSizeT;
	cin >> nSizeT;
	for (int i = 0; i < nSizeT; i++)
	{
		int R;
		int C;
		cin >> R >> C;
		vector<vector<char>> nArr;
		nArr.resize(R);
		for (int j = 0; j < R; j++)
		{
			nArr[j].resize(C);
			for (int k = 0; k < C; k++)
			{
				cin >> nArr[j][k];
			}
		}
		string sNote = "Case #";
		int nR = calR(nArr);
		if (nR < 0)
		{
			cout << sNote << i+1<<": "<<"IMPOSSIBLE"<<"\n";
		}
		else
		{
			cout << sNote << i+1<<": "<<nR<<"\n";
		}		
	}
	return 0;
}
