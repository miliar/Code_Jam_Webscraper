#include<stdio.h>


int main()
{
	char ch;
	int T, i, j;
	int r[4], c[4], d[2], a[4][4], l;
	int resultPossible;
	scanf("%d",&T);
	for(int it =0; it < T; it++) {
		printf("Case #%d: ",(it+1));
		resultPossible = 0;
		l = -1;
		r[0]=r[1]=r[2]=r[3]=1;
		c[0]=c[1]=c[2]=c[3]=1;
		d[0]=d[1]=1;
		int count = 0, t = 0;
		while(count  <16){
			i = count/4;
			j = count%4;
			scanf("%c",&ch);
			switch(ch){
				case 'T': l = count; a[i][j] = 1;  break;
				case 'X': a[i][j]=1;		break;
				case 'O': a[i][j]=0;		break;
				case '.' :  a[i][j]=-1;
							r[i]=0; c[j]=0; 
							if(i==j) d[0]=0;
							if((i+j)==3) d[1]=0;
							t++; break;
				default: count--;	break;			
			}
			count++;
		}

		while(1) {
		//Row Column.
		for(int k =0 ; k <4; k++)
		{
			int X =0, Y = 0;
				if(r[k]){
					X = a[k][0] & a[k][1] & a[k][2] & a[k][3];
					if(X){
					 resultPossible =1;
					 printf("X won");
					 break;		  
					}	
					Y = (a[k][0]^1) & (a[k][1]^1) & (a[k][2]^1) & (a[k][3]^1);
					if(Y) {
					 resultPossible =1;	
					 printf("O won");			
					 break;
					}					
									
				}
				if(c[k]) {
					
					X = a[0][k] & a[1][k] & a[2][k] & a[3][k];
					if(X){
					 resultPossible =1;
					 printf("X won");
					 break;		  
					}
						
					
				 	Y = (a[0][k]^1) & (a[1][k]^1) & (a[2][k]^1) & (a[3][k]^1);
					if(Y) {
					 resultPossible =1;	
					 printf("O won");			
					 break;
					}				
	 
				}

		}
		
		//Diagonal.
		if(!resultPossible)
		{
			int X = 0, Y = 0;		
			if(d[0]) {
			X = (a[0][0] & a[1][1] & a[2][2] & a[3][3]);
			if(X){
			 resultPossible =1;
			 printf("X won");
			 break;		  
			}
			
			Y = ((a[0][0]^1) & (a[1][1]^1) & (a[2][2]^1) & (a[3][3]^1));
			if(Y) {
			 resultPossible =1;	
			 printf("O won");			
			 break;
			}			
			
			}
			
			if(d[1]) {
			X = (a[0][3] & a[1][2] & a[2][1] & a[3][0]);
			if(X){
			 resultPossible =1;
			 printf("X won");
			 break;		  
			}				
				
			Y =((a[0][3]^1) & (a[1][2]^1) & (a[2][1]^1) & (a[3][0]^1));
			if(Y) {
			 resultPossible =1;	
			 printf("O won");			
			 break;
			}			
			}
		}
		
			
			if(l>=0 && !resultPossible) {
				a[l/4][l%4] = 0;
				l=-1;		 
			}
			else
				break;
				
		}
	
		if(!resultPossible)
		{
			if(t)
			 printf("Game has not completed");
		 	else
	 		 printf("Draw");
		}
		
		printf("\n");
	}
}
