#include <cstdio>

long int limit = 6;
char MatchChar;
bool foundT, foundEmpty, winnerX, winnerO;
int i, j, k, m;

int main ()
{
	FILE * pInFile;
	FILE * pOutFile;
	
	pInFile = fopen ("C:\\Users\\Lenovo-PC\\Desktop\\in.txt","r");
	pOutFile = fopen ("C:\\Users\\Lenovo-PC\\Desktop\\out.txt","w");

	for (i = 1; i <= limit; i++)
	{
		char TestArray[4][5] = {"\0"};
		fscanf (pInFile, "%s", &TestArray[0]);
		fscanf (pInFile, "%s", &TestArray[1]);
		fscanf (pInFile, "%s", &TestArray[2]);
		fscanf (pInFile, "%s", &TestArray[3]);

		winnerX = false;
		winnerO = false;
		foundEmpty = false;
		for (j = 0; j < 4 ; j++)
		{
			// For Rows
			k = 0;
			foundT = false;
			MatchChar = TestArray[j][k];
			if (MatchChar == 'T')
			{
				foundT = true;
				k = 1;
				MatchChar = TestArray[j][k];
			}

			if (MatchChar != '.')
			{	
				for (m = k + 1; m < 4; m++)
				{
					if(TestArray[j][m] == MatchChar)
					{
						continue;
					}
					else if (foundT == false && TestArray[j][m] == 'T')
					{
						foundT = true;
						continue;
					}
					else
						break;
				}

				if (m == 4)
				{
					if (MatchChar == 'X')
						winnerX = true;
					else
						winnerO = true;

					break;
				}
			}
			else
			{
				foundEmpty = true;
			}

			// For Columns
			k = 0;
			foundT = false;
			MatchChar = TestArray[k][j];
			if (MatchChar == 'T')
			{
				foundT = true;
				k = 1;
				MatchChar = TestArray[k][j];
			}

			if (MatchChar != '.')
			{	
				for (m = k + 1; m < 4; m++)
				{
					if(TestArray[m][j] == MatchChar)
					{
						continue;
					}
					else if (foundT == false && TestArray[m][j] == 'T')
					{
						foundT = true;
						continue;
					}
					else
						break;
				}

				if (m == 4)
				{
					if (MatchChar == 'X')
						winnerX = true;
					else
						winnerO = true;

					break;
				}
			}
			else
			{
				foundEmpty = true;
			}
		}

		// For Left Diagonal
		if(winnerX == false && winnerO == false)
		{
			k = 0;
			foundT = false;
			MatchChar = TestArray[k][k];
			if (MatchChar == 'T')
			{
				foundT = true;
				k = 1;
				MatchChar = TestArray[k][k];
			}

			if (MatchChar != '.')
			{
				for (m = k + 1; m < 4; m++)
				{
					if(TestArray[m][m] == MatchChar)
					{
						continue;
					}
					else if (foundT == false && TestArray[m][m] == 'T')
					{
						foundT = true;
						continue;
					}
					else
						break;
				}

				if (m == 4)
				{
					if (MatchChar == 'X')
						winnerX = true;
					else
						winnerO = true;
				}
			}
			else
			{
				foundEmpty = true;
			}
		}

		// For Right Diagonal
		if(winnerX == false && winnerO == false)
		{
			k = 0;
			m = 3;
			foundT = false;
			MatchChar = TestArray[k][m];
			if (MatchChar == 'T')
			{
				foundT = true;
				k = k + 1;
				m = m - 1;
				MatchChar = TestArray[k][m];
			}

			if (MatchChar != '.')
			{
				for (m = m - 1; m >= 0; m--)
				{
					k = k + 1;
					if(TestArray[k][m] == MatchChar)
					{
						continue;
					}
					else if (foundT == false && TestArray[k][m] == 'T')
					{
						foundT = true;
						continue;
					}
					else
						break;
				}

				if (m == -1)
				{
					if (MatchChar == 'X')
						winnerX = true;
					else
						winnerO = true;
				}
			}
			else
			{
				foundEmpty = true;
			}
		}

		fprintf (pOutFile, "Case #%d: ", i);
		if(winnerX == false && winnerO == false && foundEmpty == true)
			fprintf (pOutFile, "%s\n", "Game has not completed");
		else if(winnerX == false && winnerO == false && foundEmpty == false)
			fprintf (pOutFile, "%s\n", "Draw");
		else if(winnerX == true && winnerO == false)
			fprintf (pOutFile, "%s\n", "X won");
		else if(winnerX == false && winnerO == true)
			fprintf (pOutFile, "%s\n", "O won");
	}

	fclose (pInFile);
	fclose (pOutFile);
	printf("\nOutput Generated!!!");
	scanf("END");
    return 0;
}