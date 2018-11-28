#include <iostream>
#include <cstdio>
using namespace std;

int t;
int a, b, k;
int wyn;
int p;

int main()
{
	scanf("%d", &t);
	for (int h=1; h<=t; h++)
	{
		scanf("%d%d%d", &a, &b, &k);
		wyn=0;
		for (int i=0; i<a; i++)
		{
			for (int j=0; j<b; j++)
			{
				p=i&j;
				if (p<k)
				wyn++;
			}
		}
		printf("Case #%d: %d\n", h, wyn);
	}
	return 0;
}
