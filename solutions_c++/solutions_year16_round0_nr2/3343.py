//
//  main.cpp
//  Revenge of the Pancakes
//
//  Created by Rugen Heidbuchel on 09/04/16.
//  Copyright © 2016 Rugen Heidbuchel. All rights reserved.
//

#include <iostream>
#include <string>

bool isDone(std::string &stack) {
    for (auto c: stack) {
        if (c != '+') {
            return false;
        }
    }
    return true;
}

char invertCharacter(char character) {
    return character == '+' ? '-' : '+';
}


size_t T, count;
std::string pancakes;

int main(int argc, const char * argv[]) {
    
    #ifdef USE_INPUT_FILE
    freopen("input.txt", "r", stdin);
    #endif
    
    // MAIN Begin
    
    std::cin >> T;
    for (size_t caseNumber = 0; caseNumber < T; caseNumber++) {
        
        std::cin >> pancakes;
        count = 0;
        
        while (!isDone(pancakes)) {
            
            count++;
            
            char firstCharacter = pancakes[0];
            char invertedCharacter = invertCharacter(firstCharacter);
            
            size_t indexOfInverted = pancakes.find(invertedCharacter);
            
            if (indexOfInverted == std::string::npos) {
                indexOfInverted = pancakes.size();
            }
            
            for (size_t i = 0; i < indexOfInverted; i++) {
                pancakes[i] = invertCharacter(pancakes[i]);
            }
        }
        
        std::cout << "Case #" << caseNumber + 1 << ": " << count << std::endl;
    }
    
    // MAIN End
    
    return 0;
}