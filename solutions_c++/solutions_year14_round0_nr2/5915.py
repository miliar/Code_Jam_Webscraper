//
//  B.m
//  GoogleCodeJam2014
//
//  Created by dabao on 14-4-12.
//  Copyright (c) 2014年 Dabaopku. All rights reserved.
//

#import <Foundation/Foundation.h>
#include <stdio.h>
#include <iostream>
using namespace std;

double C, F, X;
double t1, t2, t;
double amount;
double v;

void input()
{
    cin>>C>>F>>X;
    t1 = 0;
    t2 = 0;
    t = 0;
    amount = 0;
    v = 2;
}

void solve()
{
    while (true) {
        t1 = t + X / v;
        t2 = t + C / v + X / (v + F);
        if (t1 < t2) {
            break;
        }
        t += C / v;
        v += F;
    }
    
    printf("%.7f\n", t1);
}

int main(int argc, const char * argv[])
{
    
    @autoreleasepool {
        
        freopen("/Users/dabao/Desktop/GoogleCodeJam2014/GoogleCodeJam2014/B/in", "r", stdin);
        freopen("/Users/dabao/Desktop/GoogleCodeJam2014/GoogleCodeJam2014/B/out", "w", stdout);
        
        int CaseNum;
        cin>>CaseNum;
        for (int i = 0; i < CaseNum; ++i) {
            printf("Case #%d: ", i + 1);
            input();
            solve();
        }
        
    }
    return 0;
}

