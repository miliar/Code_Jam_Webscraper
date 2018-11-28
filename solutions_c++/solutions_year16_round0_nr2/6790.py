//============================================================================
// Name        : CodeJam2.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>

char panStack[101];

//void printStack(int n){
//	for(int i=0;i<n;i++){
////		if(panStack[i]==1){
//			printf("%c",panStack[i]);
////		}else{
////			printf("-");
////		}
//	}
//	printf("\n");
//}

int main() {

//	freopen("sin","r",stdin);
//	freopen("sout","w",stdout);

	int t;
		int tc;
		int n,i,j,k;
		int curNum;
		scanf("%d",&t);
		int found;
		char c;
		char curChar;
		scanf("%c",&c);
		int change=0;
		for(tc=1;tc<=t;tc++){
//			memset(panStack,0,pan)

			for(i=0;;i++){

				if(scanf("%c",&c)==EOF)
					break;
				if(c=='\n'){
					break;
//				}else if(c=='+'){
//					panStack[i]=1;
				}else{
					panStack[i]=c;
				}
			}
			n=i;
			curChar=panStack[0];
			change=0;
			for(i=1;i<n;i++){
				if(panStack[i]!=curChar){
					change++;
					curChar=panStack[i];
				}
			}
			if(panStack[n-1]=='-'){
				change++;
			}
//			printStack(n);

			printf("Case #%d: %d\n",tc,change);


		}
	return 0;
}
