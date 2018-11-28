// GCJ.cpp : Defines the entry point for the console application.
//

#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstring>
using namespace std;
#pragma warning (disable : 4996)

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, bk;
	cin >> t;
	for (bk = 1; bk <= t; bk++)
	{
		int s, a[10], i, j, k, ans = 0, sum = 0, temp;
		cin >> s;
		for (i = 0; i <= s; i++)
		{
			scanf("%1d", &a[i]);
		}
		sum = a[0];
		for (i = 1; i <= s; i++)
		{
			if (a[i]!=0)
			{
				if (sum < i)
				{
					ans = ans + (i - sum);
					sum = i;
				}
				sum = sum + a[i];
			}
		}
		cout << "Case #" << bk << ": " << ans << endl;
	}
	return 0;
}
