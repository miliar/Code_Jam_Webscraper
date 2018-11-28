#include<cstdio>
#include<iostream>
using namespace std;

int main(){
    int t;
    int cn = 1;
    double  C, F, X;
    scanf("%d", &t);
    while(cn<=t){
        /*
        scanf("%f", &C);
        scanf("%f", &F);
        scanf("%f", &X);*/
        cin >> C >> F >> X;
        if(C>=X) printf("Case #%d: %0.7f\n", cn, X/2.0);
        else{
            double rate = 2.0;
            double secs=0.0;
            while((X/rate) > ((X/(rate+F))+(C/rate))){
                secs += C/rate;
                rate += F;
            }
            secs += X/rate;
            printf("Case #%d: %0.7f\n", cn, secs);
        }
        cn++;
    }
}
