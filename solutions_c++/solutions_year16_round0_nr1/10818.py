//
//  main.cpp
//  stacks
//
//  Created by Vipul Modi on 09/04/16.
//  Copyright © 2016 Vipul Modi. All rights reserved.
//
#include<iostream>
#include <fstream>
#include <string>

using namespace std;

bool flags[13];

bool isDone()
{
    int i;
    for(i=0;i<10;i++)
    {
        if(!flags[i])
        {
            return false;
        }
    }
    return true;
    
}
int main()
{
    int t;
    string line;
    ifstream infile ("/Users/vipul.modi/Desktop/stacks/stacks/input.txt");
    ofstream outfile ("/Users/vipul.modi/Desktop/stacks/stacks/output.txt");
    if (infile.is_open())
    {
        getline (infile,line);
        t=stoi(line);
        //cout<<t<<endl;
        //outfile<<t<<endl;
        int i=1;
        std::fill(std::begin(flags), std::end(flags), false);
        while (i<=t)
        {
            getline (infile,line);
            long long n = (long long)(stoi(line));
            if(n==0)
            {
                outfile<<"Case #"<<i<<": INSOMNIA"<<endl;
            }
            else
            {
                long long j=1;
                long long curr;
                while(j<INT32_MAX)
                {
                    curr=j*n;
                    while(curr>0)
                    {
                        flags[curr%10L]=true;
                        curr/=10L;
                    }
                    if(isDone())
                    {
                        std::fill(std::begin(flags), std::end(flags), false);
                        break;
                    }
                    j++;
                }
                if(j==INT32_MAX)
                {
                    outfile<<"Case #"<<i<<": INSOMNIA"<<endl;
                }
                else
                {
                    outfile<<"Case #"<<i<<": "<<(j*n)<<endl;
                }
            }
            i++;
        }
        infile.close();
    }
    else
    {
        cout<<"Open failed!!"<<endl;
    }
}
