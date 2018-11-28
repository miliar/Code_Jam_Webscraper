#include "stdafx.h"
#include <stdio.h>
#include <math.h>
#include <string.h>

int main()
{
	FILE *fpin = NULL,*fpout = NULL;
	unsigned int TCno = 0, Flag = 0 , i = 0;
	double C = 0.0 ,F = 0.0,X = 0.0, time = 0.0, tempTime = 0.0;
	double CperS = 2.0;
	double CurrC = 0.0;

	fpin = fopen("B-large.in","r");
	fpout = fopen("OutPut.out","w");

	fscanf(fpin,"%d",&TCno);
	
	for (i=1;i<=TCno;i++)
	{
		time = 0.0;
		CurrC = 0.0;
		CperS = 2.0;
		Flag = 0;
		fscanf(fpin,"%lf",&C);
		fscanf(fpin,"%lf",&F);
		fscanf(fpin,"%lf",&X);

		while (1)
		{
			if(Flag || (C >= (X - CurrC)))
			{
				time += (X-CurrC)/CperS;
				fprintf(fpout,"Case #%d: %.7lf\n",i,time);
				break;
			}

			time += C/CperS;
			CurrC += C;

			if ((X-CurrC)/CperS > X/(CperS + F))
			{
				CperS += F;
				CurrC -= C;
			}
			else 
			{
				Flag = 1;
			}
		}
	}

    fclose(fpin);
	fclose(fpout);
	return 0;
}

