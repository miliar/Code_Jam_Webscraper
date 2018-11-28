#include <stdio.h>
#include <algorithm>

double cookie(double g, double y);
double farm(double cost, double r, double addr, double goal);
using namespace std;

int main(){
FILE*input;
FILE*output;

input=fopen("B-large.in","r");
output=fopen("output.txt","w");

int t=0;
double c=0,f=0,x=0,cks=0,rate=2,tc=0,tf=0,time=0;

fscanf(input,"%d",&t);
for(int k=1;k<=t;k++){
    fscanf(input, "%lf %lf %lf", &c, &f, &x);
    while(cks!=x){
        tc=cookie(rate,x);
        tf=farm(c,rate,f,x);
        if(tc<tf){
            time+=tc;
            fprintf(output, "Case #%d: %f\n",k, time);
            break;
        }
        else{
            time+=c/rate;
            rate+=f;
        }
        //printf("tf = %f, tc = %f,  time= %f\n", tf, tc, time);
    }
    rate=2;
    time=0;
}

fclose(input);
fclose(output);
}

double cookie(double g, double y){
    //printf("hi y=%f, g=%f\n", y,g);
    return (y/g);
}
double farm(double cost, double r, double addr, double goal){
    double t1=0,t2=0;
    t1= cost/r;
    r+=addr;
    t2=goal/r;
    return(t1+t2);
}
