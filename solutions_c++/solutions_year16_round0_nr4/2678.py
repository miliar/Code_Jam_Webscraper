//
//  main.cpp
//  Fractiles
//
//  Created by Rugen Heidbuchel on 09/04/16.
//  Copyright © 2016 Rugen Heidbuchel. All rights reserved.
//

#include <iostream>
#include <cmath>

size_t T, K, C, S, blockSize;

int main(int argc, const char * argv[]) {
    
    #ifdef USE_INPUT_FILE
    freopen("input.txt", "r", stdin);
    #endif
    
    // MAIN Begin
    
    std::cin >> T;
    for (size_t caseNumber = 0; caseNumber < T; caseNumber++) {
        
        std::cout << "Case #" << caseNumber + 1 << ":";
        
        std::cin >> K >> C >> S;
        blockSize = (size_t)std::pow((double)K, (double)(C-1));
        
        for (size_t i = 0; i < K; i++) {
            std::cout << " " << i * blockSize + 1;
        }
        
        std::cout << std::endl;
    }
    
    // MAIN End
    
    return 0;
}