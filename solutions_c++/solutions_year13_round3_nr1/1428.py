/*Vladimir Ignatiev 2013*/
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

char S[1001];
int n;

int64 f()
{	
	int nRes=0;
	int L=strlen(S);
	
	rep(i,L-n+1)
	{
		int nC=0;
		repi(j,i,L)
		{
			if((S[j]!='a')&&(S[j]!='e')&&(S[j]!='i')&&(S[j]!='o')&&(S[j]!='u')) 
			{
				nC++;
				if(nC>=n) 
				{
					nRes+=L-j;
					break;
				};
			}
			else
				nC=0;
		}
	}
	return nRes;
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
		fscanf(In,"%s%d",&S,&n);
		int64 res=f();
		fprintf(Out,"%I64d\n",res);
	};
	fclose(In);
	fclose(Out);
	return 0;
}