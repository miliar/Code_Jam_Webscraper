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
#include <algorithm>
using namespace std;

int f(vector<int> plates, int n) {
    int maximum = *max_element(plates.begin(), plates.end());
    
    // priprava delov maximuma
    vector<int> parts(n, 0);
    for (int i = 0; i < n-1; i++) {
        parts[i] = maximum/n;
    }
    parts[n-1] = maximum - (n-1)*parts[0];
    
    // razdelitev
    int special_mins;
    int d = plates.size();
    for (int i = 0; i < d; i++) {
        if (plates[i] == maximum) {
            plates[i] = parts[0];
            for (int j = 1; j < n; j++) {
                plates.push_back(parts[j]);
                special_mins += 1;
            }
        }
    }
    
    // nov maximum in nmax
    maximum = 0;
    int nmax = 0;
    for (int i = 0; i < plates.size(); i++) {
        if (plates[i] > maximum) {
            maximum = plates[i];
            nmax = 1;
        } else if (plates[i] == maximum) {
            nmax++;
        }
        //cout << plates[i] << ' ';
    }
   // cout << endl;
    
    // nove razdelitve
    int j = 2;
    int best = maximum;
    while ((j-1)*nmax + maximum/j <= maximum && maximum > 1 && j <= maximum) {
        int vf = f(plates, j);
        if (vf < best) {
            best = vf;
        }
        j++;
    }
    
    return best + special_mins;
}

int main(int argc, char *argv[]) {
    cout.precision(10);
    ifstream input;
   
    if (argc < 2) {
        input.open("data.dat");
    } else {
        input.open(argv[1]);
    }
    
    
    int n;
    input >> n;
    
    for (int u = 0; u < n; u++) {
        int d;
        input >> d;
        vector<int> plates(d,0);
        for (int i = 0; i < d; i++) {
            input >> plates[i];
        }
        
        int best = f(plates, 1);
        
        cout << "Case #" << u+1 << ": ";
        cout << best;
        cout << endl;
    }

    return 0;
}
