//
//  main.cpp
//  beautyofcode
//
//  Created by 甄晓磊 on 14-4-11.
//  Copyright (c) 2014年 甄晓磊. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main(int argc, const char * argv[])
{
    // insert code here..
    FILE *fp;
    fp = freopen("data.txt", "r", stdin);
    FILE *fp1;
    fp1 = freopen("out.txt", "w", stdout);
    int T;
    cin>>T;

    for (int i=1; i<=T; i++) {
        double C,F,X;
        cin>>C>>F>>X;
        if (X<=C) {
            cout<<setiosflags(ios::fixed);
            cout.precision(7);
            cout<<"Case #"<<i<<": "<<X/2.0<<endl;
            continue;
        }
        double rate=2;
        double time=C/rate;
        while ((X-C)*F>=C*rate) {
            rate+=F;
            time+=C/rate;

        }
        time+=(X-C)/rate;
        cout<<setiosflags(ios::fixed);
        cout.precision(7);
        cout<<"Case #"<<i<<": "<<time<<endl;
    }
    
    return 0;
}



