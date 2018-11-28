//============================================================================
// Name        : B.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <queue>
#include <cmath>
using namespace std;

int a[10000];

int main() {
	freopen("B.txt", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	scanf("%d", &T);
	int D;

	for (int c = 1; c <= T; ++c)
	{
		scanf("%d", &D);
		int ans = 0, max = 0;
		for (int i = 0; i < D; ++i)
		{
			scanf("%d", &a[i]);
			if (a[i] > ans)
				ans = a[i];
		}
		max = ans;
		for (int s = 1; s <= max; ++s)
		{
			int t = 0;
			for (int i = 0; i < D; ++i)
				if (a[i] > s)
					t += (a[i] + (s - a[i] % s) % s) / s - 1;
			if (t + s < ans)
			{
				ans = t + s;
			}
		}
		printf("Case #%d: %d\n", c, ans);
	}
	return 0;
}
