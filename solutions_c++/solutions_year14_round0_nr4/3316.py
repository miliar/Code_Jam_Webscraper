// dwar.cpp : Defines the entry point for the console application.
//



#include "stdafx.h"
#include <stdio.h>

int main(int argc, char* argv[])
{
	int T, N, w, dw,i;
	double naomi[1000], ken[1000], tmp;
	FILE *fp;
	fp = fopen("c:\\small.in", "r");

	fscanf(fp, "%d", &T);

	for (int tc = 0; tc<T; tc++)
	{
		dw = w = 0;
		fscanf(fp, "%d", &N);

		for (int i=0; i<N; i++)
		fscanf(fp, "%lf", &naomi[i]);   
		for (i=0; i<N; i++)
		fscanf(fp, "%lf", &ken[i]); 

		for ( i=0; i<N; i++)
		{
			for (int j=i+1; j<N; j++)
			{
			if (naomi[i]> naomi[j])
			{
			tmp = naomi[i];
			naomi[i] = naomi[j];
			naomi[j] = tmp; 
			}
			}
		}

		for ( i=0; i<N; i++)
		{
			for ( int j=i+1; j<N; j++)
			{
			if (ken[i]> ken[j])
			{
			tmp = ken[i];
			ken[i] = ken[j];
			ken[j] = tmp; 
			}
			}
		}

		int ix = 0;
		for ( i=0; i<N; i++)
		for ( int j=ix; j<N; j++)
		if (naomi[i] > ken[j])
		{
			ix = j+1;
			dw++;
			break;    
		}

		ix = N-1;
		for (i=N-1; i>=0; i--)
		{
			for (int j=ix; j>=0; j--)
			{
				if (naomi[i] > ken[j])
				{
				w++;
				break;    
				}
				else
				{
				ix = j-1;
				break;
				}
			}
		}
		printf("Case #%d: %d %d\n", tc+1, dw, w);
	}
	fclose(fp);
	return 0;
}
