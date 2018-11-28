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
//    ifstream infile ("/Users/ted/Downloads/A-small-attempt0.in.txt");
    ifstream infile ("/Users/ted/Downloads/A-large.in.txt");
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
 *
 */
void solve(ifstream& infile, ofstream& outfile){
    string line;
    getline(infile, line);
    stringstream ss(line);
    int T;
    ss >> T;
    for (int tt=0; tt<T; tt++) {
        getline(infile, line);
        vector<char> res;
        for (int i=0; i<line.length(); i++) {
            char ch = line.at(i);
            if (res.size() > 0 && ch >= res.at(0)) {
                res.insert(res.begin(), ch);
            } else {
                res.push_back(ch);
            }
        }
        cout << "Case #" << (tt+1) << ": ";
        outfile << "Case #" << (tt+1) << ": ";
        for (vector<char>::iterator it=res.begin(); it!=res.end(); ++it) {
            cout << (*it);
            outfile << (*it);
        }
        cout << endl;
        outfile << endl;
    }
}