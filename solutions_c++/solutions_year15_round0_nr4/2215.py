#include<stdio.h>
#include<stdlib.h>

int main(){
	freopen("0Q/D-small-attempt0.in","r",stdin);
	freopen("0Q/out.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int X,R,C;
		scanf("%d%d%d",&X,&R,&C);

		bool isGabriel=true;
		switch(X){
			case 2:
				if(R*C % 2)isGabriel=false;
				break;
			case 3:
				if(R*C % 3 || R*C == 3)isGabriel=false;
				break;
			case 4:
				if(R*C % 4 || R*C == 4 || R*C == 8)isGabriel=false;
				break;
		}

		printf("Case #%d: %s\n",t,isGabriel ? "GABRIEL":"RICHARD");

	}
}
