//
//  main.cpp
//  Cookie Clicker Alpha
//
//  Created by Estelle :) on 12/4/14.
//  Copyright (c) 2014 AWESOMENESS. All rights reserved.
//

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    freopen("/Users/student/Downloads/B-large.in", "r", stdin);
    int T;
    scanf("%d", &T);
    for (int i=0; i<T; i++)
    {
        double c,f,x,rate=2.0;
        scanf("%lf%lf%lf", &c, &f, &x);
        double time=0.0;
        bool done=false;
        while (!done)
        {
            double t_need=x/rate;
            double farm=c/rate+x/(rate+f);
            if (t_need>farm)
            {
                time+=c/rate;
                rate+=f;
            }
            else {
                done=true;
            }
        }
        time+=x/rate;
        cout<<"Case #"<<i+1<<": "<<fixed<<setprecision(7)<<time<<endl;
    }
}

