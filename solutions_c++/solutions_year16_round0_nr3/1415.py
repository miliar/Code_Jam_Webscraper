//
//  main.cpp
//  AlgorithmStudy
//
//  Created by 김태우 on 2015. 12. 30..
//  Copyright © 2015년 김태우. All rights reserved.
//

#include <stdio.h>
#include <memory.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <cassert>

using namespace std;

void solve(ifstream& infile, ofstream& outfile);

int main(int argc, const char * argv[]) {
    string line;
//    ifstream infile ("/Users/ted/Downloads/C-small-attempt1.in.txt");
    ifstream infile ("/Users/ted/Downloads/C-large.in.txt");
//    ifstream infile ("/Users/ted/Downloads/test.in.txt");
    if (infile.is_open()) {
        ofstream outfile;
        outfile.open("/Users/ted/Downloads/out.txt");
        solve(infile, outfile);
        outfile.close();
        infile.close();
    } else {
        cout << "Unable to open file";
    }
    return 0;
}

int jamcoin(int* jc, int base, int N) {
    int divisor = 0;
    for (int a=2; a<2000; a++) {
        int r = jc[0];
        for (int b=1; b<N; b++) {
            r = ((r * base) + jc[b]) % a;
        }
        if (r == 0) {
            divisor = a;
            break;
        }
    }
    return divisor;
}

/**
 * Problem C. Coin Jam
 * https://code.google.com/codejam/contest/6254486/dashboard#s=p2
 */
void solve(ifstream& infile, ofstream& outfile){
    string line;
    getline(infile, line);
    stringstream ss(line);
    int T;
    ss >> T;
    for (int a=0; a<T; a++) {
        getline(infile, line);
        stringstream ss(line);
        int N, J;
        ss >> N >> J;
        
        cout << "Case #" << (a+1) << ":" << endl;
        outfile << "Case #" << (a+1) << ":" << endl;
        
        int jc[N];
        memset(jc, 0, sizeof(jc));
        jc[0] = 1;
        jc[N-1] = 1;
        
        int divisor[11];
        int jj = 0;
        
        while (jj < J) {
            bool success = true;
            for (int base=2; base<=10; base++) {
                divisor[base] = jamcoin(jc, base, N);
                if (divisor[base] == 0) {
                    success = false;
                    break;
                }
            }
            if (success) {
                for (int d=0; d<N; d++) {
                    cout << jc[d];
                    outfile << jc[d];
                }
                for (int base=2; base<=10; base++) {
                    cout << " " << divisor[base];
                    outfile << " " << divisor[base];
                }
                cout << endl;
                outfile << endl;
                jj++;
            }
            
            // 다른 jc로 변경
            for (int b=1; b<N-1; b++) {
                if (jc[b] == 0) {
                    jc[b] = 1;
                    break;
                } else {
                    jc[b] = 0;
                }
            }
        }
    }
}