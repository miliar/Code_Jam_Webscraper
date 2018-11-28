//
//  main.cpp
//  google.code.jam.2014
//
//  Created by Daniel on 12/4/14.
//  Copyright (c) 2014 Daniel. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <math.h>
#include <set>
using namespace std ;

double cookie3(int farm, double p,double C,double F,double X)
{
    double t=0;
    for(int i =0;i<farm;i++)
    {
        
        t += C/p;
        p += F;
    }
    return t += X/p;
}
double cookie2(double x,double p,double C,double F,double X)
{
    //C = 30.50000;F=3.14159;X=1999.19990;p=2;x=X;
    double t = 0,tOld = t;
    int n=0;
    int farm = 0;
    
    while ( n<2 || t<tOld ) {
        tOld = t;
        t = cookie3(farm, p, C, F, X);
        farm ++;
        n++;
        
    }
    return tOld;
    
    
}
void solve()
{
    double C,F,X,p=2;
    cin >> C;
    cin >> F;
    cin >> X;
    cout <<cookie2(X,p, C,F, X);
    cout <<endl;
    
    
}
int Main()
{
    int testCase;
    cin >> testCase;
   //testCase = 1;
    for (int caseId = 1;caseId<=testCase;caseId++)
    {
        cout << "Case #"<<caseId<<": ";
        solve();
    }
    return 0;
}

int main(int argc, const char * argv[])
{
    
    cout.precision(7);
    cout.setf(ios::fixed,ios::floatfield);
    
    freopen("B-large.in", "r", stdin);
    freopen("out.txt","w",stdout);
    Main();
    
    return 0;
}

