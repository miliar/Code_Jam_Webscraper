//
//  main.cpp
//  Fair and Square__CodeJam2013
//
//  Created by Marcin's Mac on 13.04.2013.
//  Copyright (c) 2013 Marcin's Mac. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <math.h>
using namespace std;

short int t;
short int a,b;
short int output [10010];
int help;
int asqrt;
int sqrthelp;

int length(int n)
{
    int x=0;
    while (n>0)
    {
        n=n/10;
        x++;
    }
    return x;
}
int backwards(int number, int len)
{
    int output=0;
    int zz=0;
    len--;
    while(len>=0)
    {
        zz=number%10;
        number=number/10;
        output=output+(zz*pow(10, len));
        len--;
    }
    return output;
}

int main()
{
    
    cin>>t;
    int i=0;
    while (i<t)
    {
        cin>>a>>b;
        while (a<=b)
        {
            help=length(a);
            asqrt=sqrt(a);
            sqrthelp=length(asqrt);
            if (backwards(a, help)==a && backwards(asqrt, sqrthelp)*backwards(asqrt, sqrthelp)==a)
            {
                output[i]++;
            }
            
            a++;
        }
        
        i++;
    }
    i=0;
    while (i<t)
    {
        cout<<"Case #"<<i+1<<": "<<output[i]<<endl;
        i++;
    }
    
    
    
    
    
    getchar();
    cin.ignore();
    return 0;
}

