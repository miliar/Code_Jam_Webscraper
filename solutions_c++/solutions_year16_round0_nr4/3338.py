#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<algorithm>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<queue>

using namespace std;

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	int k, c, s, t, i, j;
	long long orz,a[105];
	cin >> t;
	j = 1;
	while (t--)
	{
		cin >> k >> c >> s;
		a[0] = 1;
		cout << "Case #" << j++ << ":";
		for (i = 1; i <= c + 1; i++)
		{
			a[i] = a[i - 1] * k;
		}
		for (i = 0; i < s; i++)
		{
			orz = 0;
			for (int ii = 0; ii <c; ii++)
			{
				orz = orz + i*a[ii];
			}
			orz++;
			cout << " "<<orz ;
		}
		cout << "\n";
	}
}