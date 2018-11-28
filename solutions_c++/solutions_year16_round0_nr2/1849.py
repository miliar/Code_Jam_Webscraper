//
//  main.cpp
//  CodeJam2016Qualification-B
//
//  Created by Michael Walker on 4/8/16.
//  Copyright © 2016 Michael Walker. All rights reserved.
//

#include <iostream>
#include <fstream>

const int I = 100;
char array[I];
char tempArray[I];
char tempChar;
int numChar;
int numFlips;
int tempIndex;
int lastNegIndex;


bool checkArray() {
    for (int i = 0; i < numChar; ++i) {
        if (array[i] == '-') {
            return false;
        }
    }
    return true;
}

bool isAllNegative() {
    for (int i = 0; i < numChar; ++i) {
        if (array[i] == '+') {
            return false;
        }
    }
    return true;
}

void flipArraySegment(int startIndex, int endIndex) {
    for (int i = endIndex; i >= startIndex; --i) {
        tempIndex = endIndex - i;
        tempArray[tempIndex] = array[i];
        if (tempArray[tempIndex] == '-') {
            tempArray[tempIndex] = '+';
        } else {
            tempArray[tempIndex] = '-';
        }
    }
    for (int i = startIndex; i <= endIndex; ++i) {
        array[i] = tempArray[i];
    }
    numFlips++;
}

int main(int argc, const char * argv[]) {
    freopen("/Users/Michael/Desktop/B-large.in", "r", stdin);
    std::ofstream out("/Users/Michael/Desktop/output");
    
    
    int T;
   
    
    scanf("%i", &T);
    scanf("%c", &tempChar);
    
    
    for (int i = 0; i < T; ++i) {
        numChar = 0;
        numFlips = 0;
        
        for (int ii = 0; ii <= I; ++ii) {
            if (scanf("%c", &tempChar) == EOF || tempChar == '\n') {
                numChar = ii;
                break;
            } else {
                array[ii] = tempChar;
            }
        }
        
        while (!checkArray()) {
            if (isAllNegative()) {
                numFlips++;
                break;
            }
            tempIndex = numChar - 1;
            while (array[tempIndex] == '+') {
                tempIndex--;
            }
            lastNegIndex = tempIndex;
            if (lastNegIndex == 0) {
                numFlips++;
                break;
            }
            tempIndex = 0;
            while (array[tempIndex] == '+') {
                tempIndex++;
            }
            if (tempIndex > 0) {
                flipArraySegment(0, tempIndex - 1);
            }
            flipArraySegment(0, lastNegIndex);
        }
        
        out << "Case #" << i + 1 << ": " << numFlips << "\n";
    }
    
    out.close();
    return 0;
}