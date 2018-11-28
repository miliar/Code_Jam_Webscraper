//
//  main.cpp
//  Codeforces
//
//  Created by Taygrim on 20.03.13.
//  Copyright (c) 2013 Taygrim. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

bool check(long long n)
{
    long long nn = n, n1 = 0;
    while(nn)
    {
        n1 = n1*10 + nn %10;
        nn/=10;
    }
    return (n == n1);
}

int main()
{
    ifstream cin("C-large-1.in.txt");
    ofstream cout("output.txt");
    
    long t;
    cin>>t;
    for(long w=0; w<t; w++)
    {
        long long a, b;
        long long res = 0;
        cin>>a>>b;
        for(long long i=0; ; i++)
        {
            long long temp, tmp;
            tmp = temp = i;
            tmp/=10;
            while(tmp!= 0)
            {
                temp = temp * 10 + tmp % 10;
                tmp/=10;
            }
            
            temp = temp * temp;
            if(temp > b)
                break;
            if(temp >=a && temp <=b && check(temp))
                res++;
            
            
            tmp = temp = i;
            while(tmp!= 0)
            {
                temp = temp * 10 + tmp % 10;
                tmp/=10;
            }
            
            temp = temp * temp;
            if(temp >=a && temp <=b && check(temp))
                res++;
        }
        cout<<"Case #"<<w+1<<": "<<res<<"\n";
    }

}












