/******************************************************************************/
/*!
\file   main.cpp
\author Lim Yee Chen, yeechen.lim
\par    email: ycprog\@gmail.com
\date   April 9, 2016
\brief  
        Copyright (C) 2016 Lim Yee Chen. Reproduction or disclosure of
        this file or its contents without the prior written consent of Lim
        Yee Chen is prohibited.
 */
/******************************************************************************/

#include <iostream>
#include <string>

#define PANCAKE_HAPPY '+'
#define PANCAKE_SAD '-'

void flipPancake(std::string &pancakes, size_t numToFlip) {
    auto end = pancakes.begin();
    std::advance(end,numToFlip);
    for(auto it = pancakes.begin(); it != end; ++it) {
        *it = (*it == PANCAKE_HAPPY) ? PANCAKE_SAD : PANCAKE_HAPPY;
    }
    std::reverse(pancakes.begin(),end);
}

int makePancakeHappy(std::string pancakes) {
    // Flip prata
    int numOfFlip = 0; 

    while(!pancakes.empty()) {
        // Ioslate the happy at the bottom
        while(pancakes.back() == PANCAKE_HAPPY) {
            pancakes.pop_back();

            if(pancakes.empty()) {
                return numOfFlip;
            }
        }

        if(pancakes.front() == PANCAKE_HAPPY) {
            // Find all pancake with happy
            int numOfHappy = 1;
            for(unsigned i = 1; i < pancakes.length(); ++i) {
                if(pancakes[i] == PANCAKE_HAPPY)
                    ++numOfHappy;
                else
                    break;
            }

            flipPancake(pancakes,numOfHappy);
            ++numOfFlip;
        }
        
        flipPancake(pancakes,pancakes.length());
        ++numOfFlip;
        
    }

    return numOfFlip;
}

int main() {

    int T = 0;
    std::string S;

    std::cin >> T;

    for(int i = 1; i <= T; ++i) {
        std::cin >> S;

        std::cout << "Case #" << i <<": " << makePancakeHappy(S) << std::endl;
    }

    return 0;
}
