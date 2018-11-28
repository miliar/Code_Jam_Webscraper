#include <stdio.h>
#include <string.h>

#define MaxT 1000
char table[4][4];

bool playerX[2][4], playerO[2][4]; //0: row, 1:col
bool diogonalX[2],diogonalO[2];

int main()
{
	int T, i, j, k;
	char inp, str[20];
	int winner;
	bool notCompleted;
	FILE * ffile, *ffile2;
	ffile = fopen("A-small-attempt3.in", "r");
	ffile2 = fopen("A-small-attempt3.out", "w");
	//scanf("%d", &T);
	//fflush(ffile);
	fgets(str, 5, ffile);
	sscanf(str, "%d", &T); 
	for (k = 1; k <= T; k++)
	{
		memset(playerX, true, 14*sizeof(bool));
		memset(playerO, true, 14*sizeof(bool));
		memset(diogonalO, true, 2*sizeof(bool));
		memset(diogonalX, true, 2*sizeof(bool));
		winner = 0;
		notCompleted = false;
		for (i = 0; i < 4; i++)
		{
			
			//fflush(ffile);
			fgets(str, 10, ffile);
			if (str[strlen(str) - 1] == '\n')
				str[strlen(str) - 1] = '\0'; 
			for (j = 0; j < 4; j++)
			{
				inp = str[j];
				if (inp == '.')
					notCompleted = true;
				if (inp == 'X' || inp == '.') {
					
					playerO[0][i] = false;
					playerO[1][j] = false;
					if (i == j)
						diogonalO[0] = false;
					if (i + j == 3)
						diogonalO[1] = false;
				}

				if (inp == 'O' || inp == '.') {
					playerX[0][i] = false;
					playerX[1][j] = false;
					if (i == j)
						diogonalX[0] = false;
					if (i + j == 3)
						diogonalX[1] = false;
				}

			}
		}

		for (i = 0; i < 2; i++) {
			if (diogonalO[i] == true) {
				winner = 2;
				break;
			}
			if (diogonalX[i] == true) {
				winner = 1;
				break;
			}
				
			for (j = 0; j < 4; j++) {
				if (playerO[i][j] == true) {
					winner = 2;
					break;
				}
				if (playerX[i][j] == true) {
					winner = 1;
					break;
				}

			}
			if (winner != 0)
				break;
		}

		fprintf(ffile2, "Case #%d: ", k);
		if (winner == 0) {
			if (notCompleted)
				fprintf(ffile2, "Game has not completed\n");
			else fprintf(ffile2, "Draw\n");
		}
		else if (winner == 1)
			fprintf(ffile2, "X won\n");
		else if (winner == 2)
			fprintf(ffile2, "O won\n");
		
		//fflush(ffile);
		fgets(str, 5, ffile);
		
	}
	fclose(ffile);
	fclose(ffile2);
	return 0;
}
