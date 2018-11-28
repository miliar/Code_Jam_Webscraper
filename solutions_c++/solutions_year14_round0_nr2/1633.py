//
//  main.cpp
//  abc
//
//  Created by mascure on 14-3-22.
//  Copyright (c) 2014年 mascure. All rights reserved.
//
#include <iostream>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <stdio.h>
#include <sstream>
#define MAX_N 505
#define MAX_Q 100
#define MAXK 100000
#define MAX_V 5005
#define MAX_E 100005
#define inf 1000005
using namespace::std;
typedef long long ll;

double C,F,X;
void solve(){
    double total=0.0,r=2.0;
    double c1=X/r,c2=C/r+X/(r+F);
    while (c1>c2) {
        total+=C/r;
        r+=F;
        c1=X/r,c2=C/r+X/(r+F);
    }
    printf("%.7f\n",total+c1);
}

int main()
{
    freopen("/Users/mascure/Desktop/B-large.in", "r", stdin);
    freopen("/Users/mascure/Desktop/B-large.out", "w", stdout);
    //freopen("/Users/mascure/Desktop/abc.in", "r", stdin);
    int caseN;
    cin>>caseN;
    for (int i=1; i<=caseN; i++) {
        scanf("%lf%lf%lf",&C,&F,&X);
        cout<<"Case #"<<i<<": ";
        solve();
    }
    return 0;
}

