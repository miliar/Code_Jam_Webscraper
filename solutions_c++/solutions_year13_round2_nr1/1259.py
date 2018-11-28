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

int A, N;
int n[100];

struct T
{
	int64 nCur;
	int nPos;
};

bool operator <(const T& t1,const T t2) {return t1.nCur==t2.nCur?t1.nPos<t2.nPos:t1.nCur<t2.nCur;}


map<T, int> S;

int f(int64 nCur,int pos)
{
	T t; t.nCur=nCur; t.nPos=pos;

	if(S.find(t)!=S.end())
		return S[t];

	if(pos==N) return 0;
	if(nCur>n[pos])  return f(nCur+n[pos],pos+1);
	int nMin=f(nCur,pos+1);
	int64 nCurNew=(nCur<<1)-1;
	if(nCurNew==nCur) {S[t]=nMin+1; return nMin+1;}
	nMin=min(nMin,f(nCurNew,pos));
	S[t]=nMin+1;
	return nMin+1;
};

int main()
{
	FILE* In=fopen("A.in","r");if(!In) return 1;
	FILE* Out=fopen("A.res","w");if(!Out) return 2;

	int nCount;
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		S.clear();
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"%d%d",&A,&N);
		rep(j,N)
			fscanf(In,"%d",&n[j]);

		std::sort(n,n+N);

		int res=f(A,0);
		fprintf(Out,"%d\n",res);
	};
	fclose(In);
	fclose(Out);
	return 0;
}