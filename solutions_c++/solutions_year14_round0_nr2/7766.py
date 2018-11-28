//
//  p2.cpp
//  GoogleCodeJam
//
//  Created by zhaoxm on 14-4-12.
//  Copyright (c) 2014年 zhaoxm. All rights reserved.
//

#include "p2.h"

#include <iostream>
#include <fstream>
#include <set>
#include <iomanip>

using namespace std;

double helper(double c, double f, double x){
    double pretime = x / 2.0;
    double current = 2.0;
    double time = 0;
    
    while(1){
        double temp = c/current + x/(current +f);
        if(temp  < pretime){
            time += c/current;
            current += f;
            pretime = x/(current);
        }else{
            break;
        }
    }
    time += x/current;
    
    return time;
}



int main(int argc, const char * argv[])
{
    ifstream in("/Users/zhaoxm/Study/interview/GoogleCodeJam/test.txt");
    if(! in.is_open()){
        cout << "Error opening file";
        exit(1);
    }
    while(! in.eof()){
        int count = 0;
        in >> count;
        for(int i = 1; i <= count; i++){
            double c, f, x;
            in >>c >>f >>x;
            
            cout <<setprecision(15) << "Case #"<< i <<": " << helper(c,f,x) << endl;
        }
    }
    return 0;
}