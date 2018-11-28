#include "stdafx.h"
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <functional>   
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

map<multiset<int,greater<int> >, int> cache;

int f(multiset<int, greater<int> >& P)
{	
	if(cache.find(P)!=cache.end()) return cache[P];

	int min_time=*P.begin();
	
	if(*P.begin()>2)
	{
		int p1=*P.begin()>>1;
		repi(i,2,p1+1) 
		{
			int p2=*P.begin()-i;
			multiset<int, greater<int> > tmp;
			tmp.clear();
			tmp.insert(P.begin(),P.end());
			tmp.erase(tmp.begin());
			tmp.insert(i);
			tmp.insert(p2);
			min_time=min(min_time,f(tmp)+1);
		}
	}

	cache[P]=min_time;
	return min_time;
}

int main()
{
	FILE* In=fopen("B.in","r");if(!In) return 1;
	FILE* Out=fopen("B.res","w");if(!Out) return 2;

	int D;
	multiset<int, greater<int> > P;

	int nCount;
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"%d",&D);
		int p;
		P.clear();
		rep(j,D) {fscanf(In,"%d",&p);P.insert(p);}

		int res=f(P);

		fprintf(Out,"%d\n",res);
	};
	fclose(In);
	fclose(Out);
	return 0;
}
