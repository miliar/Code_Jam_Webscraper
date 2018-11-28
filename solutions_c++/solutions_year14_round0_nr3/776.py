#include <algorithm>
#include <cstdio>
using namespace std;

int main(void)
{
	int cases;
	scanf("%i", &cases);
	for (int t = 0; t < cases; ++t)
	{
		int rows, cols, mines;
		scanf("%i %i %i", &rows, &cols, &mines);
		bool swapped = false;
		if (rows > cols)
		{
			swap(rows, cols);
			swapped = true;
		}
		int free = rows*cols - mines;
		printf("Case #%i:\n", t+1);
		// Setup.
		bool possible = false;
		char board[50][51];
		for (int r = 0; r < rows; ++r)
		{
			for (int c = 0; c < cols; ++c)
				board[r][c] = '*';
			board[r][cols] = '\0';
		}
		board[0][0] = 'c';
		// Solve, cols >= rows
		if (free == 1)
		{
			possible = true;
		}
		else if (rows == 1)
		{
			for (int i = 1; i < free; ++i)
				board[0][i] = '.';
			possible = true;
		}
		else if (rows == 2)
		{
			if (free >= 4 && free % 2 == 0)
			{
				board[1][0] = '.';
				for (int i = 1; i < free/2; ++i)
				{
					board[0][i] = '.';
					board[1][i] = '.';
				}
				possible = true;
			}
		}
		else // cols >= rows >= 3
		{
			if (free == 4)
			{
				board[0][1] = '.';
				board[1][0] = '.';
				board[1][1] = '.';
				possible = true;
			}
			else if (free == 6 || free >= 8)
			{
				// Fill the two first rows
				board[1][0] = '.';
				int freeLeft = free - 2;
				for (int i = 1; i < cols && freeLeft >= 4; ++i)
				{
					board[0][i] = '.';
					board[1][i] = '.';
					freeLeft -= 2;
				}
				for (int curRow = 2; freeLeft > 0; ++curRow)
				{
					if (freeLeft == cols+1)
					{
						// Put two on the next row, there cannot be one alone one on a row.
						board[curRow+1][0] = '.';
						board[curRow+1][1] = '.';
						freeLeft -= 2;
					}
					for (int i = 0; i < cols && freeLeft > 0; ++i)
					{
						board[curRow][i] = '.';
						--freeLeft;
					}
				}
				possible = true;
			}
		}
		// Print result
		if (possible)
		{
			if (swapped)
			{
				for (int c = 0; c < cols; ++c)
				{
					for (int r = 0; r < rows; ++r)
						printf("%c", board[r][c]);
					printf("\n");
				}
			}
			else
			{
				for (int r = 0; r < rows; ++r)
					printf("%s\n", board[r]);
			}
		}
		else
			printf("Impossible\n");
	}
	return 0;
}
