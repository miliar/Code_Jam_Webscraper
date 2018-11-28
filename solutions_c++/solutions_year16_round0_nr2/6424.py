//
//  main.cpp
//  RevengeOfPancakes
//
//  Created by Raymond Tse on 4/8/16.
//  Copyright © 2016 Raymond Tse. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>

int calcFlips(std::string input) {
    
    int result;
    
    if (input == "-") {
        return 1;
    } else if (input == "+") {
        return 0;
    } else {
        
        std::vector<char> groups = {};
        int grpindex = 0;
        groups.push_back(input[0]);
        
        for(char x: input)
        {
            if (x != groups[grpindex])
            {
                groups.push_back(x);
                grpindex++;
            }
        }
        
        if (groups.back() == '-') {
            return groups.size();
        } else {
            return groups.size() -1;
        }
    }
}

int main(int argc, const char * argv[]) {
    std::ifstream inFp(argv[1]);
    
    if (!inFp.is_open())
    {
        fprintf(stderr, "Can't open the file");
        exit(1);
    }
    
    std::ofstream outFp("out.txt");
    
    int numInputs;
    std::string input;
    int result;
    
    inFp >> numInputs;
    
    for (int i = 0; i < numInputs; i++)
    {
        inFp >> input;
        result = calcFlips(input);
        outFp << "Case #" + std::to_string(i+1) + ": "+std::to_string(result)+"\n";
    }
    
    inFp.close();
    outFp.close();
    
    return 0;
}
