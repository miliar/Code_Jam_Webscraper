#include <stdio.h>
#include <iostream>
#include <cmath>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
const int nMax=10000+4;
int m[nMax];
int main()
{
	//FILE *in = fopen("input.txt", "r");
	FILE *in = fopen("A-large.in", "r");
	FILE *out = fopen("output.txt", "w");
	int t, q, i, n, x, y, sum=0, d=0;
    fscanf(in, "%d", &t);
  	for (q=1;q<=t; q++) 
	{
		fscanf(in, "%d", &n);
		fscanf(in, "%d", &m[0]);
		int maxD=0;
		d=0;
		for (i=1; i<n; i++)
			{
				sum+=m[i-1];
				fscanf(in, "%d", &m[i]);
				if (m[i]<m[i-1]) 
				{
					d+=m[i-1]-m[i];
					if (m[i-1]-m[i]>maxD) maxD=m[i-1]-m[i];
				}
			}
		sum=0;	
		for (i=0; i<n-1; i++)
			{
				if (m[i]>maxD)
					sum+=maxD;
				else
					sum+=m[i];
			}
    	fprintf(out, "Case #%d: %d %d\n", q, d, sum);
  	}
	fclose(in);
    fclose(out);
return(0);
}
