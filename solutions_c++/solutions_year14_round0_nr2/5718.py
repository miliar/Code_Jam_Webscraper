//============================================================================
// Name        : gcj0b.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include<stdio.h>
#include<stdlib.h>
#define eps 1e-8
using namespace std;

int main() {
	int cas,cnt,n;
	double sum,X,F,C,temp;
	 freopen("B-small-attempt3.in","r",stdin);
	 freopen("B-small-attempt3.out","w",stdout);
	scanf("%d",&cas);
	cnt=0;
	while(cas--){


		scanf("%lf%lf%lf",&C,&F,&X);
		if(C/2+X/(2+F)-X/2>=eps)
			sum=X/2;
		else{
			sum=C/2+X/(2+F);
			for(n=2;;n++){
				temp=sum-X/(2+(n-1)*F)+X/(2+n*F)+C/(2+(n-1)*F);
				if(sum-temp>eps)
					sum=temp;
				else
					break;
			}

		}
		printf("Case #%d: %.7lf\n",++cnt,sum);

		}


	}

