#pragma comment(linker, "/STACK:128777216")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <string>
#include <memory.h>
using namespace std;

void prepare()
{
#ifdef _DEBUG
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
cin.sync_with_stdio(false);
cout.sync_with_stdio(false);
}

char a[4][4];


int main()
{
	prepare();
	int n;
	cin >> n;
	for (int t = 0; t < n; t++)
	{
		int k = 0;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				cin >> a[i][j];
				if (a[i][j] == '.')
					k++;
			}
		char ch = '0';
		for (int i = 0; i < 4; i++)
		{
			bool flag = 1;
			char cur = a[i][0];
			for (int j = 1; j < 3; j++)
				if (a[i][j] != cur && !(j == 1 && cur == 'T') || a[i][j] == '.')
					flag = 0;
			if (flag && (a[i][3] == 'T' || a[i][3] == cur))
				ch = cur;
		}
		//cout << ch;

		for (int i = 0; i < 4; i++)
		{
			bool flag = 1;
			char cur = a[0][i];
			for (int j = 1; j < 3; j++)
				if (a[j][i] != cur && !(j == 1 && cur == 'T') || a[j][i] == '.' )
					flag = 0;
			if (flag && (a[3][i] == 'T' || a[3][i] == cur) )
				ch = cur;
		}
		//cout << ch;

		bool flag = 1;
		char cur = a[0][0];
		for (int j = 1; j < 3; j++)
			if (a[j][j] != cur && !(j == 1 && cur == 'T') || a[j][j] == '.' )
				flag = 0;
		if (flag && (a[3][3] == 'T' || a[3][3] == cur))
			ch = cur;

		flag = 1;
		cur = a[0][3];
		for (int i = 1; i < 3; i++)
			if (a[i][4 - i - 1] != cur && !(i == 1 && cur == 'T') || a[i][4 - i - 1] == '.' )
				flag = 0;
		if (flag && (a[3][0] == 'T' || a[3][0] == cur))
			ch = cur;

		//cout << ch;
		cout << "Case #" << t + 1 << ": ";
		if (ch == 'X')
			cout << "X won\n";
		else
			if (ch == 'O')
				cout << "O won\n";
			else
				if (k == 0)
					cout << "Draw\n";
				else
					cout << "Game has not completed\n";



	}
	
	
	return 0;
}
