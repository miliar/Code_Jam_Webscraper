#include<iostream>
#include<stdio.h>

int const PI = 3.141592653589;

int main(){
    int T;
    scanf("%d", &T);
    for(int i=1;i<=T;i++){
        double r, d,t0;
        scanf("%lf %lf", &r,&t0);
        double a0=0;
        int c1=1;
        a0=t0*PI;
        a0=a0-(PI*((r+1)*(r+1)-(r*r)));
        d=r;
        while(1){
            d=d+2;
            a0=a0-(PI*((d+1)*(d+1)-(d*d)));
            if(a0>=0)
                c1++;
            else
                break;
        }
    printf("Case #%d: %d\n", i, c1);
    }
return 0;
}