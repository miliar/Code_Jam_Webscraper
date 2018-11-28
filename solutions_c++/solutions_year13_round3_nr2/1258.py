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

string way;
int X,Y;
int nMax;

struct St
{
	int x;
	int y;
	int step;
};

bool operator <(const St& st1, const St& st2)
{
	if(st1.x==st2.x)
	{
		if(st1.y==st2.y) return st1.step<st2.step;
		else return st1.y<st2.y;
	}
	return st1.x<st2.x;
}

set<St> st_set;

bool test(int x,int y, int step)
{
	St st;st.x=x;st.y=y;st.step=step;
	if(st_set.find(st)!=st_set.end()) return false;

	if((x==X)&&(y==Y))	return true;
	if(step>=nMax)		return false;

	if(test(x-step,y,step+1)) {way='W'+way;return true;}
	if(test(x+step,y,step+1)) {way='E'+way; return true;}
	if(test(x,y+step,step+1)) {way='N'+way;return true;}
	if(test(x,y-step,step+1)) {way='S'+way;return true;}

	st_set.insert(st);

	return false;
}


void f()
{	
	repi(i,20,500)
	{
		nMax=i;
		st_set.clear();
		if(test(0,0,1)) return;
	}
}

int main()
{
	FILE* In=fopen("B.in","r");if(!In) return 1;
	FILE* Out=fopen("B.res","w");if(!Out) return 2;

	int nCount;
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"%d%d",&X,&Y);

		way="";
		
		f();
		fprintf(Out,"%s\n",way.c_str());
	};
	fclose(In);
	fclose(Out);
	return 0;
}