//
//  main.cpp
//  revenge_of_the_pancakes
//
//  Created by Quintin-Donnelly on 4/9/16.
//  Copyright © 2016 Quintin-Donnelly. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ifstream inF;
    ofstream outF;
    
    inF.open("B-large.in");
    outF.open("b-large.out");
    
    unsigned int t;
    inF >> t;
    
    string input;
    int diff = 0;
    for(int test_case = 1; test_case < t+1; ++test_case)
    {
        inF >> input;
        
        for(unsigned int p = 1; p < input.size(); ++p)
        {
            if(input[p] != input[p-1])
                ++diff;
        }
        
        if(input[input.size() -1] == '-')
            ++diff;
        
        outF << "Case #" << test_case << ": " << diff << endl;
        diff = 0;
    }
    
    inF.close();
    outF.close();
    
    return 0;
}
