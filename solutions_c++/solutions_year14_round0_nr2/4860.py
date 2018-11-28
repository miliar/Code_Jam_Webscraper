//
//  main.cpp
//  AlgorithmStudy
//
//  Created by Young Seok Kim on 1/9/14.
//  Copyright (c) 2014 Young Seok Kim. All rights reserved.
//



#include <stdio.h>
#include <string.h>

// Problem B. Cookie Clicker Alpha

int T; // 1~100
double C,F,X;
double answers[101];


double function(int n)
{
    double sum = 0.0;
    for (int i=0; i<n; i++) {
        sum+=C/(2+(i*F));
    }
    return sum+(X/(2+n*F));
}





int main(int argc, const char * argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    scanf("%d", &T);
    for (int t=0; t<T; t++) {
        scanf("%lf %lf %lf", &C, &F, &X);
        int n=0;
        // Algorithm
        if (X/2 <= (C/2 + X/(2+F))) {
            answers[t]=X/2;
        }
        else {
            while (function(n) > function(n+1)) {
                n++;
            }
            answers[t]=function(n);
        }
        
        
    }
    
    
    for (int i=0; i<T; i++) {
        printf("Case #%d: %.7lf\n",i+1,answers[i]);
    }
    /*
    for (int k=0; k<10; k++) {
        printf("func %d is %f\n", k, function(k));

    }
     */
    
}











