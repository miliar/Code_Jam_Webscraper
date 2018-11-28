//
//  main.cpp
//  codejamProblemB
//
//  Created by Vena Jia Li on 4/11/14.
//  Copyright (c) 2014 Vena Jia Li. All rights reserved.
//


#include <iostream>
#include <string>
#include <cmath>
#include <climits>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <ctime>
#include <memory.h>
using namespace std;


int main()
{
    int t;
    double c,f,x;

   // freopen("/Users/vena/Documents/vena/codejam/A-large-practice.txt","r",stdin);
    freopen("/Users/vena/Documents/vena/codejam/B-large.in","r",stdin);
    freopen("/Users/vena/Documents/vena/codejam/B-large-output.txt","w",stdout);
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        double remain=x;
        double time=0.0;
        double currentrate=2.0;
        while(1)
        {
            if(remain<c)
            {
                time=time+remain/currentrate;
                break;
            }
            
            if(remain/(currentrate+f)<=(remain-c)/currentrate)//then buy it
            {
                time+=c/currentrate;
                currentrate+=f;
            }
            else
            {
                time+=remain/currentrate;
                break;
            }
            
          }
        printf("Case #%d: %.7lf\n",i+1,time);

    }
    
    
    return 0;
}



