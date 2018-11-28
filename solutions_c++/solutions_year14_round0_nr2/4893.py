#include<iostream>
#include<stdio.h>
#include<float.h>
using namespace std;

double myMin(double a, double b){
    if ((a-b)>DBL_EPSILON)
        return b;
    else
        return a;
}

double cookieTimeOptmization(double farmPrice, double increasingRate, double winPrice,double currentRate){
    if((currentRate-winPrice)>=DBL_EPSILON)
        return winPrice/currentRate;
    double timeNeeded=winPrice/currentRate;//just wait
    timeNeeded=myMin(timeNeeded,farmPrice/currentRate+cookieTimeOptmization(farmPrice,increasingRate,winPrice,(currentRate+increasingRate)));
    //printf("The currentSize is %.7f,The time needed is %.7f\n",currentRate,timeNeeded);
    return timeNeeded;
}

int main()
{
    FILE* inputFile=fopen("B-small-attempt8.in.txt","r");
    //FILE* inputFile=fopen("inputTemp.txt","r");
    FILE* outputFile=fopen("output.txt","a+");
    int iterator;
    fscanf(inputFile,"%d",&iterator);
    for(int ii=1;ii<=iterator;ii++){
        double C,F,X;
        fscanf(inputFile,"%lf",&C);// for a farm
        fscanf(inputFile,"%lf",&F);// increasing rate
        fscanf(inputFile,"%lf",&X);// destination
        F=F/10;
        double time=cookieTimeOptmization(C,F,X,0.2);
        fprintf(outputFile,"Case #%d: %.7f\n",ii,time/10);
        //printf("Case #%d: %.7f\n",ii,time/10);
    }
    return 0;
}