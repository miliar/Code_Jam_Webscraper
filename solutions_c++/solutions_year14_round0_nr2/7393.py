#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

bool solved=false;
double c, f, x;

double v=         2.000000000;
double time_delta=0.000000000;

int main(){
    int t;
    scanf("%d", &t);
    for(int i = 1; i<=t;i++){
        scanf("%lf%lf%lf", &c, &f, &x);
        time_delta=0.00000000;
        v=2.00000000;
        for( ; ; ){
            double time1=x/v;              //withoutn factory
            double time2=c/v + x/(v+f);    //otherwise
            //printf("time1: %lf, time2: %lf, v: %lf", time1, time2, v);
            //printf(", timedelta: %lf\n", time_delta);
            if(time1<time2){
                time_delta+time1;
                time_delta+=time1;
                break;
            }
            else{
                time_delta+=c/v;
                v+=f;
            }
            //getchar();
        }
        printf("Case #%d: %.7lf\n", i, time_delta);
    }
}
