#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(){
    int T;
    scanf("%d",&T);
    float c,f,x,time,kue,rate,temp;
    for(int i=1;i<=T;i++){
            rate =2;
            time = 0;
            kue = 0;
            temp = 0;
            scanf("%f %f %f",&c,&f,&x);
            while(1){
                     //printf("time = %f\n",time);
                     kue = x/rate + time;
                     temp = x/(rate+f) + time + c/rate;
                     if(kue <= temp ){
                            time = kue;
                            break;
                     }
                     else{
                          
                          time += c/rate;
                          rate+=f; 
                     }
            }
            printf("Case #%d: %f\n",i,time);
    
    }


return 0;
}
