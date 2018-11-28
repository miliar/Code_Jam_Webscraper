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

#define M 1001
int f(int s_max,int* S)
{	
	int nTotal=0;
	int ret=0;
	
	rep(i,s_max) 
	{
		if(nTotal<i) {ret+=i-nTotal; nTotal=i;}
		nTotal+=S[i];
	}
		
	return ret;
}

int main()
{
	FILE* In=fopen("A.in","r");if(!In) return 1;
	FILE* Out=fopen("A.res","w");if(!Out) return 2;

	int s_max, S[M];

	int nCount;
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"%d%*[ ]",&s_max);
		s_max++;
		char ch;
		rep(j,s_max) {fscanf(In,"%c",&ch);S[j]=ch-'0';}

		fprintf(Out,"%d\n",f(s_max,S));
	};
	fclose(In);
	fclose(Out);
	return 0;
}