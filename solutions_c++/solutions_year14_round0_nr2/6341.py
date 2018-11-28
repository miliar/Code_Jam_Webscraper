#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    FILE *in,*out;
    in=fopen("B-large.in","r");
    out=fopen("output1.txt","w");
    int t,k=1;
    fscanf(in,"%d",&t);
    while(k<=t){
            double c,f,x,y,t=0;
        fscanf(in,"%lf %lf %lf",&c,&f,&x);
        //fprintf(out,"%lf,%lf,%lf",c,f,x);
        y=2;
    while(x/y>c/y+x/(y+f)){
        t=t+c/y;
        y=y+f;
    }
        t=t+x/y;
        fprintf(out,"Case #%d: %.7lf\n",k,t);
        k++;
    }

}
