/* 
 * File:   main.cpp
 * Author: watcharin
 *
 * Created on April 9, 2015, 3:21 PM
 */

#include <stdio.h>

#include <cstdlib>
#include <algorithm>
#include <fstream>

#include <iomanip>
#include <iostream>

#include <sstream>
#include <string>
#include <vector>

using namespace std;

string solve(int x, int r, int c) {
    int area = r * c;
    int shorter = min(r, c);
    int longer = max(r, c);
    
    if (area % x != 0) {
        return "RICHARD";
    }
    
    if (x <= 2) {
        return "GABRIEL";
    }
    
    if (x >= 2 * (shorter + 1) - 1) {
        return "RICHARD";
    }
    
    if (x >= 2 * longer - 1) {
        return "RICHARD";
    }
    
    if (x == 4 && shorter <= 2) {
        return "RICHARD";
    }
    
    if (x >= 7) {
        return "RICHARD";
    }
    
    return "GABRIEL";
}

/*
 * 
 */
int main(int argc, char** argv) {
    char in_file_name[256];
    char out_file_name[256];
    
    sprintf(in_file_name, "%s.in", argv[1]);
    sprintf(out_file_name, "%s.out", argv[1]);
    
    ifstream infile(in_file_name);
    ofstream outfile(out_file_name);
    string line;
    
    getline(infile, line);
    istringstream iss(line);
    int cases;
    
    iss >> cases;
    
    for (int i = 0; i < cases; i++) {
        getline(infile, line);
        int x, r, c;
        
        istringstream iss(line);
        iss >> x >> r >> c;
        
        cout << "Solving Case " << (i + 1) << " ..." << endl;
        string rv = solve(x, r, c);
        
        outfile << "Case #" << (i + 1) << ": " << rv << endl;
    }
    
    return 0;
}
