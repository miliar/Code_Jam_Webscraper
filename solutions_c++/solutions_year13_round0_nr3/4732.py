//
//  main.cpp
//  Fair_and_Square
//
//  Created by Jinchao Ye on 4/13/13.
//  Copyright (c) 2013 Jinchao Ye. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int T = 0;
long long A;
long long B;

bool isPalindrome(long long num)
{
    long long numcopy = num;
    long long newnum = 0;
    long long ans = num/10;
    long long rem = num - ans*10;
    num = ans;
    while(ans>0)
    {
        newnum = newnum * 10 + rem;
        ans = num/10;
        rem = num - ans*10;
        num = ans;
    }
    newnum = newnum * 10 + rem;
    
    return (newnum==numcopy);
}

void countFS(ofstream & fout, int t)
{
    int count = 0;
    long long start = ceil(sqrt(A+0.0));
    long long ss = start*start;
    while(ss <= B)
    {
        if(isPalindrome(start) && isPalindrome(ss))
            count++;
        start++;
        ss = start*start;
    }
    fout<<"Case #"<<t<<": "<<count<<"\n";
}

int main(int argc, const char * argv[])
{
    ifstream fin("/Users/jcye/Desktop/C.txt");
    ofstream fout("/Users/jcye/Desktop/C_result.txt");
    fin>>T;
    for(int i = 0; i < T; i++)
    {
        fin>>A;
        fin>>B;
        countFS(fout,i+1);
    }
    fin.close();
    fout.close();
    return 0;
}

