//
//  main.cpp
//  1
//
//  Created by Harshit Singh on 11/05/14.
//  Copyright (c) 2014 Harshit Singh. All rights reserved.
//

#include <iostream>
#include<iomanip>
#include<string.h>
#include <fstream>
#include<cmath>
using namespace std;
long long int greatestCommonDivisor(long long int m, long long int n)
{
    long long int r;
    
    /* Check For Proper Input */
    if((m == 0) || (n == 0))
    return 0;
    else if((m < 0) || (n < 0))
    return -1;
    
    do
    {
        r = m % n;
        if(r == 0)
        break;
        m = n;
        n = r;
    }
    while(true);
    
    return n;
}
long long int func(long long int n)
{
    long long int no=0;
    long long int s=2;
    while(n>=s)
    {
        s=s*2;
        no++;
    }
    return no;
}
long long int primeq(long long int n)
{
    while(n>1)
    {
        if(n%2!=0)
        {
            n=-1;
            break;
        }
        n=n/2;
    }
    if(n==-1)
    return 1;
    else
    return 0;
}
int main(int argc, const char * argv[])
{
    long long int t,p,q,pq,hcf;
    char pc,qc,bar;
    int i;
    long long int den,num,ans;
    ifstream myReadFile;
    myReadFile.open("abc.in");
    if (myReadFile.is_open())
    {
    myReadFile>>t;
    for(i=1;i<=t;i++)
    {
        p=0;
        q=0;
        
        myReadFile>>bar;
        while(bar!='/')
        {
            p=10*p+(bar-'0');
            myReadFile>>bar;
        }
       // cout<<p;
        myReadFile>>q;
        hcf=greatestCommonDivisor(p,q);
        p=p/hcf;
        q=q/hcf;
        pq=primeq(q);
        if(pq!=1)
        {
            den=func(q);
            num=func(p);
            ans=den-num;
        }
        else
        
        {
            ans=-5;
        }
        ofstream myfile;
        myfile.open ("output35.txt",std::fstream::out | std::fstream::app);
        if(ans<0)
        {
            myfile<<"Case #"<<i<<": "<<"impossible"<<endl;
        }
        else
        {
            myfile<<"Case #"<<i<<": "<<ans<<endl;
        
        }
        myfile.close();
    }
        
    }
    return 0;
}

