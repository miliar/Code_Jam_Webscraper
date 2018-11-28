/* -*- Mode: C; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- */

/*  Mafijski praktikum naloga
 *  =========================
 *  Copyright 2015 Domen Ipavec <domen.ipavec@z-v.si>
 *
 *  Licensed under the MIT License (the "License");
 */


#include <iostream>
#include <cmath>
#include <fstream>
#include <random>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <string>
#include <stdint.h>
using namespace std;

double epsilon = 0.00001;

int main(int argc, char *argv[]) {
    cout.precision(10);
    ifstream input;
   
    if (argc < 2) {
        input.open("data.dat");
    } else {
        input.open(argv[1]);
    }
    
    
    uint64_t n;
    input >> n;
    
    for (uint64_t u = 0; u < n; u++) {
        cerr << "Start " << u << endl;
        
        int N;
        double V;
        double X;
        input >> N >> V >> X;
        
        double seconds;
        
        if (N == 1) {
            double R, C;
            input >> R >> C;
            
            if (abs(C - X) > epsilon) {
                seconds = -1;
            } else {
                seconds = V/R;
            }
        } else {
            double R1, C1, R2, C2;
            input >> R1 >> C1;
            input >> R2 >> C2;
            
            if ((C1 > X && C2 > X) || (C1 < X && C2 < X)) {
                seconds = -1;
            } else if (C1 == C2) {
                seconds = V/(R1 + R2);
            } else {
                double s1 = V/R1*(X-C2)/(C1-C2);
                double s2 = V/R2*(X-C1)/(C2-C1);
                seconds = max(s1,s2);
            }
        }
        
        cout << "Case #" << u+1 << ": ";
        if (seconds == -1) {
            cout << "IMPOSSIBLE";
        } else {
            cout << seconds;
        }
        cout << endl;
        cerr << "done" << endl;
    }

    return 0;
}
