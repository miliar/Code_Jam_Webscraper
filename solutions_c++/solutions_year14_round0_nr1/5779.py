#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

int main()
{
	int t;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		unsigned short int a = 0, b = 0;
		int r1, r2;
		scanf("%d", &r1);
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				int l;
				scanf("%d", &l);
				if (j == r1 - 1)
				{
					a |= 1 << (l - 1);
				}
			}
		}
		scanf("%d", &r1);
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				int l;
				scanf("%d", &l);
				if (j == r1 - 1)
				{
					b |= 1 << (l - 1);
				}
			}
		}
		unsigned short int n = a & b;
		printf("Case #%d: ", i);
		if (!n)
		{
			printf("Volunteer cheated!");
		}
		else if (!(n & (n - 1)))
		{
			int j;
			for (j = 0; j < 16; j++)
			{
				if (n & (1 << j))
				{
					break;
				}
			}
			printf("%d", j + 1);
		}
		else
		{
			printf("Bad magician!");
		}
		printf("\n");
	}
	return 0;
}