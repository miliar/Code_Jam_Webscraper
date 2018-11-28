// template.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>

FILE *fin = fopen("input.txt","r");
FILE *fout = fopen("output.txt","w");

void proc()
{
	int n;
	fscanf(fin,"%d",&n);
	int mush[2000];
	long long int m1=0;
	long long int max_diff=0;
	for(int i=0;i<n; i++)
	{
		fscanf(fin,"%d ",&mush[i]);
		if(i!=0)
		{
			if(mush[i-1]-mush[i]>0)
			{
				m1+=mush[i-1]-mush[i];
				if(mush[i-1]-mush[i]>max_diff)
					max_diff=mush[i-1]-mush[i];
			}
		}
	}
	long long int m2=0;
	for(int i=0;i<n-1;i++)
	{
		if(max_diff>=mush[i])
			m2+=mush[i];
		else
			m2+=max_diff;
	}
	fprintf(fout,"%lld %lld",m1,m2);
	fprintf(fout,"\n");
}
int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	
	fscanf(fin,"%d",&t);
	for(int i=0;i<t;i++)
	{
		fprintf(fout,"Case #%d: ",i+1);
		proc();
	}
	return 0;
}

