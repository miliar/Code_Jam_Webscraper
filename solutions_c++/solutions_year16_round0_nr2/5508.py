//
//  main.cpp
//  code_jam_2
//
//  Created by divya gupta on 09/04/16.
//  Copyright (c) 2016 divya gupta. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

int main() {
    // your code goes here
   // freopen("/Users/divyagupta/Desktop/input.txt","r",stdin);
   // freopen("/Users/divyagupta/Desktop/out.txt","w",stdout);
    int t,i,j;
    cin>>t;
    int x=1;
    while(t--)
    {
        string s;
        cin>>s;
        i=s.size()-1;
        while(s[i]=='+')
        {
            i--;
        }
        if(i<0)
        {
            cout<<"Case #"<<x<<":"<<" "<<"0"<<endl;
        }
        else
        {
            int flag=0;
            int ct=0;
            for(j=i;j>=0;j--)
            {
                if(s[j]=='-' && (s[j]!=s[j+1] || j==s.size()-1 ) && flag==0)
                {
                    ct++;
                }
                else if(s[j]=='-' && s[j]!=s[j+1] && flag==1)
                {
                    ct+=2;
                }
                else if(s[j]=='+' && s[j]!=s[j+1] )
                {
                    flag=1;
                }
            }
            if(s[0]=='+')
            {
                ct++;
            }
            cout<<"Case #"<<x<<":"<<" "<<ct<<endl;
        }
        x++;
    }
    
    return 0;
}