//
//  main.cpp
//  CodeJam A
//
//  Created by Baker Mohd Anas on 4/12/14.
//  Copyright (c) 2014 Baker Mohd Anas. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <string.h>

int main(int argc, const char * argv[])
{
    freopen("/Users/Baker/Desktop/CodeJam_A/B.in", "r", stdin);
    freopen("/Users/Baker/Desktop/CodeJam_A/B.out", "w", stdout);
    // insert code here...
    
    int Case = 1, test;
    double C,F,X;
    
    scanf("%d",&test);
    
    
    while(test--)
    {
        scanf("%lf %lf %lf",&C, &F, &X);
        
        double rate = 2.0;
        double total_time = 0.0;
        
        while( X/rate > (C/rate + X/(rate+F)) )
        {
            total_time += C/rate;
            rate += F;
        }
        
        total_time += X/rate;
        printf("Case #%d: %.7lf\n",Case++, total_time);
        
    }
    
    return 0;
}

