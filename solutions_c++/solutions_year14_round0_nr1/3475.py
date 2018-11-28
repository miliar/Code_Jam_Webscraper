// MagicTrick.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>

int cardset1[4][4];
int cardset2[4][4];
int numberoftests=0;

int main(int argc, char* argv[])
{
	FILE *fp;

	int row1=0, row2=0, matchno=0, matchcount=0, j=1;
	fp = fopen("c:\\small.in", "r");
	fscanf(fp, "%d", &numberoftests);

	if ( ( numberoftests < 0) || (numberoftests > 100) )
	{
		printf("Wrong number of test cases\n");
		return 0;
	}

	while (numberoftests--)
	{
		fscanf(fp, "%d", &row1);
		
		for (int i=0; i<4; i++)
			fscanf(fp, "%d %d %d %d", &cardset1[i][0], &cardset1[i][1], &cardset1[i][2], &cardset1[i][3]);
		
		fscanf(fp, "%d", &row2);

		for (i=0; i<4; i++)
			fscanf(fp, "%d %d %d %d", &cardset2[i][0], &cardset2[i][1], &cardset2[i][2], &cardset2[i][3]);

		row1--;
		row2--;
		
		if ( ( cardset1[row1][0] == cardset2[row2][0] ) || ( cardset1[row1][0] == cardset2[row2][1] )  || ( cardset1[row1][0] == cardset2[row2][2] ) || ( cardset1[row1][0] == cardset2[row2][3] ) )
		{
			matchno = cardset1[row1][0];
			matchcount++;
		}
			
		if ( ( cardset1[row1][1] == cardset2[row2][0] ) || ( cardset1[row1][1] == cardset2[row2][1] ) || ( cardset1[row1][1] == cardset2[row2][2] ) || ( cardset1[row1][1] == cardset2[row2][3] ) )
		{
			matchno = cardset1[row1][1];
			matchcount++;
		}

		if ( ( cardset1[row1][2] == cardset2[row2][0] ) || ( cardset1[row1][2] == cardset2[row2][1] ) || ( cardset1[row1][2] == cardset2[row2][2] ) || ( cardset1[row1][2] == cardset2[row2][3] ) )
		{
			matchno = cardset1[row1][2];
			matchcount++;
		}

		if ( ( cardset1[row1][3] == cardset2[row2][0] ) || ( cardset1[row1][3] == cardset2[row2][1] ) || ( cardset1[row1][3] == cardset2[row2][2] ) || ( cardset1[row1][3] == cardset2[row2][3] ) )
		{
			matchno = cardset1[row1][3];
			matchcount++;
		}

		if (matchcount == 1)
		{

			printf("Case #%d: %d\n", j, matchno);
		}
		else if (matchcount > 1)
		{
			printf("Case #%d: Bad magician! \n", j);
		}
		else if (matchcount == 0)
		{
			printf("Case #%d: Volunteer cheated! \n", j);
		}
		j++;
		matchcount=0;
		matchno=0;
	}
	
	return 0;
}