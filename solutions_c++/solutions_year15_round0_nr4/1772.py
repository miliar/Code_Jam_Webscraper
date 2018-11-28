#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
bool desc(int & i, int & j)
{
	return i > j;
}

int main()
{
	freopen("1.in", "rt", stdin);
	freopen("1.out", "wt", stdout);
	int T, X, R, C, max, min;
	std::vector<int> P;
	scanf("%d\n", &T);
	for (int kace = 1; kace <= T; ++kace)
	{
		scanf("%d %d %d\n", &X, &R, &C);
		max = std::max(R, C);
		min = std::min(R, C);
		if (X / 2 + (X % 2 ? 1 : 0) > min 
			|| X / 2 + 1 > max || R * C % X)
		{
			printf("%s%d: %s\n", "Case #", kace, "RICHARD");
			continue;
		}
		if (X > R*C)//may be never is true
		{
			printf("%s%d: %s\n", "Case #", kace, "GABRIEL");
			continue;
		}
		if (X == R*C || min == 1 || X < 3)
		{
			printf("%s%d: %s\n", "Case #", kace, "GABRIEL");
			continue;
		}
		if (min == 3 && X > max + 1)////4 or h
		{
			printf("%s%d: %s\n", "Case #", kace, "RICHARD");
			continue;
		}
		if (min > 3 && X > max + 2)//4 or h
		{
			printf("%s%d: %s\n", "Case #", kace, "RICHARD");
			continue;
		}
		if (min > 2 && X > 6)//hole
		{
			printf("%s%d: %s\n", "Case #", kace, "RICHARD");
			continue;
		}
		if (X >= 2*min)////T or P
		{
			printf("%s%d: %s\n", "Case #", kace, "RICHARD");
			continue;
		}
		printf("%s%d: %s\n", "Case #", kace, "GABRIEL");
	}
}
