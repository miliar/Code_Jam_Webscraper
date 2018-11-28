//
//  main.cpp
//  Counting Sheep
//
//  Created by Rugen Heidbuchel on 09/04/16.
//  Copyright © 2016 Rugen Heidbuchel. All rights reserved.
//

#include <iostream>
#include <bitset>


std::bitset<10> digitsInNumber(size_t number) {
    std::bitset<10> digits;
    do {
        size_t digit = number % 10;
        digits[digit] = true;
        number /= 10;
    } while (number > 0);
    return digits;
}


size_t T, N, i, iN;
std::bitset<10> digitsDone;

int main(int argc, const char * argv[]) {
    
    #ifdef USE_INPUT_FILE
    freopen("input.txt", "r", stdin);
    #endif
    
    // MAIN Begin
    
    std::cin >> T;
    
    for (size_t caseNumber = 0; caseNumber < T; caseNumber++) {
        
        digitsDone.reset();
        std::cin >> N;
        i = 1;
        std::cout << "Case #" << caseNumber + 1 << ": ";
        
        if (N == 0) {
            std::cout << "INSOMNIA" << std::endl;
            continue;
        }
        
        while (!digitsDone.all()) {
            
            iN = i * N;
            
            // Check overflow
            if (iN / i != N) {
                std::cout << "INSOMNIA" << std::endl;
                break;
            }
            
            digitsDone |= digitsInNumber(i*N);
            
            if (digitsDone.all()) {
                std::cout << iN << std::endl;
            } else {
                i++;
            }
        }
    }
    
    // MAIN End
    
    return 0;
}