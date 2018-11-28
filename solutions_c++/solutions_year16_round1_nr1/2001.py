//
//  main.cpp
//  TheLastWord
//
//  Created by Raymond Tse on 4/15/16.
//  Copyright © 2016 Raymond Tse. All rights reserved.
//

#include <iostream>
#include <fstream>


int main(int argc, const char * argv[]) {
    std::ifstream inFp(argv[1]);
    
    if (!inFp.is_open())
    {
        fprintf(stderr, "Can't open the file");
        exit(1);
    }
    
    std::ofstream outFp("out.txt");
    
    int numInputs;
    std::string word;
    
    
    inFp >> numInputs;
    
    for (int i = 0; i < numInputs; i++)
    {
        inFp >> word;
        std::string finalword;
        if (word.length() > 0) {
            finalword = word[0];
            for (int x = 1; x< word.length(); x++) {
                char c = word[x];
                if (c >= finalword[0]) {
                    finalword.insert(0,1, c);
                } else {
                    finalword.push_back(c);
                }
            }
            
        } else {
            finalword = "";
        }
        outFp << "Case #" + std::to_string(i+1) + ": " + finalword +"\n";
    }
                          
    inFp.close();
    outFp.close();
                          
    return 0;
}