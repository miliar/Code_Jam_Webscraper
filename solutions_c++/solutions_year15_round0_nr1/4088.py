#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>

int main()
{
	freopen("1.in", "rt", stdin);
	freopen("1.out", "wt", stdout);
	int T, s, result, sum;
	int S[1000];
	char tmp;
	scanf("%d\n", &T);
	for (int kace = 1; kace <= T; ++kace)
	{
		result = 0;
		sum = 0;
		scanf("%d ", &s);
		std::memset(S, 0, sizeof(S));
		for (int i = 0; i <= s; ++i)
		{
			scanf("%c", &tmp);
			S[i] = tmp - 48;
		}
		if (s == 0)
		{
			printf("%s%d: %d\n", "Case #", kace, 0);
			continue;
		}
		for (int i = 1; i <= s; ++i)
		{
			sum += S[i - 1];
			if (i - sum > 0)
			{
				result += i - sum;
				sum +=(i - sum);
			}
		}
		printf("%s%d: %d\n", "Case #", kace, result);
	}
}
