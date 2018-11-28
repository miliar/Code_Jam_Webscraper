#include<stdio.h>
#include<memory.h>
#include<string.h>
int n;
int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	unsigned long long int r,t,k;

	int i, j, tc;
	int cnt;
	fscanf(fp, "%d", &n);
	for(i=0;i<n;i++) 
		{
		fscanf(fp, "%llu",&r);
		fscanf(fp, "%llu",&t);
		for(k=1;2*r*k+2*k*k-k<=t;k++);
		
		fprintf(ofp, "Case #%d: %llu\n",i+1,k-1);
		}
		
	return 0;
}
