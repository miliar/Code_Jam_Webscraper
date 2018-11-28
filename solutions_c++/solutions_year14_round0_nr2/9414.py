// prob2.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include "stdio.h"
#include "stdlib.h"


int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fpi;
	FILE *fpo;

	int nT;

	double nC, nF, nX;
	int flag;
	int i,j;
	int k;
	double tout;
	double tend;
	double tpre;
	double num;
	double kout;


	fpi = fopen("B-small-attempt0.in","r");
//	fpi = fopen("test2.txt","r");
	if (!fpi)
	{
		printf("Fail to open the input file!\n");
		exit(0);
	}
	
	fpo = fopen("B-small-attempt0.out","w");
//	fpo = fopen("output.out","w");
	if (!fpo)
	{
		printf("Fail to open the output file!\n");
		exit(0);
	}

	fscanf(fpi, "%d", &nT);
	for (k=0; k<nT; k++)
	{
		fscanf(fpi, "%lf", &nC);
		fscanf(fpi, "%lf", &nF);
		fscanf(fpi, "%lf", &nX);

		tout = 0;
		tend = 0;
		tpre = 0;
		num = 0;
		kout = 2.0;

		flag = 1;
		while (flag)
		{
			tend = tout + (nX-num) / kout;
			tpre = tout + nC/kout + nX/(kout+nF);
			if (tpre < tend)
			{
				tout = tout + nC/kout;
				kout = kout + nF;
			}
			else
			{
				tout = tend;
				flag = 0;
			}
		}

OUTPUT:
		fprintf(fpo, "Case #%d: %.7f\n", k+1, tout);

	}

	fclose(fpi);
	fclose(fpo);

	return 0;
}

