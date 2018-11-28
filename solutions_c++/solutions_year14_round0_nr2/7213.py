//
//  main.cpp
//  Cookie Clicker Alpha
//
//  Created by SourKream on 12/04/14.
//  Copyright (c) 2014 SourKream. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;


int main(int argc, const char * argv[])
{
    fstream fil;
    fil.open("input.txt",ios::in);
    int cases;
    fil >> cases;
    for(int i=1;i<=cases;i++)
    {
        cout << "Case #" << i << ": ";
        long double C, F, X;
        fil >> C >> F >> X;
        long double  Time=0;
        long double rate = 2;
        while(X/rate > C/rate + X/(rate+F))
        {
            Time += C/rate;
            rate += F;
        }
        
        Time += X/rate;
        
        cout << setprecision(9) << Time << endl;
        
    }
    fil.close();
    
    return 0;
}

