// try.cpp : Defines the entry point for the console application.
//

#pragma warning (disable:4996)
#include "stdafx.h"

#include<stdio.h>
#include<iostream>
#include <string>
#include<vector>
#include <algorithm>
using namespace std;
vector<int> a;
bool judge(int mid)
{
	bool ret = false;
	for (int spe = 0; spe < mid; spe++)
	{
		int spe1 = spe;
		int nor = mid - spe;
		int siz = a.size();
		for (int i = 0; i < siz; i++)
		{
			int num = ceil((double)a[i] / nor) - 1;
			spe1 -= num;
		}
		if (spe1 >= 0)
		{
			return true;
		}
	}
	return false;
}
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B_large_out.txt", "w", stdout);
	int tk, tk1 = 0;
	cin >> tk;
	while (tk--)
	{
		tk1++;
		int n;
		cin >> n;
		a.resize(n);
		int maxVal = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> a[i];
			maxVal = max(maxVal, a[i]);
		}
		int l = 1, r = maxVal;
		while (l < r)
		{
			int mid = (l + r) / 2;
			if (judge(mid))
			{
				r = mid;
			}
			else {
				l = mid + 1;
			}
		}
		cout << "Case #" << tk1 << ": " << l << endl;
	}
}