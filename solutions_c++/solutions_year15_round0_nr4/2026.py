#include <stdio.h>

int main(){
	/*int matrix[4][4][4];
	//X = 1
	matrix[1][1][1]= 1;		
	matrix[1][2][1]= 1;		
	matrix[1][3][1]= 1;		
	matrix[1][4][1]= 1;		
	matrix[2][2][1]= 1;		
	matrix[2][3][1]= 1;		
	matrix[2][4][1]= 1;		
	matrix[3][3][1]= 1;		
	matrix[3][4][1]= 1;		
	matrix[4][4][1]= 1;

	//X = 2
	matrix[1][1][2]= 0;		
	matrix[1][2][2]= 0;		
	matrix[1][3][2]= 0;		
	matrix[1][4][2]= 1;		
	matrix[2][2][2]= 1;		
	matrix[2][3][2]= 1;		
	matrix[2][4][2]= 1;		
	matrix[3][3][2]= 0;		
	matrix[3][4][2]= 1;		
	matrix[4][4][2]= 1;

	//X = 3
	matrix[1][1][3]= 0;		
	matrix[1][2][3]= 0;		
	matrix[1][3][3]= 0;		
	matrix[1][4][3]= 0;		
	matrix[2][2][3]= 0;		
	matrix[2][3][3]= 1;		
	matrix[2][4][3]= 0;		
	matrix[3][3][3]= 1;		
	matrix[3][4][3]= 1;		
	matrix[4][4][3]= 0;

	//X = 4
	matrix[1][1][4]= 0;		
	matrix[1][2][4]= 0;		
	matrix[1][3][4]= 0;		
	matrix[1][4][4]= 0;		
	matrix[2][2][4]= 0;		
	matrix[2][3][4]= 0;		
	matrix[2][4][4]= 0;		
	matrix[3][3][4]= 0;		
	matrix[3][4][4]= 1;		
	matrix[4][4][4]= 1;
	*/
	int T;
	scanf("%d",&T);
	int g=1;

	while(T--){
		int X,R,C;
		scanf("%d",&X);
		scanf("%d",&R);
		scanf("%d",&C);

		if(R>C){
			int temp = C;
			C = R;
			R = temp;
		}
		
		if(X == 1)
			printf("Case #%d: %s\n", g,"GABRIEL");
		else if(X == 2){
			if((R==1 && C ==4) || (R==2 && C ==2) || (R==2 && C ==3) || (R==2 && C ==4) || (R==3 && C ==4) || (R==4 && C ==4) || (R==1 && C ==2))
				printf("Case #%d: %s\n", g,"GABRIEL");
			else
				printf("Case #%d: %s\n", g,"RICHARD");
		}
		else if(X == 3){
			if((R==2 && C ==3) || (R==3 && C ==3) || (R==3 && C ==4))
				printf("Case #%d: %s\n", g,"GABRIEL");
			else
				printf("Case #%d: %s\n", g,"RICHARD");
		}
		else if(X == 4){
			if((R==3 && C ==4) || (R==4 && C ==4))
				printf("Case #%d: %s\n", g,"GABRIEL");
			else
				printf("Case #%d: %s\n", g,"RICHARD");

		}
		
		g++;
	}
return 0;
}