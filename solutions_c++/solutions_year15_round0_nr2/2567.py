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

int estimate(vector<int>& pancakes) {
    int rv = *max_element(pancakes.begin(), pancakes.end());
    
    return rv;
}

int solve(int d, vector<int> pancakes) {
    int t = 0;
    int upper = estimate(pancakes);
    
    for (int target = upper - 1; target > 0; target--) {
        bool ok = false;
        
        for (int special = 1; special < target; special++) {
            int allowed = target - special;
            
            vector<int> alter = pancakes;
            
            for (int i = 0; i < special; i++) {
                sort(alter.begin(), alter.end(), greater<int>());
                
                alter[0] -= allowed;
                alter.push_back(allowed);
            }
            
            sort(alter.begin(), alter.end(), greater<int>());
            if (alter[0] <= allowed) {
                ok = true;
                break;
            }
        }
        
        if (!ok) {
            return target + 1;
        }
    }
    
    return upper;
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
        int d;
        
        istringstream iss(line);
        iss >> d;
        
        getline(infile, line);
        istringstream ss_pancakes(line);
        
        vector<int> pancakes;
        string item;
        while (getline(ss_pancakes, item, ' ')) {
            istringstream ss_item(item);
            int p;
            
            ss_item >> p;
            
            pancakes.push_back(p);
        }
        
        int rv = solve(d, pancakes);
        
        outfile << "Case #" << (i + 1) << ": " << rv << endl;
    }
    
    return 0;
}
