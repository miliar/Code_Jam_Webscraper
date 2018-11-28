//
//  main.cpp
//  gcj
//
//  Created by Jinfu Leng on 4/11/14.
//  Copyright (c) 2014 jinfu. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const double ddd =0.0000001;
double Time(double C, double F, double X){
    double bestTime = X/2.0;
    int cnt=1;
    double farmTime = 0.0;
    while(1){
        double newFarmTime = C/(2.0+cnt*F-F)+farmTime;
        double newTime = newFarmTime + X/(2.0+cnt*F);
        //cout<<bestTime<<" "<<newTime<<endl;
        if(bestTime<newTime || (bestTime-newTime)<ddd)
            return bestTime;
        bestTime=newTime;
        farmTime=newFarmTime;
        cnt++;
    }
}
int main(int argc, const char * argv[])
{
    freopen("/Users/jinfu/Workspace/test/input.in","r",stdin);
    freopen("/Users/jinfu/Workspace/test/output","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=0;t<T;t++){
        printf("Case #%d: ",t+1);
        double C,F,X;
        scanf("%lf %lf %lf",&C,&F,&X);
        printf("%.7lf\n", Time(C,F,X));
    }
    return 0;
}

