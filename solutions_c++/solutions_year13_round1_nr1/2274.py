//============================================================================
// Name        : ProblemA.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include<stdlib.h>
#include<math.h>

int main(){
	int T,t,r;
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		scanf("%d %d",&r,&t);
		double temp=pow(2*r+3,2)-4*2*(2*r-t+1);
		temp=sqrt(temp);
		temp-=2*r+3;
		temp/=4;
		int fin=floor(temp);
		printf("Case #%d: %d\n",i+1,fin+1);
	}
	return 0;
}
