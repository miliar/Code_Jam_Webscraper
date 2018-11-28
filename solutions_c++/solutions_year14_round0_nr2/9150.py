//
//  main.cpp
//  Code Jam 1
//
//  Created by Tony on 4/12/14.
//  Copyright (c) 2014 Tony. All rights reserved.
//
#include <iostream>
#include <vector>
#include <fstream>
#include <iomanip>
using namespace std;
ifstream infile;
ofstream outfile;
void cookie(double c, double f, double x) {
    double s   = 2;
    double t   = 0;
    while (x*f > c * (s + f)) {
        t += c/s;
        s += f;
    }
    t+= x/s;
    outfile<< fixed << setprecision(7) <<t<<"\n";
}
int main(int argc, const char * argv[])
{
    infile.open("/Users/Tony/Desktop/code jam/Code Jam 1/Code Jam 1/cookie.in");
    outfile.open("/Users/Tony/Desktop/code jam/Code Jam 1/Code Jam 1/cookie.out");
    int num_t;
    infile>>num_t;
    for (int i = 0; i < num_t; i++) {
        double c,f,x;
        infile>>c>>f>>x;
        outfile<<"Case #"<<i+1<<": ";
        cookie(c,f,x);
    }
    infile.close();
    outfile.close();
    return 0;
}

