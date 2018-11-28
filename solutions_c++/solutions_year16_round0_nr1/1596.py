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

using namespace std;

void test();
void solve(ifstream& infile, ofstream& outfile);

int main(int argc, const char * argv[]) {
    string line;
    ifstream infile ("/Users/ted/Downloads/A-large.in.txt");
//    ifstream infile ("/Users/ted/Downloads/test.in.txt");
    if (infile.is_open()) {
        ofstream outfile;
        outfile.open("/Users/ted/Downloads/out.txt");
        solve(infile, outfile);
//        test();
        outfile.close();
        infile.close();
    } else {
        cout << "Unable to open file";
    }
    return 0;
}

void test(){
}

/**
 * Problem A. Counting Sheep
 * https://code.google.com/codejam/contest/6254486/dashboard
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
        int N;
        ss >> N;
        int nn = 0;
        string str;
        bool ckd[10];
        int ckdn = 0;
        memset(ckd, false, sizeof(ckd));
        
        for (int b=0; b<100; b++) {
            nn += N;
            str = to_string(nn);
            for (int c=0; c<str.length(); c++) {
                // check and fill
                int m = str.at(c) - '0';
                if (!ckd[m]) {
                    ckd[m] = true;
                    ckdn++;
                }
            }
            // if full, break
            if (ckdn == 10) {
                break;
            }
        }
        if (nn == 0) {
            cout << "Case #" << (a+1) << ": INSOMNIA" << endl;
            outfile << "Case #" << (a+1) << ": INSOMNIA" << endl;
        } else {
            cout << "Case #" << (a+1) << ": " << nn << endl;
            outfile << "Case #" << (a+1) << ": " << nn << endl;
        }
    }
}