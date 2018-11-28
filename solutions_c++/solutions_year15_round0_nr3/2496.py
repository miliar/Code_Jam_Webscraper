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

int L, X, T;
vector<int> A;

/*
'1' = 1
'i' = 2
'j' = 3
'k' = 4
*/
int rule[4][4]={{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};

int get(int x, int y)
{
	int sign=(((x<0)&&(y<0))||((x>0)&&(y>0)))?1:-1;
	return rule[abs(x)-1][abs(y)-1]*sign;
}

int find_val(int idx, int& cur_val, int val)
{
	while(idx<T)
	{
		if((cur_val=get(cur_val,A[idx%L]))==val) {idx++; return idx;}
		idx++;
	}
	return -1;
}

int find_end_val(int idx)
{
	int cur_val=1;

	while(idx<T)
	{
		cur_val=get(cur_val,A[idx%L]);
		idx++;
	}
	return cur_val;
}

bool f()
{	
	int cur_val_i=1;
	int idx_i=0;
	vector<int> ch;

	rep(i,T) ch.push_back(find_end_val(i));

	while(idx_i<T)
	{
		if((idx_i=find_val(idx_i,cur_val_i,2))<0) return false;

		int cur_val_j=1;
		int idx_j=idx_i;

		while(idx_j<T)
		{
			if((idx_j=find_val(idx_j,cur_val_j,3))<0) break;
			if(idx_j>=T) break;

			if(ch[idx_j]==4) return true;
		}
	}

	return false;
}

int main()
{
	FILE* In=fopen("C.in","r");if(!In) return 1;
	FILE* Out=fopen("C.res","w");if(!Out) return 2;

	int nCount;

	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"%d%d%*[ \n]",&L,&X);
		char chr;
		A.clear();
		T=X*L;
		rep(j,L)
		{
			fscanf(In,"%c",&chr);
			if(chr=='i') A.push_back(2);
			else
			if(chr=='j') A.push_back(3);
			else
			if(chr=='k') A.push_back(4);
			else
			{
				printf("Error");
				abort();
			}
		}
		
		fprintf(Out,"%s\n",f()?"YES":"NO");
	};
	fclose(In);
	fclose(Out);
	return 0;
}