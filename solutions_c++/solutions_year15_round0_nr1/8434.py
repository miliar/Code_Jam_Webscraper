//
//  main.cpp
//  StandingOvation
//
//  Created by Sarah Azouvi on 11/04/2015.
//  Copyright (c) 2015 Sarah Azouvi. All rights reserved.
//

#include <iostream>
#include <fstream>

#include<stdio.h>
#include<string>
#include <vector>
#include <cmath>

using namespace std;

int main(int argc, const char * argv[]) {
    int T;
    FILE *input = fopen("/Users/sarahazouvi/Downloads/A-large.in", "r");
    ofstream out("/Users/sarahazouvi/Desktop/output2.in.txt");
    fscanf(input,"%i",&T);
    
    for (int t=1; t<=T;t++){
        int Smax;
        fscanf(input,"%i\t",&Smax);
        int* N =new int[Smax+1];
        int ct=0;
        char c=fgetc(input);
        N[0]=c-'0';
        if (N[0]==0) ct=1;
        int sum=N[0];
        for (int i=1;i<=Smax;i++){
            char c=fgetc(input);
            N[i]=c- '0';
            
            if ((sum+ct)<i && N[i]!=0) ct+=i-sum-ct;
            
            sum+=N[i];
            // cout<<N[i]<<endl;
            
        }
        out <<"Case #"<<t<<": "<<ct<<endl;
        delete [] N;
    }//end loop cases
    return 0;
}