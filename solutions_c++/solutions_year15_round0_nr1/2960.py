// try.cpp : Defines the entry point for the console application.
//

#pragma warning (disable:4996)
#include "stdafx.h"

#include<stdio.h>
#include<iostream>
#include <string>
using namespace std;
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A_large_out.txt", "w", stdout);
	int tk, tk1 = 0;
	cin >> tk;
	while (tk--)
	{
		tk1++;
		int n;
		cin >> n;
		string s;
		cin >> s;
		int res = 0;
		int tot = 0;
		for (int i = 0; i <= n; i++)
		{
			int now = s[i] - '0';
			if (tot < i)
			{
				res += i - tot;
				tot = i;
			}
			tot += now;
		}
		cout << "Case #" << tk1 << ": " << res << endl;
	}
}