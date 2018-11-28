// contingsheep.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

bool comp(int *a)
{
	int i;
	for (i = 0; i <= 9; i++)
	{
		if (a[i] == 0) return false;
	}
	return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
#define cin fin
#define cout fout
	ifstream fin("data.in");
	ofstream fout("data.out");
	int t;
	cin >> t;
	int c;
	for (c = 1; c <= t; c++)
	{
		long long n;
		cin >> n;
		int a[10];
		for (int i = 0; i <= 9; i++)
		{
			a[i] = 0;
		}
		long long i = 1, nr;
		if (n == 0)
		{
			cout << "Case #" << c << ": " << "INSOMNIA" << '\n';
			continue;
		}
		while (!comp(a))
		{
			nr = n * i;
			i++;
			while (nr > 0)
			{
				a[nr % 10] = 1;
				nr /= 10;
			}
		}
		cout << "Case #" << c << ": " << n * (i - 1) << '\n';
	}
	return 0;
}

