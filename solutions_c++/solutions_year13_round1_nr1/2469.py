// r1a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <math.h>



FILE *input;
double  r,T;
 double pi, res;

int _tmain(int argc, _TCHAR* argv[])
{
	
	int cases;
	double a,b,c;
	
	pi = 2 * asin(1.0);



	input = _wfopen (argv[1],L"r");

	fscanf(input, "%d ", &cases);

	for(int i=1; i<= cases; i++)
	{
		fscanf(input, "%lg %lg ",&r, &T);
		a=  2 ;
		b= ( 2*r -1);
		c= -T;
		res= ( -b + sqrt( b*b - 4 * a *c))/2/a;
		long int resi = res;

		printf("Case #%d: %ld\n", i, resi);
	}
	return 0;
}

