#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;
int main()
{
    double C,F,X,TOTAL_time,CURRENT_time;
    int i,T;
    scanf("%d",&T);
    for(i=0;i<T;i++)
    {
                    TOTAL_time=0;
                    CURRENT_time=2;
                    scanf("%lf%lf%lf",&C,&F,&X);
                    while(!((X/CURRENT_time) < (C/CURRENT_time)+(X/(CURRENT_time+F))))
                    {
                                TOTAL_time=TOTAL_time+(C/CURRENT_time);
                                CURRENT_time=CURRENT_time+F;
                    }
                    
                    TOTAL_time=TOTAL_time+(X/CURRENT_time);
                    printf("Case #%d: %lf\n",i+1,TOTAL_time);
    }
    return 0;
}
