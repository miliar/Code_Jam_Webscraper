#include <stdio.h>

void main() 
{
	FILE *in = fopen("B-large.in", "r");
	FILE *out = fopen("B-large.out", "w");
	
	double C, F, X, tpc, total, t1, t2;	// 농장비용, 증가량, 목표량
	int n, N;
	int i, j;

	fscanf(in,"%d",&N);

	n=0;
	while(n<N) 
	{
		fscanf(in,"%lf %lf %lf",&C, &F, &X);
		
		tpc = 2.0;
		total = 0.0;
		while(1) 
		{
			t1 = total + (X/tpc);
			t2 = total + (C/tpc) + (X/(tpc+F));

			if(t1 > t2)	// buying farm
			{
				total += C/tpc;
				tpc += F;
			}
			else	// no buying
			{
				total += X/tpc;
				break;
			}
		}

		fprintf(out,"Case #%d: %.7lf\n",n+1,total);	
		++n;
	}

}