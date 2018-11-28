//============================================================================
// Name        : CodeJam.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Problem D. Ominous Omino
//============================================================================

#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;



int main() {
	int T,X,R,C;
	float div;
	int divn;
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		scanf("%d %d %d",&X,&R,&C);
		printf("Case #%d: ",i+1);
		div=(float)(R*C)/X;
		divn=div;
		if(X>max(R,C))
			printf("RICHARD\n");
		else if(div - divn > 0)
			printf("RICHARD\n");
		else{
			int x,xi,xd;
			if(X%2==0){
				x=X/2;
			}else{
				x=(X+1)/2;
			}
			xd=X-x;
			xi=x-1;

			if(xi >= min(R,C))
				printf("RICHARD\n");
			else if(xi + 1 == min(R,C)){
				if(xd > 1)
					printf("RICHARD\n");
				else
					printf("GABRIEL\n");
			}else
				printf("GABRIEL\n");
		}
	}

	return 0;
}
