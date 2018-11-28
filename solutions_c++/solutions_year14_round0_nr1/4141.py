#include <cstdio>

int cards1[4][4];
int cards2[4][4];

int main()
{
    int T,row1,row2,common,magic,i,j;
    scanf("%i", &T);
	int z;
    for(int t=1; t<=T; t++)
    {
		scanf("%i",&row1);
		for(i = 0; i < 4; i++)
		{
			for(j = 0; j < 4; j++)
			{
				scanf("%i", &cards1[i][j]);
			}
		}

		scanf("%i",&row2);
		for(i = 0; i < 4; i++)
		{
			for(j = 0; j < 4; j++)
			{
				scanf("%i", &cards2[i][j]);
			}
		}

		row1--;
		row2--;
		common = 0;

		for(i = 0; i < 4; i++)
		{
			for(j = 0; j < 4; j++)
			{
				if (cards1[row1][i]==cards2[row2][j])
				{
					magic = cards1[row1][i];
					common++;
					break;
				}
			}
		}

		if (common == 0)
			printf("Case #%i: Volunteer cheated!\n", t);
		else if (common > 1)
			printf("Case #%i: Bad magician!\n", t);
		else
			printf("Case #%i: %i\n", t, magic);
	}
}

