//
//  main.cpp
//
//  Created by Virat Goyal on 09/04/16.
//  Copyright © 2016 Virat Goyal. All rights reserved.
//
#include <fstream>
#include <iostream>
#include <iostream>
#include <unordered_map>
using namespace std;
int main(int argc, const char * argv[]) {
    
    //long long int n= 100001;
    // int data;
    long long int n;
    
    ifstream infile;
    infile.open("input.txt");
    
    ofstream outfile;
    outfile.open("output.txt");
 //   long long int t;
    
    infile >> n;
 //   cout<<n;
    int temp=0;
    while(n--)
    {
        string s;
        temp++;
        infile>>s;
        int len = s.length();
        int count=0;
        //int flag=0;
        string s2="";
        while(true)
        {
            s2="";
            int pos=-1;
            for(int i=0;i<len;i++)
            {
                if(s[i]=='-')
                {
                    pos=i;
                }
            }
            if(pos==-1)
            {
                outfile<<"Case #"<<temp<<": "<<count<<endl;
                //flag=1;
                break;
            }
                count++;
            for(int i=0;i<=pos;i++)
            {
                if(s[i]=='+')
                    s2+='-';
                else
                    s2+='+';
            }
            for(int i=pos+1;i<len;i++)
                s2+=(s[i]);
            s=s2;
            
            }
    }
    outfile.close();
    infile.close();
    return 0;
}
