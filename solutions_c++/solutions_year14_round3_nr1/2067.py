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

typedef long long int64;
#define abs64(A) _abs64((int64)A)
#define INT64_MAX   0x7fffffffffffffffLL
#define INT64_MIN   (-INT64_MAX - 1LL)

int64 P, Q;

int64 GCD(int64 a,int64 b)
{
  while(a&&b)
    if (a >= b)
      a = a % b;
    else
      b = b % a;
 
  return (a + b);
}

map<pair<int64,int64>,int> M;

void savedb(int64 p1,int64 p2,int level)
{
	M[make_pair(p1,p2)]=level;
};

int checkdb(int64 p1,int64 p2)
{
	auto pos=M.find(make_pair(p1,p2));
	if(pos==M.end()) return -1;
	return pos->second;
}

int check(int64 p1,int64 p2, int level)
{
	if(level>40) return INT_MAX;

	p1<<=1;
	if(p1>p2)
	{
		if(check(p1-p2,p2,level+1)!=INT_MAX) return level;
		return INT_MAX;
	}

	int64 gcd=GCD(p1,p2);
	p1/=gcd;
	p2/=gcd;
	int res=checkdb(p1,p2);
	if(res!=-1)
	{
		if(res!=INT_MAX) res++; 
		return res;
	}

	int64 p1_val=min((p1>>1)+(p1&1),p2);
	int minRes=INT_MAX;
	for(int64 i=1;i<=p1_val;i++)
	{
		int res1=check(i,p2,level+1);
		int res2=(p1==i)?res1:check(p1-i,p2,level+1);
		
		if((res1!=INT_MAX)&&(res2!=INT_MAX)) minRes=min(minRes,min(res1,res2)); 
	}

	savedb(p1,p2,minRes);
	if(minRes!=INT_MAX) minRes++;

	return minRes;
}

int main()
{
	FILE* In=fopen("A.in","r");if(!In) return 1;
	FILE* Out=fopen("A.res","w");if(!Out) return 2;

	M.clear();
	savedb(1,1,0);
	savedb(0,1,INT_MAX);

	int nCount;
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"%I64d%*c%I64d",&P,&Q);

		int res=check(P,Q,1);
		if(res==INT_MAX)
			fprintf(Out,"%s\n","impossible");
		else
			fprintf(Out,"%d\n",res);
	};
	fclose(In);
	fclose(Out);
	return 0;
}