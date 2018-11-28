#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<string.h>
#include<vector>
#include<cmath>
#include<limits.h>
#define MOD 1000000009
#define MAX 1005

using namespace std;


double fun(double C,double F,double X){
    double rate = 2;
    double answer=0;
    while(1){
        if(X/rate<=C/rate+(X/(rate+F))){
            answer += X/rate;
            return answer;
        }
        else{
            answer += C/rate;
            rate += F;
        }
    }
}
int main(){

    
    int test;
    double X,C,F;
    scanf("%d",&test);
    for(int i=1;i<=test;i++){
        double answer=0;
        scanf("%lf%lf%lf",&C,&F,&X);
        answer=fun(C,F,X);
        printf("Case #%d: %.7lf\n",i,answer);
    }
    return 0;
}
