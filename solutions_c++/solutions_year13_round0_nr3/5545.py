//============================================================================
// Name        : CodeJam2013.cpp
// Author      : Gaurav
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include<iostream>
#include<stdio.h>
#include<algorithm>

#include<vector>
#include<stack>
#include<math.h>
#include<string.h>
using namespace std;

bool isPalin(long long A){
	char str[20];
	sprintf(str,"%lld",A);
	int len=strlen(str),i;
	len--;
	for(i=0;i<len;i++,len--)if(str[i]!=str[len])return false;
	return true;
}
long long eval(long long A,long long B){
	long double Aroot,Broot;
	Aroot = sqrt(A);
	Broot = sqrt(B);
	Aroot = ceil(Aroot);Broot=floor(Broot);
	long long Aa,Bb;
	Aa=(long long)Aroot;Bb=(long long)Broot;
	long long  i,sum=0;

	for(i=Aa;i<=Bb;i++){
		if(isPalin(i) && isPalin(i*i))
			sum++;
	}
	return sum;
}

int main() {

	int i,j,k,T;
	long long A,B;
	scanf("%d",&T);

	for(i=0;i<T;i++){
		scanf("%lld %lld",&A,&B);

		printf("Case #%d: %lld\n",i+1,eval(A,B));

	}
}
