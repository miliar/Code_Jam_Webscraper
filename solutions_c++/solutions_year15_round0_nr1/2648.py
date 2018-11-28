/* 
 * File:   main.cpp
 * Author: watcharin
 *
 * Created on April 9, 2015, 3:21 PM
 */

#include <stdio.h>

#include <cstdlib>
#include <fstream>

#include <iomanip>
#include <iostream>

#include <sstream>
#include <string>
#include <vector>

using namespace std;

int solve(int max_s, vector<int> amount) {
    int rv = 0;
    int supporters = 0;
    
    for (int i = 0; i <= max_s; i++) {
        if (supporters >= i) {
            supporters += amount[i];
        }
        else {
            rv += i - supporters;
            supporters = i + amount[i];
        }
    }
    
    return rv;
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
        int max_s;
        string amount;
        
        istringstream iss(line);
        iss >> max_s >> amount;
        
        vector<int> v_amount;
        for (char& c : amount) {
            v_amount.push_back(c - '0');   
        }
        
        int rv = solve(max_s, v_amount);
        
        outfile << "Case #" << (i + 1) << ": " << rv << endl;
    }
    
    return 0;
}
