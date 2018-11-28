//============================================================================
// Name        : CodeJam1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include<stdlib.h>
#include<string.h>
//using namespace std;

int digits[10]={0,0,0,0,0,0,0,0,0,0};

void findDigits(int number){
	while(number)
	{
		digits[number%10]=1;
	    number /= 10;
	}
}

int checkDigits(){
	int i,j,k;
	int b=1;
	for(i=0;i<10;i++){
		if(digits[i]==0){
			b=0;
			break;
		}
	}
	return b;
}

int main() {

	freopen("sin","r",stdin);
	freopen("sout","w",stdout);

	int t;
	int tc;
	int n,i,j,k;
	int curNum;
	scanf("%d",&t);
	int found;
	for(tc=1;tc<=t;tc++){
		memset(digits,0,sizeof(int)*10);
		scanf("%d",&n);
		if(n==0){
			printf("Case #%d: INSOMNIA\n",tc);
			continue;
		}
		found=0;
		curNum=n;
		findDigits(curNum);
		found=checkDigits();
		while(found==0){
			curNum=curNum+n;
			findDigits(curNum);
			found=checkDigits();
		}
		printf("Case #%d: %d\n",tc,curNum);
	}

	return 0;
}
