//============================================================================
// Name        : word.cpp
// Author      : Xutong Wang
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
using namespace std;

int t, n = 0, v[1000], d[2000], lo = 1000, hi = 1000;
string s;
char c[1000];

void printarray()
{
	for (int i = 0; i < 2000; i++)
	{
		if (d[i] == 0) continue;
		else cout << char(d[i]);
	}
	cout << endl;
}

int main()
{
	cin >> t;
	while (n < t)
	{
		lo = 1000; hi = 1000;
		for (int i = 0; i < 1000; i++)
		{
			v[i] = 0;
			c[i] = char(0);
		}
		for (int i = 0; i < 2000; i++)
		{
			d[i] = 0;
		}
		n++;
		cin >> s;
		strcpy(c, s.c_str());
		for (int i = 0; i < 1000; i++)
		{
			v[i] = int(c[i]);
		}
		for (int i = 0; i < 1000; i++)
		{
			if (v[i] >= d[lo])
			{
				lo--;
				d[lo] = v[i];
			}
			else
			{
				hi++;
				d[hi] = v[i];
			}
		}
		cout << "Case #" << n << ": ";
		printarray();
	}
	return 0;
}
