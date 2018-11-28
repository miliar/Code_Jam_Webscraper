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

int N, M, a[100][100];


bool f()
{	
	int maxX[100];
	int maxY[100];

	rep(x,N)
	{
		maxX[x]=0;
		rep(y,M)
			maxX[x]=std::max(maxX[x],a[x][y]);
	}
						
	rep(y,M)
	{
		maxY[y]=0;
		rep(x,N)
			maxY[y]=std::max(maxY[y],a[x][y]);
	}
	
	rep(x,N)
	rep(y,M)
	if((a[x][y]<maxX[x])&&(a[x][y]<maxY[y])) return false;
	
	return true;
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
		fscanf(In,"%d%d",&N,&M);
		rep(x,N)
			rep(y,M)
				fscanf(In,"%d",&a[x][y]);

		fprintf(Out,"%s\n",f()?"YES":"NO");
	};
	fclose(In);
	fclose(Out);
	return 0;
}