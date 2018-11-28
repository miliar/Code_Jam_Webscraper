#include <cstdio>
#include <cstdlib>

int original[4][4];
int nouveau[4][4];

int compteur;
int elmt;

int main()
{
		int nbCase;
		scanf("%d", &nbCase);
		for(int testCase = 0; testCase < nbCase; testCase++)
		{
				compteur = 0;
				int originalLine;
				scanf("%d", &originalLine);
				for(int i = 0; i < 4; ++i)
				{
						for(int j = 0; j < 4; ++j)
						{
								scanf("%d", &original[i][j]);
						}
				}
				int newLine;
				scanf("%d", &newLine);
				for(int i = 0; i < 4; ++i)
				{
						for(int j = 0; j < 4; ++j)
						{
								scanf("%d", &nouveau[i][j]);
						}
				}
				for(int i = 0; i < 4; ++i)
				{
						for(int j = 0; j < 4; ++j)
						{
								//printf("$$ %d -- %d\n", original[originalLine - 1][i], nouveau[newLine - 1][j]);
								if(original[originalLine- 1][i] == nouveau[newLine - 1][j])
								{
										compteur++;
										elmt = original[originalLine - 1][i];
								}
						}
				}
				printf("Case #%d: ", (testCase+1));
				if(compteur == 1)
				{
						printf("%d\n", elmt);
				}
				else if(compteur == 0)
				{
						printf("Volunteer cheated!\n");
				}
				else if(compteur > 1)
				{
						printf("Bad magician!\n");
				}
		}
		return 0;
}
