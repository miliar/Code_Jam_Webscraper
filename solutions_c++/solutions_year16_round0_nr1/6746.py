/******************************************************************************/
/*!
\file   main.cpp
\author Lim Yee Chen, yeechen.lim
\par    email: ycprog\@gmail.com
\date   April 9, 2016
\brief  
        Copyright (C) 2016 Lim Yee Chen. Reproduction
        or disclosure of this file or its contents without the prior written
        consent of Lim Yee Chen is prohibited.
 */
/******************************************************************************/

#include <iostream>
#include <string>

#define RESULT_INFINITE -1

// Return false if all digit is registered
bool checkAllDigit(char (&checkList)[10], unsigned numberToInsert) {
    while(numberToInsert) {
        ++checkList[numberToInsert % 10];
        numberToInsert /= 10;
    }

    // Check if all digit is registered
    for(int i = 0; i < 10; ++i) {
        if(!checkList[i])
            return true;
    }
    return false;
}

unsigned getLastNumber(const unsigned N) {
    // Trivial
    if(!N) {
        return RESULT_INFINITE;
    }

    unsigned currentNumber = N, previousNumber = 0, i = 0;
    char checkList[10] = {0};

    while( checkAllDigit(checkList, currentNumber) ) {
        ++i;
        currentNumber += N;
    }

    return currentNumber;
}

int main() {

    int T = 0;
    unsigned N = 0;

    std::cin >> T;

    for(int i = 1; i <= T; ++i) {
        std::cin >> N;

        unsigned lastNumber = getLastNumber(N);

        std::cout << "Case #" << i <<": ";
        if(lastNumber != RESULT_INFINITE) {
            std::cout << lastNumber << std::endl;
        }
        else {
            std::cout<< "INSOMNIA" << std::endl;
        }
    }
    
    return 0;
}
