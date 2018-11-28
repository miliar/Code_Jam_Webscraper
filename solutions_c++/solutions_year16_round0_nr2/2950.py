#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string.h>

using namespace std;

#define vi vector<int>
#define vii vector<vi >
#define vb vector<bool>
#define vc vector<char>
#define z x[k][side]

int N,n,m;

char cake[100];

vii x(100);

int compute(int k,int side){
	// this is the main case
	if(z!=-1)
		return z;
	char next=cake[k];
	if(k==0){
		if(next=='-' && side==0)
			return z = 0;
		if(next=='-' && side==1)
			return z = 1;
		if(next=='+' && side==0)
			return z = 1;
		if(next=='+' && side==1)
			return z = 0;
	}
	int a=compute(k-1,0);
	int b=compute(k-1,1);
	if(next=='-' && side==0){
		return z = min(a,b+2);
	}
	if(next=='-' && side==1){
		return z = min(a+1,b+3);
	}
	if(next=='+' && side==0){
		return z = min(a+3,b+1);
	}
	if(next=='+' && side==1){
		return z = min(a+1,b);
	}
}

int main(int argc, char const *argv[])
{
	cin>>N;
	for (int ii = 1; ii <= N; ++ii)
	{
		for (int i = 0; i < 100; ++i)
		{
			vi tmp(2);
			x[i]=tmp;
		}
		for (int i = 0; i < 100; ++i){
			x[i][0]=-1;
			x[i][1]=-1;
		}
		scanf("%s",cake);
		n=strlen(cake);
		// printf("%s %d\n",cake,n );
		int ans = compute(n-1,1);
		printf("Case #%d: %d\n",ii,ans );
	}
	return 0;
}
