//
//  revenge_pancakes.cpp
//  CodeJam_2016
//
//  Created by Snehil Vishwakarma on 4/8/16.
//  Copyright © 2016 Indiana University Bloomington. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <string.h>

using namespace std;

int main()
{
    int T,i,s,e,x,y;
    char ch;
    long ans;
    
    ifstream f1;
    f1.open("IS2_2016.in");
    ofstream f2;
    f2.open("OS2_2016.out");
    
    f1>>T;
    string NS;
    getline(f1,NS,'\n');
    for(i=0;i<T;i++)
    {
        string N;
        getline(f1,N,'\n');
        ans=0;
        
        s=0;
        e=(int)N.length()-1;
        while(N[e]=='+')
            e--;
        while(s<=e)
        {
            if(N[s]=='+')
            {
                x=s+1;
                while(N[x]=='+')
                    x++;
                x--;
                while(x>=s)
                {
                    N[x]='-';
                    x--;
                }
                ans++;
            }
            x=s;
            y=e;
            while(x<=y)
            {
                ch=N[x];
                if(N[y]=='-')
                    N[x]='+';
                else
                    N[x]='-';
                if(ch=='-')
                    N[y]='+';
                else
                    N[y]='-';
                x++;
                y--;
            }
            ans++;
            while(N[e]=='+')
                e--;
        }
        f2<<"Case #"<<(i+1)<<": "<<ans<<"\n";
    }
    return 0;
}