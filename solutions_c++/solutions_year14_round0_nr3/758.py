/*Vladimir Ignatiev 2014*/
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

int R, C, M;
char A[50][50];

int f()
{	
	int T=R*C-M;
	int nMin=std::min(R,C);
	memset(A,'*',sizeof(A));
	if(T==1) {A[0][0]='.';return 0;}
	
	
	if((T/C>=2)&&(T%C!=1))
	{
		rep(r,R)
		rep(c,C)
		{
			A[r][c]='.';
			--T;
			if(!T) return 0;
		}
	}

	int Cx=C-1;
	if((Cx>2)&&(Cx*R>=T)&&(T/Cx>=2)&&(T%Cx!=1))
	{
		rep(r,R)
		rep(c,Cx)
		{
			A[r][c]='.';
			--T;
			if(!T) return 0;
		}
	}
	

	if((T/R>=2)&&(T%R!=1))
	{
		rep(c,C)
		rep(r,R)
		{
			A[r][c]='.';
			--T;
			if(!T) return 0;
		}
	}
	
	int Rx=R-1;
	if((Rx>2)&&(Rx*C>=T)&&(T/Rx>=2)&&(T%Rx!=1))
	{
		rep(c,C)
		rep(r,Rx)
		{
			A[r][c]='.';
			--T;
			if(!T) return 0;
		}
	}

	repi(i,2,T)
	{
		int j=T/i;
		if(j<i) break;
		if(i*j==T)
		{
			if((i<=R)&&(j<=C))
			{
				rep(x,i)
				rep(y,j)
					A[x][y]='.';

				return 0;
			}
			if((i<=C)&&(j<=R))
			{
				rep(x,j)
				rep(y,i)
					A[x][y]='.';

				return 0;
			}
		}
	}

	if((C>=3)&&(T/C>=3)&&(T%C==1))
	{
		rep(r,R)
		rep(c,C)
		{
			A[r][c]='.';
			--T;
			if(!T)
			{
				A[r][c+1]='.';
				A[r-1][C-1]='*';
				return 0;
			}
		}
	}

	if((R>=3)&&(T/R>=3)&&(T%R==1))
	{
		rep(c,C)
		rep(r,R)
		{
			A[r][c]='.';
			--T;
			if(!T)
			{
				A[r+1][c]='.';
				A[R-1][c-1]='*';
				return 0;
			}
		}
	}

	return 1;
}

int main()
{
	FILE* In=fopen("C.in","r");if(!In) return 1;
	FILE* Out=fopen("C.res","w");if(!Out) return 2;

	int nCount;
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d:\n",i+1);
		printf("%d\n",i);
		fscanf(In,"%d%d%d",&R,&C,&M);

		if(f())	
			fprintf(Out,"%s\n","Impossible");
		else
		{
			A[0][0]='c';
			rep(r,R)
			{
				rep(c,C)
					fprintf(Out,"%c",A[r][c]);

				fprintf(Out,"\n");
			}
		}
	};
	fclose(In);
	fclose(Out);
	return 0;
}