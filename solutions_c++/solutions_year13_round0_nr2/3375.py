#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int m, n;
int field[100][100];
int maxrows[100];
int maxcols[100];
bool ok[100][100];

void test(int i, int j)
{
	if (field[i][j] == maxrows[i] || field[i][j] == maxcols[j])
	{
		ok[i][j] = true;
	}
}

bool test(void)
{
	int i, j;
	
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < m; j++)
		{
			if (!ok[i][j])
			{
				return false;
			}
		}
	}
	return true;
}

int main()
{
	int t;
	int cases;
	int i, j;
	
	scanf("%d", &t);
	for (cases = 1; cases <= t; cases++)
	{
		printf("Case #%d: ", cases);
		
		scanf("%d %d", &n, &m);
		
		for (i = 0; i < n; i++)
		{
			for (j = 0; j < m; j++)
			{
				scanf("%d", &field[i][j]);
				ok[i][j] = false;
			}
		}
		
		for (i = 0; i < n; i++)
		{
			maxrows[i] = 0;
		}
		
		for (j = 0; j < m; j++)
		{
			maxcols[j] = 0;
		}
		
		for (i = 0; i < n; i++)
		{
			for (j = 0; j < m; j++)
			{
				maxrows[i] = max(maxrows[i], field[i][j]);
			}
		}
		
		for (j = 0; j < m; j++)
		{
			for (i = 0; i < n; i++)
			{
				maxcols[j] = max(maxcols[j], field[i][j]);
			}
		}
		
		for (i = 0; i < n; i++)
		{
			for (j = 0; j < m; j++)
			{
				test(i, j);
			}
		}
		
		if (test())
		{
			printf("YES");
		}
		else
		{
			printf("NO");
		}
		
		printf("\n");
	}
	
	return 0;
}
