// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>
#include <map>
#include <list>
#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

int d;
int p[1005];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("b-large.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; T++)
	{
		scanf("%d", &d);
		for (int i = 0; i < d; i++)
			scanf("%d", &p[i]);

		int ans = 10000;

		for (int i = 1; i <= 1000; i++)
		{
			int sum = 0;
			for (int j = 0; j < d; j++)
				sum += (p[j] + i - 1) / i - 1;
			if (i + sum < ans)
				ans = i + sum;
		}
		printf("Case #%d: %d\n", T, ans);
	}
}