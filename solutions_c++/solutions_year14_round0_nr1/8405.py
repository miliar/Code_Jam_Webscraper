#include "stdafx.h"
#include <stdio.h>
#include <math.h>
#include <string.h>

int main()
{
	FILE *fpin = NULL,*fpout = NULL;
	unsigned int TCno = 0, i = 0,j=0,k=0;
	unsigned int Val,row1 = 0,row2 = 0;
	unsigned int arr[17] = {0,};
	unsigned int PossAnsCnt = 0;
	unsigned int PossAns = 0;
	unsigned int val = 0;


	fpin = fopen("A-small-attempt0.in","r");
	fpout = fopen("OutPut.out","w");

	fscanf(fpin,"%d",&TCno);
	
	for (i=1;i<=TCno;i++)
	{
		PossAnsCnt = 0;
		PossAns = 0;
		memset(arr,0,17*sizeof(unsigned int));

		fscanf(fpin,"%d",&row1);

		for (j=1;j<=4;j++)
		{
			for (k=1;k<=4;k++)
			{
				fscanf(fpin,"%d",&val);
				if (row1 == j)
				{
					arr[val] = 1;
				}
			}
		}

		fscanf(fpin,"%d",&row2);

		for (j=1;j<=4;j++)
		{
			for (k=1;k<=4;k++)
			{
				fscanf(fpin,"%d",&val);
				if (row2 == j)
				{
					if (arr[val] == 1)
					{
						PossAnsCnt++;
						PossAns = val;
					}
				}
			}
		}

		fprintf(fpout,"Case #%d: ",i);
		if(PossAnsCnt == 0)
			fprintf(fpout,"Volunteer cheated!\n");
		else if(PossAnsCnt == 1)
			fprintf(fpout,"%d\n",PossAns);
		else
			fprintf(fpout,"Bad magician!\n");

	}
    fclose(fpin);
	fclose(fpout);
	return 0;
}

