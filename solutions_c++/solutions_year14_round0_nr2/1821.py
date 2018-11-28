#include<iostream>
#include<cstdio>
using namespace std;

int main(){
    int t,temp;
    scanf("%d", &t);
    temp = t;
    double x,c,f,answer,time;
    while(t>0){
        answer = 0;
        scanf("%lf%lf%lf", &c,&f,&x);
        time = ((x-c)/c)*(f);
        double a=2;
        while(a<time){
            answer+=c/a;
            a+=f;   
        }
        answer+=x/a;
        printf("Case #%d: ", temp-t+1);
        printf("%.7f\n", answer);
        t--;
    }
#ifdef DEBUG
    system("pause>nul");
#endif
    return 0;
}
