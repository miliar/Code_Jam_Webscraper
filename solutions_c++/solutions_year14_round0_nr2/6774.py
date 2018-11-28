// Cookie Clicker Alpha.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdio.h>
#include <stdlib.h>


int main(int argc, char* argv[])
{
	FILE *fp, *fout;

	if (argc <= 2) return -1;

	fp=fopen(argv[1],"r");
	fout=fopen(argv[2],"w");
	
	if (!fp) return -2;

	long count;
	fscanf(fp,"%ld",&count);

	long i;
	for(i=0;i<count;i++)
	{
		double C,F,X;
		double rate = 2.0;
		fscanf(fp,"%lf",&C);
		fscanf(fp,"%lf",&F);
		fscanf(fp,"%lf",&X);

		double lapsed_time = 0.0;

		while(1)
		{
			lapsed_time += C/rate;
			if ((X-C)/rate <= X/(rate+F))
			{
				//Not need Building.
				lapsed_time+=(X-C)/rate;
				break;
			}
			else
			{
				//need building and next step
				rate += F;
			}
		}
		fprintf(fout,"Case #%d: %.7lf\n",i+1,lapsed_time);
	}
	
	if (fp) fclose(fp);
	if (fout) fclose(fout);

	return 0;
}

