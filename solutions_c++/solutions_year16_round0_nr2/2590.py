//
//  main.cpp
//  Google Code Jam
//
//  Created by xiaoxin ren on 4/8/16.
//  Copyright © 2016 xiaoxin ren. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
const string FILENAME = "B-large";

int totalFlips(string &s) {
    size_t n = s.size();
    int flip = 0;
    for (size_t i = 1; i < n; i++) {
        if (s[i-1] != s[i]) flip ++;
    }
    if (s[n-1] == '-') flip ++;
    return flip;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int n = 0;
    string seq = "";
    ifstream fin (FILENAME+ ".in");
    ofstream fout (FILENAME + ".out");
    if (fin.is_open()){
        fin >> n;
        for (int i = 0; i< n; i++) {
            fin >> seq;
            fout << "Case #" << i+1 << ": " << totalFlips(seq) << '\n';
        }
    }
    
    return 0;
}
