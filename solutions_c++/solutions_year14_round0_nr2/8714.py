// cookies.cpp : Defines the entry point for the console application.
//

// magic.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include "stdio.h"


int _tmain(int argc, char* argv[])
{
	FILE* inputFile;
	FILE*outputFile;
	errno_t err1 = fopen_s(&inputFile, "B-large.in", "r");
	errno_t err2 = fopen_s(&outputFile, "B-large.ou", "w+");
	
	int numpreOfAttempt;
	double c, f, x;
	//c - farm cost
	//f - increase
	//x - target
	if(!err1 || !err2)
	{
		fscanf_s(inputFile, "%d", &numpreOfAttempt);
		for(int i=0; i<numpreOfAttempt; i++)
		{
			fscanf_s(inputFile, "%lf %lf %lf", &c, &f, &x);
			double ce = c, fe = f, ix = x;
			double cookies = 0.0;
			double currentCookisRate = 2.0;
			double t;
			if(c >= x)
			{
				t = x/currentCookisRate;
			}
			else
			{
				bool war = true;
				t = 0.0;
				while(war)
				{
					if(x/currentCookisRate < (c/currentCookisRate + x/(currentCookisRate+f)))
					{
						t =  t + x/currentCookisRate;
						war = false;
					}
					else
					{
						t = t + c/currentCookisRate;
						currentCookisRate = currentCookisRate +f;
					}
				}
			}
			fprintf_s(outputFile,"Case #%d: %.7f\n", i+1, t);

		}
		fclose(inputFile);
		fclose(outputFile);
	}
	return 0;
}


