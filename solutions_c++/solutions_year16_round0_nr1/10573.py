/*
 * Tests.cpp
 *
 *  Created on: 26 Oct 2014
 *      Author: tomy
 */

#include <cstdio>
#include <cmath>

#include <string>
#include <bitset>
#include <iostream>
#include <sstream>
#include <inttypes.h>


const int TOTAL_DIGITS = 10;

bool hasSeenAll(bool* digits) {
    for (int i = 0; i < TOTAL_DIGITS; ++i) {
        if (!digits[i]) return false;
    }
    return true;
}

uint64_t countingSheeps(uint32_t N) {
    bool digits[TOTAL_DIGITS] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    uint64_t lastNamed = 0;

    do {
        lastNamed += N;

        uint64_t remainingDigits = lastNamed;

        while (remainingDigits > 0) {
            digits[remainingDigits % TOTAL_DIGITS] = 1;
            remainingDigits /= TOTAL_DIGITS;
        }

    } while (!hasSeenAll(digits));

    return lastNamed;
}

void countingSheeps (uint32_t t, uint32_t N) {
    std::cout << "Case #" << t << ": " ;

    if (N == 0) {
        std::cout << "INSOMNIA";
    } else {
        std::cout << countingSheeps(N);
    }

    std::cout << std::endl;
}

int main(int argc, char **argv) {
    uint32_t N;
    uint32_t T;

    std::cin >> T;

    for (uint32_t t = 1; t <= T; ++t) {
        std::cin >> N;
        countingSheeps(t, N);
    }
}



