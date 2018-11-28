//
//  audience.cpp
//  partition
//
//  Created by Prasanna Prakash on 4/7/15.
//  Copyright (c) 2015 Prasanna Prakash. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    string s="";
    ifstream fin ("input.txt");
    ofstream fout("output.txt");
 
    int count=0;
    int c=0;
    int n;
    int i;
    getline(fin,s);
    n=atoi(s.c_str());
    
    
    for(int j=1;j<=n;j++)
    {
        getline(fin,s);
        string s1=s.substr(s.find(" ")+1);
        
        for (i=0; i<s1.length(); i++)
        {
            if(c<i)
            {
                count+=(i-c);
                c+=(i-c);
            }
            c+=s1[i]-'0';
        
        }
        fout<<"Case #"<<j<<": "<<count<<endl;
        c=0;
        count=0;
    }
    
    fin.close();
    fout.close();
    return 0;
}

