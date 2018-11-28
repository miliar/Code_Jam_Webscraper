// CodeJam_B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

int _tmain(int argc, _TCHAR* argv[])
{
	int T,t;
	long float F,C,X, time=0.0, r=2.0;

	errno_t err;
	FILE *ip;
	err = fopen_s(&ip,"B-large.txt","r");
	fscanf_s(ip,"%d", &T);

	errno_t errOp;
	FILE *op;
	errOp = fopen_s(&op,"outputLargeB.txt", "w");

	for (t=1; t <= T; t++)
	{
		time = 0.0; r = 2.0;
		fscanf_s(ip,"%lf %lf %lf", &C, &F, &X);	
		while ( X/r > C/r + X/(r+F) )
		{
				time += C/r;
				r += F;
		}
		time += X/r;
		fprintf_s(op,"Case #%d: %f\n", t,time);
	}

	return 0;
}