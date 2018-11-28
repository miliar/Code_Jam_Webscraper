//
//  main.cpp
//  CodeJam2015_2_CPP
//
//  Created by Nataphol Baramichai on 4/11/2558 BE.
//  Copyright (c) 2558 krabrr. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <stdio.h>
#include <math.h>

using namespace std;

string solve(int x, int row, int col) {
    if (x > 6)
        return "RICHARD";
    double dhx = double(x)/2;
    //cout << "HXX: " << half_x << "\n";
    int ihx = ceil(dhx);
    //cout << "HX: " << ihx << "\n";
    if (ihx > row || ihx > col)
        return "RICHARD";
    if (x > 3 && (ihx >= row || ihx >= col))
        return "RICHARD";
    int blocks = row * col;
    if (blocks%x != 0)
        return "RICHARD";
    
    return "GABRIEL";
}

int main() {
    string line;
    //ifstream input ("test_input.txt");
    //ifstream input ("D-large.in.txt");
    ifstream input ("D-small-attempt4.in.txt");
    
    ofstream output ("output.txt");
    
    if (input.is_open()) {
        
        getline(input, line);
        int num_case = stoi(line);
        int caseIdx = 1;
        
        while (getline(input, line)) {
            vector<string> s_arr;
            istringstream iss(line);
            copy(istream_iterator<string>(iss),
                 istream_iterator<string>(),
                 back_inserter(s_arr));
            
            vector<int> arr;
            for (int i = 0; i < s_arr.size(); i++)
                arr.push_back(stoi(s_arr[i]));
                
            
            int x = arr[0];
            int row = arr[1];
            int col = arr[2];
            
            string result = solve(x, row, col);
            
            if (x != 1) {
                for (int i = 0; i < s_arr.size(); i++)
                    cout << stoi(s_arr[i]) << " ";
                cout << "-> " << result << "\n";
            }
            
            result = "Case #" + to_string(caseIdx) + ": " + result;
            if (caseIdx != num_case)
                result += "\n";
            if (output.is_open())
                output << result;
            
            caseIdx++;
        }
        input.close();
        output.close();
    }
    else {
        cout << "Unable to open file";
    }
    return 0;
}
