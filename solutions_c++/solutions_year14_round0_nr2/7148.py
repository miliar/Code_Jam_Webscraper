//
//  main.cpp
//  2
//
//  Created by David on 14-4-12.
//  Copyright (c) 2014年 David. All rights reserved.
//

#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
#define N 5
double c, f, x, s;
int judge()
{
    double temp = (c/s) + (x/(s+f));
    if(x/s > temp)
        return 1;
    else
        return 0;
}
int main()
{
    freopen("/Users/david/Documents/x-code/google code jam/B-large.in", "r", stdin);
    freopen("/Users/david/Documents/x-code/google code jam/A-small-attempt0.out", "w", stdout);
    int k;
    cin>>k;
    string ans[N]= {"Case #",": "};
    for(int time = 1; time <= k; time++)
    {
        s= 2.0;
        double tot = 0,tt = 0;
        cin>>c>>f>>x;
        while(judge())
        {
            tt += c/s;
            s += f;
        }
        tt += x/s;
        printf("Case #%d: %.7lf\n",time,tt);
    }
    return 0;
}
   // freopen("/Users/david/Documents/x-code/google code jam/A-small-attempt4.in", "r", stdin);
  //  freopen("/Users/david/Documents/x-code/google code jam/A-small-attempt0.out", "w", stdout);


