// Standing Ovation.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int a[1010];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, sm, cnt, c = 1;
	char s[1010];
	scanf("%d", &t);
	while (t--)
	{
		cnt = 0;
		scanf("%d", &sm);
		scanf("%s", s);
		a[0] = s[0] - '0';
		for (int i = 1; i < sm + 1; i++)
		{
			if (a[i - 1] < i && s[i] != '0')
			{
				cnt += i - a[i - 1];
				a[i - 1] = i;
			}
			a[i] = a[i - 1] + s[i] - '0';
		}
		printf("Case #%d: %d\n", c, cnt);
		c++;
	}
	return 0;
}

