
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <limits>
#include <list>
using namespace std;

void testCase()
{
	int a, b, k;
	scanf("%d%d%d", &a, &b, &k);

	int answer = 0;
	for (int i = 0; i < a; i++)
	{
		for (int j = 0; j < b; j++)
		{
			for (int p = 0; p < k; p++)
			{
				answer += (i & j) == p;
			}
		}
	}
	printf("%d", answer);
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("ouptut.txt", "wt", stdout);

	int t;
	scanf("%d", &t);

	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		testCase();
		printf("\n");
	}

	return 0;
}
