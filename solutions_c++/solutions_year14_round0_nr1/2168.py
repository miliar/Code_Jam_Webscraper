#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <assert.h>

using namespace std;

typedef long long ll;
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))

bool b[16];
bool k[16];

int t[4][4];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int q = 0; q < tests; q++)
	{
		int c;
		scanf("%d", &c);
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
		{
			scanf("%d", &t[i][j]);
			t[i][j]--;
		}
		fill(b, b + 16, 0);
		fill(k, k + 16, 0);
		for (int i = 0; i < 4; i++)
			b[t[c - 1][i]] = 1;
		scanf("%d", &c);
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
		{
			scanf("%d", &t[i][j]);
			t[i][j]--;
		}
		for (int i = 0; i < 4; i++)
			k[t[c - 1][i]] = 1;
		int u = 0;
		for (int i = 0; i < 16; i++)
		{
			if (b[i] && k[i])
				u++;
		}
		printf("Case #%d: ", q + 1);
		if (u == 0)
		{
			printf("Volunteer cheated!\n");
		}
		if (u == 1)
		{
			for (int i = 0; i < 16; i++)
			{
				if (b[i] && k[i])
				{
					printf("%d\n", i + 1);
					break;
				}
			}
		}
		if (u > 1)
		{
			printf("Bad magician!\n");
		}
	}
	return 0;
}