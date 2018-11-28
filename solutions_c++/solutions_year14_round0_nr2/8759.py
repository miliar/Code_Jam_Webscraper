#include<stdio.h>

int main(){
    int t;
    double c,x,f,solution,speed,temp,temp1;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        solution = 0.0;
        speed = 2.0;
        scanf("%lf %lf %lf",&c,&f,&x);
        while((temp1=c/speed) + x/(speed+f) < (temp = x/speed)){
            solution += temp1;
            speed = speed + f;
        }
        solution += temp;
        printf("Case #%d: %.7lf\n",i,solution);
    }
    return 0;
}