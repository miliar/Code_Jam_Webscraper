//
//  main.cpp
//  Magic Trick
//
//  Created by Umair Akhtar on 12/04/2014.
//  Copyright (c) 2014 Umair Ahmad. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;


void LoadData(double &C, double &F, double &X, ifstream & stream);
double computeSeconds(double C, double F, double X);
void WriteData(double secs,int i, ofstream & stream);


int main(int argc, const char * argv[])
{
    ifstream fin("B-small-attempt0.in.txt");
    ofstream fout("B-large.out");
    fout<<setiosflags(ios_base::fixed);
    fout.precision(6);
    int loop;
    fin>>loop;
    for(int i=1; i<=loop; i++) {
        
        double C, F, X;
        LoadData(C, F, X,fin);
        double secs = computeSeconds(C, F, X);
        WriteData(secs, i, fout);
        
    }
    fin.close();
    fout.close();
    
    
    return 0;
}

double computeSeconds(double C, double F, double X) {
    double cProfit = 2.0;
    double secs = 0.00000000000;
    while((X/cProfit) > ( (C / cProfit) + (X / (cProfit + F)))) {
        secs += C/cProfit;
        cProfit += F;
    }
    secs += X/cProfit;
    return secs;
}
void WriteData(double secs, int i, ofstream & stream) {
    
    stream<<"Case #"<<i<<": "<<secs<<endl;
}

void LoadData(double &C, double &F, double &X, ifstream & stream)
{
    stream>>C>>F>>X;
    
    
}
