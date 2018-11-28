

#include "stdio.h"
#include "stdlib.h"


int main()
{
	int a[4][4],b[4][4],t,i,j,q1,q2,iCount = 0,iEqual,iNum;
	FILE *fpin,*fpout;

	fpin = fopen("A-small-attempt4.in","r");
	fpout = fopen("A-small-attempt4.out","w");
	fscanf(fpin,"%d",&t);
	while(t--)
	{
		iEqual = 0;
		iCount++;
		fscanf(fpin,"%d",&q1);
		for (i = 0;i < 4;i++)
			for (j = 0;j < 4;j++)
				fscanf(fpin,"%d",&a[i][j]);
		fscanf(fpin,"%d",&q2);
		for (i = 0;i < 4;i++)
			for (j = 0;j < 4;j++)
				fscanf(fpin,"%d",&b[i][j]);
		for (i = 0;i < 4;i++)
			for (j = 0;j < 4;j++)
				if (a[q1 - 1][i] == b[q2 - 1][j])
				{
					iEqual++;
					iNum = a[q1 - 1][i];
				}
		fprintf(fpout,"Case #%d: ",iCount);
		if (iEqual == 0)
			fprintf(fpout,"Volunteer cheated!");
		if (iEqual == 1)
			fprintf(fpout,"%d",iNum);
		if (iEqual > 1)
			fprintf(fpout,"Bad magician!");
		if (t >= 1)
			fprintf(fpout,"\n");
	}
	fclose(fpin);
	fclose(fpout);
	return 0;
}

