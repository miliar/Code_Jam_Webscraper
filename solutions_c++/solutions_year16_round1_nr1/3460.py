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
    
    int t;
    
    ifstream infile;
    infile.open("input.txt");
    
    ofstream outfile;
    outfile.open("output.txt");
    
    infile >> t;
    int temp=0;
    
    while(t--)
    {
        temp++;
        int len,count;
        string s;
        infile>>s;
        len= s.length();
        
        string output="";
        
        for(int i=0;i<len;i++)
        {
            /*char c= 'A';
            for(int j=i+1;j<len;j++)
            {
                if(s[j]>c)
                    c=s[j];
            }*/
            char d='A';
            if(output.length()>0)
            d=output[0];
            
            char cc= s[i];
            
            if(cc>=d)
                output= cc+output;
            else
                output= output+cc;
        }
        
        outfile<<"Case #"<<temp<<": "<<output<<endl;
        
        
        
    }
    outfile.close();
    infile.close();
    return 0;
}
