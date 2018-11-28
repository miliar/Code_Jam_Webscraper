#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int main(){
	int times=0,k=1;
	scanf("%d",&times);
	while(times--){
		printf("Case #%d: ",k);
		int X=0,R=0,C=0;
		scanf("%d %d %d",&X,&R,&C);
        if(C>R){
			swap(C,R);
		}
		if(X==1){
			printf("GABRIEL\n");
		}
		else if(X==2){
			if(C%2==0||R%2==0){
				printf("GABRIEL\n");
			}
			else{
				printf("RICHARD\n");
			}
		}
		else if(X==3){
			if((C==3&&R%2==0)||(R==3&&C%2==0)||(C==3&&R==3)){
				printf("GABRIEL\n");
			}
			else{
				printf("RICHARD\n");
			}
		}
		else{
			if(C==1||C==2){
				printf("RICHARD\n");
			}
			else if(C==3){
				if(R==3){
					printf("RICHARD\n");
				}
				else{
					printf("GABRIEL\n");
				}
			}
			else{
				printf("GABRIEL\n");
			}
		}
		k++;
	}
	return 0;
}
