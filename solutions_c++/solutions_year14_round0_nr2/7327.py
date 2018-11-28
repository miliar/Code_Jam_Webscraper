#include<string.h>
#include<map>
#include<iostream>
#include<utility>
#include<math.h>
#include<algorithm>
#include<stdio.h>
#include<stdlib.h>
#define DBG 0
using namespace std;



void process(double C, double F, double X) {
    int numOfFarm = 0;
    double constRate = 2.0;
    double time1;
    double prevTime=0.0;
    double minTime = X / constRate;
    //to reach the value X using N number of farms,
    //time required = {timeTo produce X cookies at speed of (2.0 + N*F)}   +   {time to create N farms (C/2.0 + C/(2.0+F) + C/(2.0+2*F) + ... + C/(2.0+(N-1)*F)   ))}
    while (numOfFarm*C<X) {
	time1 = X/(constRate + numOfFarm*F)+prevTime;
	minTime = minTime < time1 ? minTime : time1;
	prevTime = prevTime + (C/(constRate + numOfFarm*F));                   
	numOfFarm++;
    } 
    //cout<<std::setprecision(7)<<minTime;
    printf("%.7f", minTime);
}

int main() {
    int T;
    double C, F, X;
    cin>>T;
    int count=0;
    while(T>0) {
        count++;
        T--;
	cin>>C;
	cin>>F;
	cin>>X;
        cout<<"Case #"<<count<<": ";
        process(C, F, X);
        cout<<"\n";
    }
    return 0;
}

