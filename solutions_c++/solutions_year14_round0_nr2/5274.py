//
//  main.cpp
//  b.cpp
//
//  Created by Duo Donald Zhao on 4/12/14.
//  Copyright (c) 2014 Duo Donald Zhao. All rights reserved.
//

#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;


int main(int argc, const char * argv[])
{
    int N;
    double C, F, X;
    cin >> N;
    for (int i = 1; i <= N; i++){
        cin >> C >> F >> X;
        double bestNumChangeDouble = X/C - 2.0/F - 1.0;
        int bestNumChangeInt = bestNumChangeDouble < 0 ? 0.0 : ceil(bestNumChangeDouble);
        double totaltime = (double) X / (2.0 + F * bestNumChangeInt);
        for (int j = 0; j < bestNumChangeInt; j++){
            totaltime += C / (2.0 + F * j);
        }
        cout << "Case #" << i << ": " << fixed << setprecision(7) << totaltime<< endl;
    }
    return 0;
}

