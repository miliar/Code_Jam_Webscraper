/*Vladimir Ignatiev 2014*/
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

#define MAX_ARR 200

char C[MAX_ARR][MAX_ARR];
int N;

void MakeShort(const char* pSrc,char* pDest,int* Dt)
{
	*pDest=*pSrc;
	pSrc++;
	int i=0;
	Dt[i]=1;
	while(*pSrc!='\0')
	{
		if(*pDest!=*pSrc) {++pDest; *pDest=*pSrc; i++; Dt[i]=1;} else Dt[i]++;
		++pSrc;
	}

	++pDest;
	*pDest='\0';
}

int f()
{	
	int Res=0;
	char D[MAX_ARR][MAX_ARR];
	int Dt[MAX_ARR][MAX_ARR];

	MakeShort(C[0],D[0],Dt[0]);

	repi(i,1,N)
	{
		MakeShort(C[i],D[i],Dt[i]);
		if(strcmp(D[0],D[i])!=0) return -1;
	}

	int L=strlen(D[0]);

	rep(l,L)
	{
		int	av=0;
		rep(i,N)
		{
			av+=Dt[i][l];
		}

		av/=N;

		rep(i,N)
		{
			Res+=abs(av-Dt[i][l]);
		}
	}

	return Res;
}

int main()
{
	FILE* In=fopen("A.in","r");if(!In) return 1;
	FILE* Out=fopen("A.res","w");if(!Out) return 2;

	int nCount;
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"%d",&N);
		rep(i,N)
			fscanf(In,"%s",C[i]);
	
		int res=f();
		if(res<0)
			fprintf(Out,"%s\n","Fegla Won");
		else
			fprintf(Out,"%d\n",res);
	};
	fclose(In);
	fclose(Out);
	return 0;
}