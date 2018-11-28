//
//  main.cpp
//  GCJ_2
//
//  Created by Yutian Liu on 13-4-13.
//  Copyright (c) 2013年 Yutian Liu. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

bool square(__INT64_TYPE__ num)
{
    __INT64_TYPE__ res = sqrt(num);
    if(res*res == num)
        return true;
    else
        return false;
}

bool pi(__INT64_TYPE__ num)
{
    __INT64_TYPE__ temp = num;
    int digit[100];
    int len=1;
    digit[0] = temp%10;
    temp = temp/10;
    while(temp!=0)
    {
        digit[len] = temp%10;
        temp = temp/10;
        len++;
    }
    int i;
    for(i=0;i<len/2+1;i++)
    {
        if(digit[i] != digit[len-1-i])
            return false;
    }
    return true;
    
    
}


int main(int argc, const char * argv[])
{
    ifstream infile;
    infile.open("C-large-1.in.txt",ios::in);
    ofstream outfile;
    outfile.open("output.txt",ios::out);
    
    int numOfSample;
    infile >> numOfSample;
    __INT64_TYPE__ A,B;
    int i;
    __INT64_TYPE__ j;
    int res = 0;
    for(i=0;i<numOfSample;i++)
    {
        res = 0;
        infile >> A >> B;
        __INT64_TYPE__ a = sqrt(A);
        __INT64_TYPE__ b = sqrt(B);
        a--;
        b++;
        for(j=a;j<=b;j++)
        {
            if(pi(j))
            {
                __INT64_TYPE__ t = j*j;
                if(square(t))
                   if(pi(t))
                       if(t >= A && t <= B)
                       {
                            res++;
                       }
            }
        }
        /*
        for(j=A;j<=B;j++)
        {
            if(square(j) && pi(j))
            {
                __INT64_TYPE__ n = sqrt(j);
                if(pi(n))
                    res++;
            }
                
        }
        */
        
        outfile << "Case #" << i+1 << ": "<< res <<endl;
    }
    infile.close();
    outfile.close();
    
    
    return 0;
}

