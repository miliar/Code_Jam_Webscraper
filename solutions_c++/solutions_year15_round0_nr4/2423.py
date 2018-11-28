#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int j= 1; j <= t; j++){
		int X,R,C;
		cin>>X>>R>>C;
		if(X == 1){
			printf("Case #%d: %s\n", j,"GABRIEL");
		}
		else if(X == 2){
			if((R*C)%2 == 0){
				printf("Case #%d: %s\n", j,"GABRIEL");
			}
			else{
				printf("Case #%d: %s\n", j,"RICHARD");
			}
		}
		else if(X == 3){
			if((C == 3 && R == 2) || (R == 3 && C == 4) || (R == 3 && C == 2) || (C == 3 && R == 3) || (C == 3 && R == 4)) {
				printf("Case #%d: %s\n", j,"GABRIEL");
			}
			else{
				printf("Case #%d: %s\n", j,"RICHARD");
			}
			
		}
		else if(X == 4){
			if((R==3 && C ==4) || (R == 4 && C == 3) || (R == 4 && C == 4)){
				printf("Case #%d: %s\n", j,"GABRIEL");
			}
			else{
				printf("Case #%d: %s\n", j,"RICHARD");
			}
		}
	}
return 0;
}