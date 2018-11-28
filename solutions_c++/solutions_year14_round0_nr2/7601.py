#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
    int t;
    scanf("%d\n",&t);
    for (int i=0; i<t; i++) {
        double c,f,x,t1,t2;
        double r=2,time;
        
        printf("Case #%d: ",i+1);
        scanf("%lf %lf %lf\n",&c,&f,&x);
        //printf("%lf %lf %lf\n",c,f,x);
        time = 0;
        do {
            t1=x/r;
            t2=(c/r)+x/(r+f);
            if (t1>t2) {
                time += c/r;
                r+=f;
            }
        }while(t1>t2);
        time += x/r;
        printf("%.7lf\n", time);
    }
}