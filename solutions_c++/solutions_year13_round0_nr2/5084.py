#include <stdio.h>
#include <stdlib.h>
#include <iostream>

int lawn[100][100];
int lawn_col, lawn_row;

int checked_horz[100][101];
int checked_vert[100][101];

int max_horz[100];
int max_vert[100];

bool check_horz(int r, int h);
bool check_vert(int r, int h);

int main()
{
	int case_total, case_current;
	int i, j;
	int max;
	bool c;

	scanf("%d", &case_total);

	for (case_current = 1; case_current <= case_total; case_current++)
	{
		scanf("%d %d", &lawn_row, &lawn_col);

		max = 0;

		for (i = 0; i < lawn_row; i++)
		{
			for (j = 0; j < lawn_col; j++)
			{
				scanf("%d", &lawn[i][j]);
				if (lawn[i][j] > max_horz[i]) max_horz[i] = lawn[i][j];
				if (lawn[i][j] > max_vert[j]) max_vert[j] = lawn[i][j];
				if (lawn[i][j] > max) max = lawn[i][j];
			}
		}

		c = true;

		for (i = 0; i < lawn_row && c; i++)
		{
			c = check_horz(i, max_horz[i]);
		}

		for (i = 0; i < lawn_col && c; i++)
		{
			c = check_vert(i, max_vert[i]);
		}

		printf("Case #%d: %s\n", case_current, (c) ? "YES" : "NO");

		for (i = 0; i < lawn_row; i++)
		{
			for (j = 0; j <= max; j++)
			{
				checked_horz[i][j] = 0;
			}
			max_horz[i] = 0;
		}

		for (i = 0; i < lawn_col; i++)
		{
			for (j = 0; j <= max; j++)
			{
				checked_vert[i][j] = 0;
			}
			max_vert[i] = 0;
		}
	}

	return 0;
}

bool check_horz(int r, int h)
{
	int i;
	bool check;

	if (checked_horz[r][h] != 0)
	{
		return (checked_horz[r][h] > 0) ? true : false;
	}

	for (i = 0; i < lawn_col; i++)
	{
		if (lawn[r][i] < h)
		{
			check = check_vert(i, lawn[r][i]);
			if (!check)
			{
				checked_horz[r][h] = -1;
				return false;
			}
		}
		else if (lawn[r][i] > h)
		{
			checked_horz[r][h] = -1;
			return false;
		}
	}

	checked_horz[r][h] = 1;
	return true;
}

bool check_vert(int r, int h)
{
	int i;
	bool check;

	if (checked_vert[r][h] != 0)
	{
		return (checked_vert[r][h] > 0) ? true : false;
	}

	for (i = 0; i < lawn_row; i++)
	{
		if (lawn[i][r] < h)
		{
			check = check_horz(i, lawn[i][r]);
			if (!check)
			{
				checked_vert[r][h] = -1;
				return false;
			}
		}
		else if (lawn[i][r] > h)
		{
			checked_vert[r][h] = -1;
			return false;
		}
	}

	checked_vert[r][h] = 1;
	return true;
}
