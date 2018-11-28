//
//  B.cpp
//  codejam
//
//  Created by jie zheng on 14-4-12.
//  Copyright (c) 2014年 jie zheng. All rights reserved.
//
#include <iostream>
#include <iomanip>
using namespace std;

#define EPS 1e-7
double c,f,x;
double ans;
bool flag;
void solve(double fn, double cookies, double times)
{
    if(flag && times > ans)
        return;
    if(cookies - x < EPS && cookies - x > -EPS)
    {
        if(flag)
            ans = min(ans, times);
        else
        {
            ans = times;
            flag = true;
        }
        return;
    }
    

    double t2 = (x-cookies)/fn;
    solve(fn, x, times+t2);
    double t1 = (c-cookies)/fn;
    solve(fn+f, 0, times+t1);
}

int main()
{
    freopen("/Users/jiezheng/Dev/poj/B-small-attempt0.in", "r", stdin);
    freopen("/Users/jiezheng/Dev/poj/b1-out.txt", "w", stdout);
    int T;
    cin>>T;
    for(int i = 0; i < T; ++i)
    {
        flag = false;
        cin>>c>>f>>x;
        solve(2, 0, 0);
        cout<<setiosflags(ios::fixed)<<setprecision(7)<<"Case #"<<i+1<<": "<<ans<<endl;
        
    }
    return 0;
}