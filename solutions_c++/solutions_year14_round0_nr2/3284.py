#include <stdio.h>
#include <iostream>

int main(){
    int T,temp;
    double C,F,X,sum=0;

    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        scanf("%lf %lf %lf",&C,&F,&X);
        sum=C/2;
        if(C>=X){
            printf("Case #%d: %.7lf\n",i,X/2);
        }else{
            for(int j=0;1;j++){
                if((X-C)/(2+j*F) < X/(2+(j+1)*F)){
                    sum+=(X-C)/(2+j*F);
                    break;
                }
                sum+=C/(2+(j+1)*F);
            }
            printf("Case #%d: %.7lf\n",i,sum);
        }
    }
}
