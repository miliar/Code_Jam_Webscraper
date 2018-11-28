#include "stdafx.h"
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;
int N,J;
int result[10];
int val;
int mask;

int GetDiv(long long a)
{
	long long max=sqrt(a)+1;
	for(long long i=2;i<max;i++)
		if(a%i==0) return i;

	return 0;
}

long long convert(long long a,long long b)
{
	long long x=0;
	long long base=1;
	while(a) 
	{
		if(a&1) x+=base;
		base*=b;
		a>>=1;
	}
	return x;
}

int find_next()
{
	int test_val=0;

	while(1)
	{
		test_val=(val<<1)|mask;

		for(int i=2;i<=10;i++)
		{
			long long tmp=convert(test_val,i);
			if((result[i-2]=GetDiv(tmp))==0) 
			{
				val++;
				goto reset;
			}
		}
		val++;
		break;
reset:;
	}
	return test_val;
};

int main()
{
	FILE* In=fopen("C.in","r");if(!In) return 1;
	FILE* Out=fopen("C.res","w");if(!Out) return 2;

	int nCount;
	fscanf(In,"%d",&nCount);
	for(int i=0;i<nCount;i++)
	{
		fprintf(Out,"Case #%d:\n",i+1);
		
		fscanf(In,"%d%d",&N,&J);

		mask=(1<<(N-1))|1;

		val=0;
		for(int j=0;j<J;j++)
		{
			int res=find_next();
			for(int k=N-1;k>=0;k--)
				fprintf(Out,"%d",(res&(1<<k))?1:0);

			for(int k=2;k<=10;k++)
				fprintf(Out," %d",result[k-2]);

			fprintf(Out,"\n");
		}
	};
	fclose(In);
	fclose(Out);
	return 0;
}