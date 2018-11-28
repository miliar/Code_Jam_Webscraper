// A-Small.cpp : main project file.

//#include "stdafx.h"
#include <stdio.h>

bool v[17];

int main()
{
	/*freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);*/

	int t, r1, r2, aux;
	scanf("%d", &t);
	for (int z = 1; z <= t; z++)
	{
		scanf("%d", &r1);
		for (int i = 1; i <= 16; i++)
			v[i] = false;

		for (int i = 1; i <= 4; i++)
			for (int j = 0; j < 4; j++)
			{
				scanf("%d", &aux);
				if (i == r1)
					v[aux] = true;
			}

		scanf("%d", &r2);
		int nFound = 0, f;
		for (int i = 1; i <= 4; i++)
			for (int j = 0; j < 4; j++)
			{
				scanf("%d", &aux);
				if (i == r2 && v[aux])
				{
					nFound++;
					f = aux;
				}
			}

		if (nFound < 1)
			printf("Case #%d: Volunteer cheated!\n", z);
		else if (nFound == 1)
			printf("Case #%d: %d\n", z, f);
		else
			printf("Case #%d: Bad magician!\n", z);
	}
    return 0;
}
