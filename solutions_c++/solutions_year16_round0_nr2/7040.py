// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

// #include "stdafx.h"
#include <cstdio>
#include <iostream>

using namespace std;

void FillBlack(int n, int& m)
{
	while (n)
	{
		m |= 1 << (n % 10);
		n /= 10;
	}
}

int main()
{
	 freopen("B-large.in", "r", stdin);
	 freopen("B-large.out", "w", stdout);

	int T;
	cin >> T;

	char str[200];
	for (int cas = 1; cas <= T; cas++)
	{
		scanf("%s", str);
		int n = strlen(str);
		str[n] = '+';

		int ans = 0;
		for (int i = n; i > 0; i--)
		{
			ans += str[i] != str[i - 1];
		}

		printf("Case #%d: %d\n", cas, ans);
	}
    return 0;
}

