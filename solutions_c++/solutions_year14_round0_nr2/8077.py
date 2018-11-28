//
//  main.cpp
//  CookieClicker
//
//  Created by Minghui Liu on 4/12/14.
//  Copyright (c) 2014 Minghui Liu. All rights reserved.
//

#include <iostream>
#include <iomanip>

using namespace std;

void solve(int i, double c, double f, double x){
    double currentV = 2.0;
    double finalV=2.0;
    int itr = 0;
    while(true){
        if(c*currentV+c*f-x*f>0){
            finalV = currentV;
            break;
        }
        currentV+=f;
        itr+=1;
    }
    int j;
    double time = 0.0;
    for(j=0;j<itr;j++){
        time += c/(2.0+f*j);
    }
    time += x/finalV;
    cout << fixed;
    cout<<"Case #"<<i+1<<": "<<setprecision(7)<<time<<endl;
}



int main(int argc, const char * argv[])
{
    freopen("/Users/minghui/Documents/C++/CookieClicker/CookieClicker/B-large.in.txt", "r", stdin);
    freopen("/Users/minghui/Documents/C++/CookieClicker/CookieClicker/B-large.out.txt", "w", stdout);
    int T;
    cin >> T;
    int i;
    for(i=0;i<T;i++){
        double c, f, x;
        cin >> c >> f >> x;
        solve(i,c,f,x);
    }
    return 0;
}

