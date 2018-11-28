//
//  main.cpp
//  pancakes
//
//  Created by Haneen Mohammed on 4/9/16.
//  Copyright © 2016 Haneen Mohammed. All rights reserved.
//


#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <stdio.h>      /* printf, fgets */
#include <set>
#include <sstream>      // std::ostringstream

using namespace std;

int flip (string stack) {
    int flag = 0;
    int k = 0;
    cout << stack << endl;
    if (stack.length() < 1) return 0;
    // check if there is unhappy pancake
    for (int i = 0; i < stack.length()+1; i++) {
        if (stack[i] == '-' && stack[i+1] != '-') {
            flag = 1;
            k = i;
            break;
        }
        
        if (i == (stack.length() -1)) {
            return 0;
        }
    }
    cout << stack << endl;
    // substitute from that i till the top one i = 0
    for (int i = 0; i <= k; i++) {
        if (stack[i] == '-') {
            stack[i] = '+';
        } else {
            stack[i] = '-';
        }
    }
    cout << stack << endl;
    return flip (stack) + 1;
}
int main(int argc, const char * argv[]) {
    string line;
    int T = 0;     // Number of test cases
    int x = 0;
    ofstream result;    // output file
    result.open ("/Users/haneen/codes/googleCodeJam/googleCodeJam/result.txt");
   
    
    ifstream myfile ("/Users/haneen/codes/googleCodeJam/googleCodeJam/sample.txt"); // input file
    if (!myfile.is_open()) {
        cout << "Failed to open file" << endl;
        exit (0);
    }
    getline (myfile,line);
    T = atoi(line.c_str());
    cout << "Number of Test Cases = " << T << endl;
    while ( getline (myfile,line) ) {
        cout << line << endl;
        int ans = flip (line);
        cout << "ans = " << ans << endl;
        x++;
        result << "Case #" << x << ": " << ans << endl;

    }
    
    result.close();
    myfile.close();
    return 0;
}
