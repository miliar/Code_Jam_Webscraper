// prob3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

__int64 squares[1000];
int numCases,n;

bool isPalindrome(__int64 temp) {
	int table[1000], cnt = 0 ; 
	while ( temp>0) {
		table[cnt] = temp%10 ; 
		temp/=10;
		cnt++;
	}
	for(int i=0;i<cnt/2;i++) {
		if (table[i] != table[cnt-i-1] ) {
			return false ; 
		}
	}
	return true; 
}

void base() {
	n=0;
	for(int i=0;i<=10000000;i++) {
		if (isPalindrome(i)) {
			__int64 temp = (__int64)i*(__int64)i ; 
			if (isPalindrome(temp)) {
//				printf("%d %I64d \n",i,temp);
				squares[n++] = temp ; 
			}
		}
	}
}


int _tmain(int argc, _TCHAR* argv[])
{
	base(); 

	FILE *in = fopen("C-large-1.in","r");
	FILE *out = fopen("output.txt","w");

	fscanf(in,"%d",&numCases);

	for(int cnt=0;cnt<numCases;cnt++) {
		__int64 a,b;
		int result=0;
		fscanf(in,"%I64d %I64d",&a,&b);

		for(int i=0;i<n;i++) {
			if ( squares[i]>=a && squares[i]<=b) {
				result++;
			}
		}

		fprintf(out,"Case #%d: %d\n",cnt+1,result);
	}

	fclose(in);
	fclose(out);

	
	return 0;
}

