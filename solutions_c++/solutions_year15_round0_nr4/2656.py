#include<iostream>
#include<cstdio>

int main(){
	int test_cases;
	int X,R,C;
	scanf("%d",&test_cases);
	for(int i=0;i<test_cases;i++){
		scanf("%d %d %d",&X,&R,&C);
		if(R < X && C < X){
			printf("Case #%d: RICHARD\n",i+1);
			continue;
		}
		if( X % 2 == 0){
			if(R < X/2 || C < X/2){
				printf("Case #%d: RICHARD\n",i+1);
				continue;		
			}
		}
		else{
			if(R < (X/2 + 1) || C < (X/2 + 1)){
				printf("Case #%d: RICHARD\n",i+1);
				continue;		
			}
		}
		if( (R*C) % X != 0){
			printf("Case #%d: RICHARD\n",i+1);
			continue;
		}
		else if((X==4 && ((R==2 && C==4) || (R==4 && C==2))) || (X==3 && ((R==1 && C==3) || (R==3 && C==1)))){
			printf("Case #%d: RICHARD\n",i+1);
			continue;
		} 
		else{
			printf("Case #%d: GABRIEL\n",i+1);
		}
	}

	return 0;	
}
