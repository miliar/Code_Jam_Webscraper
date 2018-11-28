//
//  main.cpp
//  CodeJamRound1
//
//  Created by Shangqi Wu on 16/4/15.
//  Copyright © 2016 Shangqi Wu. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;


string generateLastWord(const string& input) {
    
    string result;
    
    for (const char& c : input) {
        
        if (result.empty() || c < result[0]) {
            result += c;
        } else {
            result = c + result;
        }
        
    }
    
    return result;
    
}


int main(int argc, const char * argv[]) {
    
    ifstream input("./A-large.in");
    ofstream output("./output.txt");
    
    if (!input.is_open() || !output.is_open()) {
        return -1;
    }
    
    int numTestCase = 0;
    string line;
    input >> numTestCase;
    
    for (int caseNum = 1; caseNum <= numTestCase; caseNum++) {
        
        input >> line;
        output << "Case #" << caseNum << ": ";
        
        output << generateLastWord(line);
        
        output << endl;
        line.clear();
        
    }
    
    input.close();
    output.close();
    
    return 0;
}
