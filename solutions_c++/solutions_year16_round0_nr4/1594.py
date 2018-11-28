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
#include <math.h>

using namespace std;

void solve(ifstream& infile, ofstream& outfile);

int main(int argc, const char * argv[]) {
    string line;
    ifstream infile ("/Users/ted/Downloads/D-small-attempt0.in.txt");
//    ifstream infile ("/Users/ted/Downloads/D-large.in.txt");
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
        int K, C, S;
        ss >> K >> C >> S;
        
        cout << "Case #" << (a+1) << ":";
        outfile << "Case #" << (a+1) << ":";
        
        // small set 에서 K=S 이므로 K만 신경쓰자.
        unsigned long long res;
        for (int b=0; b<K; b++) {
            if (C == 1) {
                res = b + 1;
            } else if (C == 2) {
                res = (K * b) + b + 1;
            } else {
                res = (pow(K, C-1) * b) + (pow(K, C-2) * b) + b + 1;
            }
            cout << " " << res;
            outfile << " " << res;
        }
        cout << endl;
        outfile << endl;
    }
}