//
//  main.cpp
//  Coin Jam
//
//  Created by Rugen Heidbuchel on 09/04/16.
//  Copyright © 2016 Rugen Heidbuchel. All rights reserved.
//

#include <iostream>
#include <bitset>
#include <cmath>

size_t T, J, N, count;
std::bitset<32> bits;
size_t divisors[9];

size_t valueOfBitsInBase(size_t base) {
    size_t value = 1;
    size_t factor = base;
    for (size_t i = 1; i < N-1; i++) {
        value += bits[i] * factor;
        factor *= base;
    }
    value += factor;
    return value;
}

size_t getDivisor(size_t n) {
    
    if (n % 2 == 0) {
        return 2;
    }
    
    if (n % 3 == 0) {
        return 3;
    }
    
    size_t p = 5;
    
    while (p <= (size_t)std::sqrt(n)) {
        
        if (n % p == 0) {
            return p;
        }
        
        if (n % (p + 2) == 0) {
            return p + 2;
        }
        
        p += 6;
    }
    
    return 0;
}

void printJamcoin() {
    
    for (size_t i = N-1; i > 0; i--) {
        std::cout << bits[i];
    }
    std::cout << "1";
    
    for (auto divisor: divisors) {
        std::cout << " " << divisor;
    }
    
    std::cout << std::endl;
}

int main(int argc, const char * argv[]) {
    
    #ifdef USE_INPUT_FILE
    freopen("input.txt", "r", stdin);
    #endif
    
    // MAIN Begin
    
    std::cin >> T;
    for (size_t caseNumber = 0; caseNumber < T; caseNumber++) {
        
        std::cin >> N >> J;
        count = 0;
        std::cout << "Case #" << caseNumber + 1 << ":" << std::endl;
        
        bits.reset();
        bits[0] = true;
        bits[N-1] = true;
        
        while (count < J) {
            
            bool isJamcoin = true;
            
            for (size_t base = 2; base <= 10; base++) {
                
                size_t value = valueOfBitsInBase(base);
                size_t divisor = getDivisor(value);
                
                if (!divisor) {
                    isJamcoin = false;
                    break;
                }
                
                divisors[base - 2] = divisor;
            }
            
            if (isJamcoin) {
                printJamcoin();
                count++;
            }
            
            bits = bits.to_ullong() + 2;
        }
    }
    
    // MAIN End
    
    return 0;
}