//
//  main.cpp
//  2015_1A_A
//
//  Created by Liubing Yu on 4/17/15.
//  Copyright (c) 2015 Liubing Yu. All rights reserved.
//


#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>
using namespace std;
ifstream ifs ("/Users/yuliubing/Desktop/input.txt", std::ifstream::in);
ofstream ofs ("/Users/yuliubing/Desktop/output.txt", std::ofstream::out);
int p[1000];
void go(int n){
    int l;
    for (int i = 0; i < n; i++){
        ifs >> l;
        p[i] = l;
    }
    cout << n <<" ";
    int temp = p[0];
    int total = 0;
    int maxS = 0;
    for (int i= 1; i< n; i++){
        if(p[i] < temp)
        {
            maxS = max( maxS, -p[i]+temp);
            total += -p[i]+temp;
        }
        temp = p[i];
    }
    cout << total <<" A "<< maxS <<endl;
    int left = p[0];
    int totalE = 0;
    for( int j = 1; j < n; j++)
    {
        if(maxS > left)
        {
            totalE += left;
        }
        else
        {
            totalE += maxS;
        }
        left = p[j];
    }
    cout << total <<" "<<totalE;
    ofs << total <<" "<<totalE;
    
}

int main(int argc, const char * argv[]) {
    int n,l;
    
    ifs >> n;
    cout << n <<" a"<<endl;
    for (int i = 0; i < n; i++){
        ifs >> l;
        cout << "Case #" << i + 1 << ": ";
        ofs << "Case #" << i + 1 << ": ";
        go(l);
        cout << endl;
        ofs << endl;
    }
    std::cout << "Hello, World!\n";
    return 0;
}


