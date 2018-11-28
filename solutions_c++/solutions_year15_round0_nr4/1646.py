#include <iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int X,R,C;
int tt,T;
void Swap(int &a,int &b){
	int t=b;
	b=a;
	a=t;
}
int main(){	
	//freopen("t.txt","r",stdin);
	//freopen("D.out","w",stdout);
	scanf("%d",&T);
	tt=1;
	while(T--){
		scanf("%d%d%d",&X,&R,&C);
		printf("Case #%d: ",tt++);
		if(X==1)
			printf("GABRIEL\n");
		if(R>C)
			Swap(R,C);
		if(X==2){
			if(C==1)
				printf("RICHARD\n");
			else if(C==2)
				printf("GABRIEL\n");
			else if(C==3){
				if(R==2)
					printf("GABRIEL\n");
				else printf("RICHARD\n");
			}
			else if(C==4)
				printf("GABRIEL\n");
		}
		else if(X==3){
			if(C==1||C==2)
				printf("RICHARD\n");
			else if(C==3){
				if(R==1)
					printf("RICHARD\n");
				else
					printf("GABRIEL\n");
			}
			else if(C==4){
				if(R==3)
					printf("GABRIEL\n");
				else
					printf("RICHARD\n");
			}
		}
		else if(X==4){
			if(C<=3)
				printf("RICHARD\n");
			else{
				if(R<=2)
					printf("RICHARD\n");
				else
					printf("GABRIEL\n");
			}
		}
	}
}