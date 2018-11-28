//
//  main.cpp
//  Cookie Clicker Alpha
//
//  Created by Tengqi Ye on 12/04/2014.
//  Copyright (c) 2014 Tengqi Ye. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <math.h>
#include <iomanip>

double greedSearch(double rate, double C, double F, double X);


int main(int argc, const char * argv[])
{

    //open files
    std::ifstream in;
    std::ofstream out;
    
    in.open("B-small-attempt0.in");
    out.open("B-small-attempt0.out");
    
    
    //global variables
    int T;
    double C, F, X;
    
    //in & out
    in >> T;
    for( int i = 0; i < T; i ++ )
    {
        in >> C >> F >> X;
        
        out << "Case #" << i + 1 << ": " << std::fixed << std::setprecision(7) << greedSearch(2, C, F, X) << std::endl;
    }
    
    
    
    //close files
    in.close();
    out.close();
    
    
    return 0;
}


double greedSearch(double rate, double C, double F, double X)
{
    double total_time = 0;
    double times = ceil( (X * F / C - rate)/F - 1 );
    
    if( times < 0 )
    {
        times = 0;
    }
    
    double current_rate = rate + F * times;
    total_time = X/current_rate;
    
    while(times > 0)
    {
        times --;
        current_rate -= F;
//        std::cout << C/current_rate << std::endl;
        total_time += C/current_rate;
    }
    
    return total_time;
}