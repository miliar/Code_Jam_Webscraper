#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>

#include<memory.h>

using namespace std;
#define MAX 100000000000000


int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");


	long long result[100];
	int npos = 0;
	for(long long i = 1; i*i<=MAX; i++)
	{
		long long x, y;
		char ch[17];
		int pos = 0;
		
		x = i;
		do 
		{
			ch[++pos] = x%10;
			x/=10;
		}while(x !=0);
		bool trac = true;
		for(int k = 1, j = pos; k<j; k++,j--)
		{
			if(ch[k]!=ch[j])
			{
				trac = false;
				break;
			}
		}
		if(!trac)continue;


		y = x = i*i;
		pos = 0;
		do 
		{
			ch[++pos] = x%10;
			x/=10;
		}while(x !=0);
		
		trac = true;
		for(int k = 1, j = pos; k<j; k++,j--)
		{
			if(ch[k]!=ch[j])
			{
				trac = false;
				break;
			}
		}
		if(trac) 
		{
			result[++npos] = y;
		}
	}

	int T;
	fscanf(fp, "%d",&T);

	for(int t = 1; t<=T; t++)
	{
		long long a, b;
		fscanf(fp, "%lld %lld",&a,&b);

		int res = 0;
		for(int i = 1; result[i]<=b; i++)
		{
			 if(result[i] >= a && result[i] <= b)res++;
		}
		fprintf(ofp, "Case #%d: %d\n",t,res);
	}
	return 0;
}