#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>

using namespace std;


int main()
{
	int T;
	int R, C;
	char table[100][100];
	bool achanger[100][100][4];

	scanf("%d\n", &T);

	for(int t = 1; t <= T; t++)
	{
		fprintf(stderr, "Cas %d\n", t);
		printf("Case #%d: ", t);

		scanf("%d %d\n", &R, &C);

		for(int i = 0; i < R; i++)
		{
			for(int j = 0; j < C; j++)
			{
				scanf("%c", &table[i][j]);
				for(int k = 0; k < 4; k++) achanger[i][j][k] = false;
			}
			scanf("\n");
		}

		bool trouve;
		int prem, der;

		for(int i = 0; i < R; i++)
		{
			trouve = false;
			for(int j = 0; j < C; j++)
			{
				if(table[i][j] != '.')
				{
					if(!trouve) prem = j;
					trouve = true;
					der = j;
				}
			}
			if(trouve)
			{
				achanger[i][prem][0] = true;
				achanger[i][der][1] = true;
			}
		}

		for(int i = 0; i < C; i++)
		{
			trouve = false;
			for(int j = 0; j < R; j++)
			{
				if(table[j][i] != '.')
				{
					if(!trouve) prem = j;
					trouve = true;
					der = j;
				}
			}
			if(trouve)
			{
				achanger[prem][i][2] = true;
				achanger[der][i][3] = true;
			}
		}

		bool possible = true;
		int combien = 0;

		for(int i = 0; i < R; i++)
		{
			for(int j = 0; j < C; j++)
			{
				int quel = -1;
				if(table[i][j] == '<') quel = 0;
				else if(table[i][j] == '>') quel = 1;
				else if(table[i][j] == '^') quel = 2;
				else if(table[i][j] == 'v') quel = 3;
				if(quel != -1)
				{
					if(achanger[i][j][quel])
					{
						bool ok = false;
						for(int k = 0; k < 4; k++)
						{
							if(!achanger[i][j][k]) ok = true;
						}
						if(!ok)
						{
							possible = false;
						}
						else combien++;
					}
				}
			}
		}

		if(possible) printf("%d\n", combien);
		else printf("IMPOSSIBLE\n");

	}

	return 0;
}
