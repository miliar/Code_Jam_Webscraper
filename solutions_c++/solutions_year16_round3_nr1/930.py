//
//  main.cpp
//  pa
//
//  Created by Rongbin Li on 5/7/16.
//  Copyright © 2016 Rongbin Li. All rights reserved.
//

#include <iostream>
#include <vector>
#include <fstream>
#include <cassert>
#include <algorithm>
using namespace std;

void outputAns(int p[], int n, ofstream &fout) {
    int sum = 0;
    for (int i=0; i<n; i++) {
        sum += p[i];
    }
    while (sum > 0) {
        int k = int(max_element(p, p+n) - p);
        int count = 0;
        for (int i = 0; i<n; i++) {
            if (p[i] == p[k]) count++;
        }
        if (count == 1) {
            fout << ' ' << (char) ('A'+k);
            sum--;
            p[k]--;
        } else {
            int x = p[k];
            int k2=0;
            for (int i=0; i<n; i++) {
                if (i != k && p[i] == x) {
                    k2 = i;
                    break;
                }
            }
            if (x >= 2 || sum == 2) {
                fout << ' ' << (char) ('A'+k) << (char) ('A'+k2);
                sum-=2;
                p[k]--;
                p[k2]--;
            } else {
                fout << ' ' << (char) ('A'+k);
                sum--;
                p[k]--;
            }
        }
    }
}

int main(int argc, const char * argv[]) {
    ifstream fin("A-large.in");
    assert(fin);
    ofstream fout("pa-large.out");
    assert(fout);
    int test;
    fin >> test;
    for (int k = 1; k<=test; k++) {
        int n;
        fin >> n;
        int p[n];
        for (int i=0; i<n; i++) {
            fin >> p[i];
        }
        fout << "Case #" << k << ":";
        outputAns(p, n, fout);
        fout << endl;
    }
    fin.close();
    fout.close();
    
    return 0;
}
