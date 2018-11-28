/*Written by Vladimir Ignatiev*/
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

#define rep(A,B) for(int A=0;A<B;++A)
#define repi(A,I,B) for(int A=I;A<B;++A)
#define repd(A,B) for(int A=B-1;A>=0;--A)
#define repdi(A,I,B) for(int A=B-1;A>=I;--A)
#define repall(A,F) for_each(A.begin(),A.end(),F);

typedef long long int64;
#define abs64(A) _abs64((int64)A)
#define INT64_MAX   0x7fffffffffffffffLL
#define INT64_MIN   (-INT64_MAX - 1LL)

vector<int64> fs; 

bool ispoly(int64 N)
{
	int64 T1=N;
	int64 T2=0;
	while(T1)
	{
		T2*=10;
		T2+=T1%10;
		T1/=10;
	}
	return (N==T2);
};

void init(int64 A,int64 B)
{	
	int res=0;
	int64 bg=sqrt(A);
	if((bg*bg)<A) bg++;
	int64 ed=sqrt(B);

	while(bg<=ed)
	{
		if(ispoly(bg)&&(ispoly(bg*bg))) fs.push_back(bg*bg);
		bg++;
	}
}

int f(int64 A,int64 B)
{
	int res=0;
	
	rep(i,fs.size())
	{
		if((fs[i]>=A)&&(fs[i]<=B)) res++;
	}

	return res;
}

int main()
{
	FILE* In=fopen("C.in","r");if(!In) return 1;
	FILE* Out=fopen("C.res","w");if(!Out) return 2;

	int64 A, B;
	init(1,100000000000000);
	int nCount;
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"%I64d%I64d",&A,&B);

		int res=f(A,B);
		fprintf(Out,"%d\n",res);
	};
	fclose(In);
	fclose(Out);
	return 0;
}