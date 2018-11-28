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
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	cin >> T;

	for (int cas = 1; cas <= T; cas++)
	{
		int n;
		cin >> n;
		if (n == 0)
		{
			printf("Case #%d: INSOMNIA\n", cas);
			continue;
		}

		int ans = 0;
		for (int bit = 0; bit != 0x3FF; )
		{
			ans += n;
			FillBlack(ans, bit);
		}

		printf("Case #%d: %d\n", cas, ans);
	}
    return 0;
}

