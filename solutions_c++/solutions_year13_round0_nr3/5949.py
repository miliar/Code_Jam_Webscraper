//
//  main.cpp
//  codejam-fairsquare
//
//  Created by Rajat on 4/13/13.
//  Copyright (c) 2013 Rajat. All rights reserved.
//


#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <cstdlib>
#include <sstream>
using namespace std;

int fs[1001];

int getrev(int a){
    int b = 0;
    while(a>0){
        b = (b+(a%10))*10;
        a/=10;
    }
    return b/10;
}

int main(int argc, const char * argv[])
{
    ifstream infile;
    infile.open("/Users/rajat/Documents/xcode/codejam/codejam-fairsquare/C-small-attempt0.in");
    ofstream outfile;
    outfile.open("/Users/rajat/Documents/xcode/codejam/codejam-fairsquare/problem2out-small.txt");
    
    for(int i = 0; i<=1000; i++){
        fs[i] = 0;
    }
    
    for(int i = 1; i<=40; i++){
        if(i == getrev(i))
        {
            int sq = i*i;
            if(sq <=1000 && sq == getrev(sq))
            {
                fs[sq] = 1;
//                cout<<sq<<endl;
            }
        }
    }
    
    
    int t,ctr = 0;
    infile>>t;
    while(t--){
        int a,b,c=0;;
        infile>>a>>b;
        
        for(int i = a; i<=b; i++)
        {
            if(fs[i]==1)
                c++;
        }
        outfile<<"Case #"<<++ctr<<": ";
        outfile<<c<<endl;
    }
    return 0;
}

