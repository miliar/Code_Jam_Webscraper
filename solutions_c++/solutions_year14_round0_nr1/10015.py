//codejam 1
#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int T,grid1[4],i,j,row1,row2,grid2[4],faltu;
	//freopen("A-small-attempt2.in", "r", stdin);
	//freopen("A-small-attempt2.out", "w",stdout);
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d", &row1);
		
		for (i = 0; i < 4; i++)
		{
			if (i == row1 - 1)  //no zeroth row
				for (j = 0; j < 4; j++)
					scanf("%d", &grid1[j]);
			else for (j = 0; j < 4; j++)
				scanf("%d", &faltu);
		}

		scanf("%d", &row2);
		for (i = 0; i < 4; i++)
		{
			if (i == row2 - 1)  //no zeroth row
				for (j = 0; j < 4; j++)
					scanf("%d", &grid2[j]);
			else for (j = 0; j < 4; j++)
				scanf("%d", &faltu);
		}
		int match = -1;
		for (i = 0; i < 4; i++)
			if (match != -2){
				for (j = 0; j < 4; j++)
				{
					if (grid1[i] == grid2[j])
					{
						if (match>=0)
						{
							match = -2; break;
						}
						else
							match = i;
					}
				}
			}
			
		static int cnt = 1;
		printf("Case #%d: ", cnt++);
		if (match >= 0)
			printf("%d", grid1[match]);
		else printf(match < -1 ? "Bad magician!" : "Volunteer cheated!");
		printf("\n");
		}
	return 0;
}