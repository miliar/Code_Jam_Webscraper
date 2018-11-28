#include <stdio.h>
#define NMAX 104
int A[NMAX][NMAX];
int T, n, m, solution;

void read()
{
	scanf ("%d%d", &n, &m);

	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
			scanf ("%d", &A[i][j]);
}

bool possiblePattern(int x, int y)
{
	bool possibleLine = true, possibleColumn = true; 
	
	for (int i = x; i <= n; i++)
		if (A[i][y] > A[x][y])		{	possibleLine = false;	break;	}

	for (int i = x; i >= 1; i--)
		if (A[i][y] > A[x][y])		{	possibleLine = false;	break;	}

	for (int i = y; i <= m; i++)
		if (A[x][i] > A[x][y])		{	possibleColumn = false;	break;	}

	for (int i = y; i >= 1; i--)
		if (A[x][i] > A[x][y])		{	possibleColumn = false;	break;	}

	return (possibleLine || possibleColumn);
}

bool solvable()
{
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
		{
			if (possiblePattern(i ,j))	continue;

			return false;
		}

	return true;
}


int main()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	scanf ("%d", &T);

	for (int i = 1; i <= T; i++)
	{
		read();
		solution = solvable();

		printf ("Case #%d: ", i);
		(solution)	?	printf ("YES\n")	:	printf ("NO\n");
	}

	return 0;
}