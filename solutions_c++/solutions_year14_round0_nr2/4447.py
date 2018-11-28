//
//  main.cpp
//  Magic Trick
//
//  Created by hijackyan on 4/12/14.
//  Copyright (c) 2014 leetcode. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
int main(int argc, const char * argv[])
{
    int t;
    double c,f,x;
    cin>>t;
    int Case = 1;
    while(t--)
    {
        cin>>c>>f>>x;
        double speed = 2.0;
        double time = x/speed;
        double buytime = 0.0;
        while(1)
        {
            buytime += c/speed;
            speed += f;
            if(time > buytime + x/speed)
                time = buytime + x/speed;
            else
                break;
        }
        printf("Case #%d: %.9f\n",Case, time);
        Case++;
    }
}

