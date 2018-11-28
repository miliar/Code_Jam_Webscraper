//============================================================================
// Name        : 130414-fairandsquare.cpp
// Author      : myscloud
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>

long long tab[100005];

bool chkPalindrome(long long x){
	int i=0,j,count=0,num[20];
	while(x>0){
		num[i] = x%10;
		x /= 10;
		i++;
	}

	for(j=0;j<i/2;j++)
		if(num[j]==num[i-j-1]) count++;

	if(count==i/2) return true;
	else return false;
}

int main(){

	int i,j,count=0,test,start,end;
	long long sum,front,back;

	//find number of ...
	for(i=1;i<=10000000;i++){
		if(chkPalindrome(i)){
			sum = (long long)i*i;
			if(chkPalindrome(sum)){
				tab[count] = sum;
				count++;
			}
		}
	}

	scanf("%d",&test);

	for(j=1;j<=test;j++){

		scanf("%lld %lld",&front,&back);
		start = -1;
		for(i=0;i<count;i++)
			if(tab[i]>=front){
				start = i;
				break;
			}

		end = -1;
		for(i=count-1;i>=0;i--)
			if(tab[i]<=back){
				end = i;
				break;
			}

		if(start==-1 || end==-1) printf("Case #%d: 0\n",j);
		else printf("Case #%d: %d\n",j,end-start+1);

	}


}
