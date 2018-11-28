#include <cstdio>
#include <cstdlib>

struct tCell {

	int		vscore;
	int		hscore;
	int		ldscore;
	int		rdscore;
	int		symbol;
};

int main ()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out1s.txt", "w", stdout); 

		int		tc, i, j, k, wx, wy;
		char	arr[4];
		bool	game;
		bool	unfinished;

	scanf("%d", &tc);

	for (i = 1; i <= tc; i++) {

		unfinished = game = false;
		tCell	grid[4][4] = {0};

		for (j = 0; j < 4; j++)	{

			scanf("%s", arr);

			for (k = 0; k < 4; k++)	{

				grid[j][k].symbol = arr[k];

				if (arr[k] != '.' && game == false) {

					// left direction
					if (k - 1 >= 0 && (grid[j][k-1].symbol == arr[k] || arr[k] == 'T' || grid[j][k-1].symbol == 'T'))
						grid[j][k].hscore = grid[j][k-1].hscore + 1;

					// up direction
					if (j - 1 >= 0 && (grid[j-1][k].symbol == arr[k] || arr[k] == 'T' || grid[j-1][k].symbol == 'T'))
						grid[j][k].vscore = grid[j-1][k].vscore + 1;

					// left diagnol
					if (j == k && j - 1 >= 0 && k - 1 >= 0 && (grid[j-1][k-1].symbol == arr[k] || arr[k] == 'T' || grid[j-1][k-1].symbol == 'T'))
						grid[j][k].ldscore = grid[j-1][k-1].ldscore + 1;

					// right diagnol
					if (j + k == 3 && j - 1 >= 0 && k + 1 <= 3 && (grid[j-1][k+1].symbol == arr[k] || arr[k] == 'T' || grid[j-1][k+1].symbol == 'T'))
						grid[j][k].rdscore = grid[j-1][k+1].rdscore + 1;

					if (grid[j][k].vscore == 3) {

						game = true;
						wx = (grid[j][k].symbol == 'T') ? j-1 : j;
						wy = k;

					} else if (grid[j][k].hscore == 3) {

						game = true;
						wx = j;
						wy = (grid[j][k].symbol == 'T') ? k-1 : k;

					} else if (grid[j][k].ldscore == 3) {

						game = true;
						wx = (grid[j][k].symbol == 'T') ? j-1 : j;
						wy = (grid[j][k].symbol == 'T') ? k-1 : k;

					} else if (grid[j][k].rdscore == 3) {

						game = true;
						wx = (grid[j][k].symbol == 'T') ? j-1 : j;
						wy = (grid[j][k].symbol == 'T') ? k+1 : k;
					}

				} else
					unfinished = true;
			}
		}

		if (game)
			printf ("Case #%d: %c won\n", i, grid[wx][wy].symbol);
		else if (unfinished)
			printf ("Case #%d: Game has not completed\n", i);
		else
			printf ("Case #%d: Draw\n", i);

	}

	return 0;
}