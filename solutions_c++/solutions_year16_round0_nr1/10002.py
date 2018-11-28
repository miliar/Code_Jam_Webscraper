//
//  main.cpp
//  CountingSheep
//
//  Created by Leo Lee on 4/9/16.
//
//

#include <iostream>

using namespace std;

uint countSheep(uint N) {
    if (N == 0) {
        return 0;
    }
    
    uint curNum = N;
    uint seenDigits = 0;
    while (curNum < INT_MAX) {
        uint w = curNum;
        while (w != 0) {
            uint digit = w % 10;
            seenDigits |= (1 << digit);
            w /= 10;
        }
        
        if (seenDigits == 0x03ff) {
            break;
        }
        curNum += N;
    }
    
    if (curNum >= INT_MAX) {
        curNum = 0;
    }
    
    return curNum;
}

int main(int argc, const char * argv[]) {

    uint numCases = 1;
    cin >> numCases;
    for (uint caseIndex = 0; caseIndex < numCases; ++caseIndex) {
        uint N = 0;
        cin >> N;
        uint lastNumber = countSheep(N);
        if (lastNumber == 0) {
            cout << "Case #" << (caseIndex + 1) << ": INSOMNIA" << endl;
        } else {
            cout << "Case #" << (caseIndex + 1) << ": " << lastNumber << endl;
        }
    }
    return 0;
}

