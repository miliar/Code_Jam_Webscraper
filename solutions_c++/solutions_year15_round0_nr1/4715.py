// GCJ.cpp : Defines the entry point for the console application.
//

#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<cmath>
#include<string>
#include<vector>
#include<cstring>
using namespace std;
#pragma warning (disable : 4996)

typedef long long nil;

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t, bk;
	cin >> t;
	for (bk = 1; bk <= t; bk++)
	{
		nil s, i, ans = 0, sum = 0, temp;
		vector<nil> v;
		cin >> s;
		for (i = 0; i <= s; i++)
		{
			scanf("%1lld", &temp);
			v.push_back(temp);
		}
		sum = v[0];
		for (i = 1; i <= s; i++)
		{
			if (v[i]!=0)
			{
				if (sum < i)
				{
					ans = ans + (i - sum);
					sum = i;
				}
				sum = sum + v[i];
			}
		}
		cout << "Case #" << bk << ": " << ans << endl;
	}
	return 0;
}
