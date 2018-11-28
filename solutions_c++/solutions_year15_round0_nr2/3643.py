#include <stdio.h>
#include <iostream>
#include <cmath>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int a[1003];
int main()
{
	//FILE *in = fopen("input.txt", "r");
	FILE *in = fopen("1.in", "r");
	FILE *out = fopen("output.txt", "w");
	int t, q, i, n, j;
    fscanf(in, "%d", &t);
  	for (q=1;q<=t; q++) 
	{
		fscanf(in, "%d", &n);
		for (i=0; i<n; i++)
			fscanf(in, "%d", &a[i]);	
		sort(a, a+n);
		int kM=a[n-1];
		for (i=1; i<kM; i++)
		{
			int kNow=i;
			for (j=n-1; j>=0; j--)
			{
				if (a[j]>i) kNow+=(a[j]+i-1)/i-1;
				if (kNow>=kM) j=-1;
			}
			if (kNow<kM) kM=kNow;
		}
    	fprintf(out, "Case #%d: %d\n", q, kM);
  	}
	fclose(in);
    fclose(out);
return(0);
}
