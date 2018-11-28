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
using namespace std;



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
        int smax;
        char i;
        int ssum = 0;
        int invitees = 0;
        
        input >> smax;
        smax++;
        for (int s = 0; s < smax; s++) {
            input >> i;
            i -= 48;
            if (ssum < s) {
                ssum++;
                invitees++;
            }
            ssum += i;
        }
        

        
        cout << "Case #" << u+1 << ": ";
        cout << invitees;
        cout << endl;
    }

    return 0;
}
