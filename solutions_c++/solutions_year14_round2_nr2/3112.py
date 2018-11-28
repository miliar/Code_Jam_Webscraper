#include <iostream>
#include <stdio.h>
using namespace std;
#pragma warning (disable:4996)
int main()
{
	int a, b, c, t,m,z;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d",&t);
	for (int i = 1; i <= t; i++)
	{
			scanf("%d%d%d", &a, &b, &c);
			if ((c >= a) && (c >= b))
			{
				m = a*b;
			}
			else
			if ((c < a) && (c < b))
			{
				if (a>b)
				{
					m = c*a + (b - c)*c;
				}
				else
				{
					m = c*b + (a - c)*c;
				}
				for (int j = c; j < a; j++)
				{
					for (int k = c; k < b; k++)
					{
						z = j&k;
						if (c > z)
						{
							m++;
						}
					}
				}
			}
			else
			{
				m = 0;
				for (int j = 0; j < a; j++)
				{
					for (int k = 0; k < b; k++)
					{
						z = j&k;
						if (c > z)
						{
							m++;
						}
					}
				}
			}
			printf("Case #%d: %d\n", i, m);
	}
	return 0;
}