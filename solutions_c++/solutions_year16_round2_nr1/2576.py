#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <map>

using namespace std;

vector <string> collab(10);
vector <int> ans(10, 0);

void mapEdit(map <char, int>* myMap, string str)
{
	int n = str.size();
	for (int i = 0; i < n; i++)
		if (myMap->find(str[i]) != myMap->end()) myMap->at(str[i])++;
		else myMap->insert(make_pair(str[i], 1));
}

void mapEdit2(map <char, int>* myMap, string str)
{
	int n = str.size();
	int zCol = 0, wCol = 0, uCol = 0, xCol = 0, gCol = 0, tCol = 0, fCol = 0, sCol = 0, iCol = 0, nCol = 0;
	for (int i = 0; i < n; i++)
	{
		if ((str[i]) == 'Z') zCol++;
		if ((str[i]) == 'W') wCol++;
		if ((str[i]) == 'U') uCol++;
		if ((str[i]) == 'X') xCol++;
		if ((str[i]) == 'G') gCol++;
	}
	for (int i = 0; i < 10; i++)
	{
		if (i == 0)
			for (int j = 0; j < collab[i].size(); j++)
			{
			if (myMap->find(collab[i][j]) != myMap->end()) myMap->at(collab[i][j]) -= zCol;
			}
		if (i == 2)
			for (int j = 0; j < collab[i].size(); j++)
			{
			if (myMap->find(collab[i][j]) != myMap->end()) myMap->at(collab[i][j]) -= wCol;
			}
		if (i == 4)
			for (int j = 0; j < collab[i].size(); j++)
			{
			if (myMap->find(collab[i][j]) != myMap->end()) myMap->at(collab[i][j]) -= uCol;
			}
		if (i == 6)
			for (int j = 0; j < collab[i].size(); j++)
			{
			if (myMap->find(collab[i][j]) != myMap->end()) myMap->at(collab[i][j]) -= xCol;
			}
		if (i == 8)
			for (int j = 0; j < collab[i].size(); j++)
			{
			if (myMap->find(collab[i][j]) != myMap->end()) myMap->at(collab[i][j]) -= gCol;
			}
	}
	if (myMap->find('T') != myMap->end()) tCol = myMap->at('T');
	for (int j = 0; j < collab[3].size(); j++)
	{
		if (myMap->find(collab[3][j]) != myMap->end()) myMap->at(collab[3][j]) -= tCol;
	}
	if (myMap->find('F') != myMap->end()) fCol = myMap->at('F');
	for (int j = 0; j < collab[5].size(); j++)
	{
		if (myMap->find(collab[5][j]) != myMap->end()) myMap->at(collab[5][j]) -= fCol;
	}
	if (myMap->find('S') != myMap->end()) sCol = myMap->at('S');
	for (int j = 0; j < collab[7].size(); j++)
	{
		if (myMap->find(collab[7][j]) != myMap->end()) myMap->at(collab[7][j]) -= sCol;
	}
	if (myMap->find('I') != myMap->end()) iCol = myMap->at('I');
	for (int j = 0; j < collab[9].size(); j++)
	{
		if (myMap->find(collab[9][j]) != myMap->end()) myMap->at(collab[9][j]) -= iCol;
	}
	if (myMap->find('N') != myMap->end()) nCol = myMap->at('N');
	for (int j = 0; j < collab[1].size(); j++)
	{
		if (myMap->find(collab[1][j]) != myMap->end()) myMap->at(collab[1][j]) -= nCol;
	}
	ans[0] = zCol;
	ans[1] = nCol;
	ans[2] = wCol;
	ans[3] = tCol;
	ans[4] = uCol;
	ans[5] = fCol;
	ans[6] = xCol;
	ans[7] = sCol;
	ans[8] = gCol;
	ans[9] = iCol;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	collab[0] = "ZERO";
	collab[1] = "ONE";
	collab[2] = "TWO";
	collab[3] = "THREE";
	collab[4] = "FOUR";
	collab[5] = "FIVE";
	collab[6] = "SIX";
	collab[7] = "SEVEN";
	collab[8] = "EIGHT";
	collab[9] = "NINE";
	int n;
	cin >> n;
	string str;
	getline(cin, str);
	for (int i = 1; i <= n; i++)
	{
		map <char, int> myMap;
		getline(cin, str);
		mapEdit(&myMap, str);
		mapEdit2(&myMap, str);
		cout << "Case #" << i << ": ";
		for (int i = 0; i < 10; i++)
			for (int j = 0; j < ans[i]; j++)
				cout << i;
		cout << endl;
		ans.assign(10, 0);
	}
	return 0;
}