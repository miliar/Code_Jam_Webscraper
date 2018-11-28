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

unsigned char digits[10];
int total;

bool parse(long long val)
{
	char str_val[64];
	sprintf(str_val,"%I64d",val);
	for(int i=strlen(str_val)-1;i>=0;i--)
	{
		int digit=str_val[i]-'0';
		if(!digits[digit])
		{
			total++;
			digits[digit]=1;
		}
		if(total==10) return true;
	}
	return false;
};

int main()
{
    FILE* In=fopen("A.in","r");if(!In) return 1;
	FILE* Out=fopen("A.res","w");if(!Out) return 2;

	int nCount;
	long long N,varN;

	fscanf(In,"%d",&nCount);
	for(int i=0;i<nCount;i++)
	{
		fprintf(Out,"Case #%d: ",i+1);
		fscanf(In,"%I64d",&N);

		if(N==0) {fprintf(Out,"INSOMNIA\n");continue;}

		memset(digits,0,10);
		total=0;
		varN=N;
		while(!parse(varN)) varN+=N;
		fprintf(Out,"%I64d\n",varN);
	};
	fclose(In);
	fclose(Out);
	return 0;
}