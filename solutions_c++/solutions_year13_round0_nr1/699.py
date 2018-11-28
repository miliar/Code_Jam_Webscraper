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

char A[4][5];

#define TEST	if(A[i][j]=='.') {cur='.';break;}\
				if((cur!='T')&&(A[i][j]!='T'))\
				if(A[i][j]!=cur) {cur='.';break;}\
				if(A[i][j]!='T') cur=A[i][j];

int f()
{	
	char cur;
	rep(i,4)
	{
		cur='T';
		rep(j,4)
		{
			TEST;
		}
		if(cur=='X') return 0;
		if(cur=='O') return 1;
	}
	
	rep(j,4)
	{
		cur='T';
		rep(i,4)
		{
			TEST;
		}
		if(cur=='X') return 0;
		if(cur=='O') return 1;
	}

	cur='T';
	rep(i,4)
	{
		int j=i;
		TEST;
	}
	if(cur=='X') return 0;
	if(cur=='O') return 1;

	cur='T';
	rep(i,4)
	{
		int j=3-i;
		TEST;
	}
	if(cur=='X') return 0;
	if(cur=='O') return 1;
	
	rep(i,4)
		rep(j,4)
			if(A[i][j]=='.') return 3;

	return 2;
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
		rep(j,4)
			fscanf(In,"%s",A[j]);

		switch (f())
		{
			case 0:fprintf(Out,"%s\n","X won");break;
			case 1:fprintf(Out,"%s\n","O won");break;
			case 2:fprintf(Out,"%s\n","Draw");break;
			default:fprintf(Out,"%s\n","Game has not completed");break;
		};
	};
	fclose(In);
	fclose(Out);
	return 0;
}