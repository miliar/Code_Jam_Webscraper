//
//  main.cpp
//  Cookie Clicker
//
//  Created by xanxus on 14-4-13.
//  Copyright (c) 2014年 xanxus. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main(int argc, const char * argv[])
{

    // insert code here...
    FILE* inputFile=fopen(argv[1], "r");
    int testCount=0;
    fscanf(inputFile, "%d",&testCount);
    double* testCase=new double[testCount];
    for (int i=0; i<testCount; i++) {
        double F=0,C=0,X=0;
        fscanf(inputFile, "%lf %lf %lf",&C,&F,&X);
        double time=0,speed=2;
        
        while (X/speed>(C/speed+X/(speed+F))) {
            time+=C/speed;
            speed+=F;
        }
        testCase[i]=time+X/speed;
    }
    fclose(inputFile);
    FILE* outputFile=fopen("./output", "w");
    for (int i=0; i<testCount; i++) {
        fprintf(outputFile, "Case #%d: %.07lf\n",i+1,testCase[i]);
    }
    fclose(outputFile);
    return 0;
}

