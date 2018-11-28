#include<stdio.h>
int main( )
{
    int t,x,r,c,i,j;
    scanf("%d",&t);
    for(i=1;i<=t;i++){
		scanf("%d%d%d",&x,&r,&c);
			if(x ==1) 
				printf("Case #%d: GABRIEL\n",i);
    	if(x==2){
        	if((r*c)% 2==0)
            	printf("Case #%d: GABRIEL\n",i);
        	else
            	printf("Case #%d: RICHARD\n",i);
    	}
		for(j=3;j<=20;j++){
			if(x==j){
				if(r*c%j==0){
					if(r<=j/2||c<=j/2) 
						printf("Case #%d: RICHARD\n",i);
					else  printf("Case #%d: GABRIEL\n",i);
				}
				else 
					printf("Case #%d: RICHARD\n",i);
				break;
			}
		}
	}
	return 0;
}