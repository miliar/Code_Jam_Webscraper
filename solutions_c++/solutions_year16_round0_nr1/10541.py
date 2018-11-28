//
//  main.cpp
//  Counting Sheep
//
//  Created by Luc van den Ackerveken on 09/04/16.
//  Copyright © 2016 Luc van den Ackerveken. All rights reserved.
//

#include <iostream>
#include <array>

int main(int argc, const char * argv[]) {
    unsigned long t, n, mn, multiplier = 0;
    std::cin >> t;
    for(int i = 1; i <= t; ++i){
        bool done = false;
        std::array<bool, 10> digits = {false, false, false, false, false, false, false, false, false, false };
        std::array<bool, 10> check = {true, true, true, true, true, true, true, true, true, true };
        std::cin >> n;
        mn = n;
        while(!done && n != 0){
            for(unsigned long digit = mn; digit > 0; digit /= 10){
                digits[digit%10] = true;
            }
            if(digits == check){
                for(int j = 0; j < digits.size(); j++){
                    digits[j] = false;
                }
                multiplier = 0;
                done = true;
            } else {
                mn = n * ++multiplier;
            }
        }
        if(mn != 0){
            std::cout << "Case #" << i << ": " << mn << std::endl;
        } else {
            std::cout << "Case #" << i << ": INSOMNIA" << std::endl;
        }
    }
    return 0;
}
