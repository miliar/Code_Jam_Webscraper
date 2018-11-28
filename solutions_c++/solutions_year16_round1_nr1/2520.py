//
//  main.cpp
//  The Last Word
//
//  Created by Rugen Heidbuchel on 16/04/16.
//  Copyright © 2016 Rugen Heidbuchel. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>

int main(int argc, const char * argv[]) {
    
    #ifdef USE_INPUT_FILE
    freopen("input.txt", "r", stdin);
    #endif
    
    // MAIN Begin
    
    size_t T;
    std::cin >> T;
    for (size_t caseNumber = 0; caseNumber < T; caseNumber++) {
        
        std::cout << "Case #" << caseNumber + 1 << ": ";
        
        std::string S;
        std::cin >> S;
        
        std::vector<char> largest;
        largest.push_back(S[0]);
        
        for (size_t i = 1; i < S.size(); i++) {
            if (S[i] >= largest[0]) {
                largest.insert(largest.begin(), S[i]);
            } else {
                largest.push_back(S[i]);
            }
        }
        
        std::string largestString(largest.begin(), largest.end());
        std::cout << largestString << std::endl;
    }
    
    // MAIN End
    
    return 0;
}