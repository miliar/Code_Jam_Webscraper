// Magic Trick.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdio.h>
#include <stdlib.h>

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fp, *fout;

	int count;
	int i,j,k,m;

	int idx=0;

	int choosen[2]={0,};
	int cards[8][4]={0,};

	fp = fopen("A-small-attempt0.in","r" );
	fout=fopen("output.txt","w");

	if (fp)
	{
		fscanf(fp,"%d", &count);
		
		for(i=0;i<count;i++)
		{
			//total case
			for(j=0;j<2;j++)
			{
				//guest choosen row
				fscanf(fp,"%d", &choosen[j]);
				choosen[j]+=j*4-1;

				for(k=0;k<4;k++)
				{
					//4card
					fscanf(fp,"%d", &cards[k+(j*4)][0]);
					fscanf(fp,"%d", &cards[k+(j*4)][1]);
					fscanf(fp,"%d", &cards[k+(j*4)][2]);
					fscanf(fp,"%d", &cards[k+(j*4)][3]);

					//printf("%d,%d,%d,%d\n",cards[k+j][0],cards[k+j][1],cards[k+j][2],cards[k+j][3]);
				}
			}
			
			int verify[4]={0,};
			int count=0;
			int latest_idx=-1;

			for(k=0;k<4;k++)
			{
				for(m=0;m<4;m++)
				{
					if (cards[choosen[0]][k] == cards[choosen[1]][m])
					{
						verify[k]++;
						latest_idx = k;
						count++;
					}
				}
			}

			if (count == 1)
			{
				fprintf(fout,"Case #%d: %d\n",i+1,cards[choosen[0]][latest_idx]);
			}
			else if(count > 1)
			{
				fprintf(fout,"Case #%d: Bad magician!\n",i+1);
			}
			else
			{
				fprintf(fout,"Case #%d: Volunteer cheated!\n",i+1);
			}

		}
	}

	

	if (fp)	fclose(fp);
	if (fout) fclose(fout);

	system("pause");

	return 0;
}

