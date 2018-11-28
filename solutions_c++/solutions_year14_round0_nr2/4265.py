#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

double time(double c, double f, double x){
    double cost = 0;
    int i = 0;
    double spd = 2.0;
    while(true){
        cost += c/spd;
        //to buy or not to buy
        if( (x-c)/spd < x/(spd+f) ){
            cost += (x-c)/spd;
            break;
        }
        else{
            spd += f;
        }
    }
    return cost;
}

int main(){
    int t;
    scanf ("%d",&t);
    for(int i=1;i<=t;i++){
        double c,f,x;
        scanf("%lf %lf %lf\n", &c, &f, &x);
        printf("Case #%d: %0.7lf\n", i, time(c,f,x));
    }
}