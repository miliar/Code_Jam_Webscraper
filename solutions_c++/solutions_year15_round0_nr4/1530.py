#include<stdio.h>
#include<iostream>
using namespace std;

int main(){

	//freopen("D.in","r",stdin);
    freopen("D-small-attempt3.in","r",stdin);
    freopen("D-small-attempt3.out","w",stdout);

    int T,X,R,C,i;

    scanf("%d",&T);
    for(i=1; i<=T; i++)
    {
    	scanf("%d %d %d",&X,&R,&C);
      	if(X==1){
            printf("Case #%d: GABRIEL\n",i);
    	}
    	else if( (X==2 && R==1 && C==1)
             ||(X==2 && R==1 && C==3)
             ||(X==2 && R==3 && C==1)
             ||(X==2 && R==3 && C==3)
             || (X==3 && R==1 && C==1)
             || (X==3 && R==1 && C==2)
             || (X==3 && R==1 && C==3)
             || (X==3 && R==1 && C==4)
             || (X==3 && R==2 && C==1)
             || (X==3 && R==2 && C==2)
             || (X==3 && R==2 && C==4)
             || (X==3 && R==3 && C==1)
             || (X==3 && R==4 && C==1)
             || (X==3 && R==4 && C==2)
             || (X==3 && R==4 && C==4)){

                printf("Case #%d: RICHARD\n",i);
        }
        else if(X==4){
            if((R==3 && C==4)||(R==4 && C==3)||(R==4 && C==4)){
                printf("Case #%d: GABRIEL\n",i);
            }
            else{
                printf("Case #%d: RICHARD\n",i);
            }
    	}
    	else{
         printf("Case #%d: GABRIEL\n",i);
    	}
    }
    return 0;
}
