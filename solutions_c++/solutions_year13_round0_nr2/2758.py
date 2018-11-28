#include <cstdlib>
#include <cstdio>
#include <fstream>
#include <string>

using namespace std;

#define MAX_SIZE 101

int 	b[MAX_SIZE][MAX_SIZE];
int		a[MAX_SIZE][MAX_SIZE];
int		m, n;

void cutRowIfPossible(int row)
{
	int h = -1;

	for (int i = 0; i < n; i++)
	{
		if (b[row][i] > h) h = b[row][i];
	}

	for (int i = 0; i < n; i++)
	{
		a[row][i] = min(a[row][i], h);
	}
}


void cutColumnIfPossible(int col)
{
	int h = -1;

	for (int i = 0; i < m; i++)
	{
		if (b[i][col] > h) h = b[i][col];
	}

	for (int i = 0; i < m; i++)
	{
		a[i][col] = min(a[i][col], h);
	}
}


string solve()
{
	for (int i = 0; i < m; i++)
	{
		cutRowIfPossible(i);
	}

	for (int i = 0; i < n; i++)
	{
		cutColumnIfPossible(i);
	}

	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (a[i][j] != b[i][j]) return string("NO");
		}
	}

	return string("YES");
}


int main()
{
	fstream		f, g;
	int 		tests;

	f.open("in.txt", ios :: in);
	g.open("out.txt", ios :: out);

	f >> tests;
	for (int k = 1; k <= tests; k++)
	{
		f >> m >> n;
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				f >> b[i][j];
			}
		}

		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				a[i][j] = 100;
			}
		}

		g << "Case #" << k << ": " << solve() << endl;
	}


	f.close();
	g.close();

	return 0;
}

