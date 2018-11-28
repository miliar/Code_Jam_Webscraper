#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int Tcases;

// Richard Wins
int results[3][4][4] =
{
	// Calculated by pen & paper.
	{
		{1, 0, 1, 0},
		{0, 0, 0, 0},
		{1, 0, 1, 0},
		{0, 0, 0, 0}
	},

	{
		{1, 1, 1, 1},
		{1, 1, 0, 1},
		{1, 0, 0, 0},
		{1, 1, 0, 1}
	},

	{
		{1, 1, 1, 1},
		{1, 1, 1, 1},
		{1, 1, 1, 0},
		{1, 1, 0, 0}
	}
};

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);

	scanf("%d", &Tcases);

	for(int i=0; i<Tcases; i++)
	{
		int x, r, c;
		scanf("%d %d %d", &x, &r, &c);

		printf("Case #%d: ", i + 1);

		if (x == 1) printf("GABRIEL\n");
		else results[x - 2][r-1][c-1] == 1 ? printf("RICHARD\n") : printf("GABRIEL\n");
	}

	return 0;
}