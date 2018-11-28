#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <utility>
#include<map>
#include<string>
#define ull unsigned long long 
using namespace std;
int product[4][4] = { { 1, 2, 3, 4 }, { 2, -1, 4, -3 }, { 3, -4, -1, 2 }, { 4, 3, -2, -1 } };//1=1,i=2,j=3,k=4;
map<int, int> mapping = { { 1, 1 }, { 'i', 2 }, { 'j', 3 }, { 'k', 4 } };
int sign(int a)
{
	return (a>0) ? 1 : -1;
}
int prod(int a, int b)
{
	return (product[abs(a) - 1][abs(b) - 1] * (sign(a)*sign(b)));
}

int main()
{
	ull x;
	int t, l, i, p, f1, f2, f3, j;
	int b[10001];
	string s, a;
	cin >>t;
	for (i = 1; i <= t; i++)
	{
		p = 1;
		f1 = f2 = f3 = 0;
		cin >>l>>x;
		cin >> s;
		a = s;
		for (j = 1; j<x; j++)
		{
			a += s;
		}
		for (j = 0; j<a.size(); j++)
		{
			b[j] = mapping[a[j]];
		}
		for (j = 0; j<a.size(); j++)
		{
			p = prod(p, b[j]);
			if (p == 2)
			{
				f1 = 1;
				break;
			}

		}
		j++;
		p = 1;
		for (; j<a.size(); j++)
		{
			p = prod(p, b[j]);
			if (p == 3)
			{
				f2 = 1;
				break;
			}
		}
		j++;
		p = 1;
		for (; j<a.size(); j++)
		{
			p = prod(p, b[j]);
			if (p == 4 && j==a.size()-1 )
			{
				f3 = 1;
			}
		}
		if (f1 && f2 && f3)
			printf("Case #%d: YES\n", i);
		else
			printf("Case #%d: NO\n", i);
	}


	return 0;
}