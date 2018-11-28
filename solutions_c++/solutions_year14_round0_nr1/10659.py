/* 
 * File:   main.cpp
 * Author: dan_2
 *
 * Created on April 13, 2014, 10:42 AM
 */

#include <cstdlib>
#include <string>
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

/*
 * 
 */

int getSetBitsFromRow(FILE* f, int rows, int rowans) {
    int thesebits = 0;

    for (int y = 0; y < rows; y++) {
        char row[13];
        fgets(row, 13, f);

        if (rowans == y + 1) {
            size_t pos = 0;
            string token;
            string s = row;

            while ((pos = s.find(" ")) != std::string::npos || (pos = s.find("\n")) != std::string::npos) {
                token = s.substr(0, pos);
                int8_t thisnum = strtol(token.c_str(), 0, 10);
                thesebits |= 1 << thisnum - 1;
                s.erase(0, pos + 1);
            }
        }
    }

    return thesebits;
}

// get high order bit index

int hobi(int32_t num) {
    if (!num || num == 0)
        return 0;

    int ret = 1;

    while (num >>= 1)
        ret++;

    return ret;
}

// get low order bit index

int lobi(int num) {
    if (!num || num == 0)
        return 0;

    int ret = 1;
    
    while ((num & 1) == 0) {
        ret++;
        num >>= 1;
    }
        

    return ret;
}

int main(int argc, char** argv) {
    int rows = 4;
    string rowDelim = " ";
    //    int cols = 4;

    FILE * pFile = fopen("test", "r");
    char totalTestsSTR [13];
    if (pFile == NULL) {
        perror("Error opening file");
        return 1;
    }

    fgets(totalTestsSTR, 13, pFile); // max 13 chars per line

    int32_t totalTests = strtol(totalTestsSTR, 0, 10);

//    cout << totalTests;
//    cout << " total tests\n";

    for (int x = 0; x < totalTests; x++) {
        uint32_t totalBits1 = 0;
        uint32_t totalBits2 = 0;
        int8_t cardIndex = 0;

        // Get 1st answer into int
        char ans1STR[13];
        fgets(ans1STR, 13, pFile);
        int8_t ans1 = strtol(ans1STR, 0, 10);

        totalBits1 = getSetBitsFromRow(pFile, rows, ans1);

        // Get 2nd answer into int
        char ans2STR[13];
        fgets(ans2STR, 13, pFile);
        int8_t ans2 = strtol(ans2STR, 0, 10);

        totalBits2 = getSetBitsFromRow(pFile, rows, ans2);

        uint32_t cardBitmask = totalBits1 & totalBits2;

        cout << "Case #";
        cout << x+1;
        cout << ": ";

        if (hobi(cardBitmask) != lobi(cardBitmask)) {
            cout << "Bad magician!";
        } else {
            if (hobi(cardBitmask) > 0) {
                cout << hobi(cardBitmask);
            } else {
                cout << "Volunteer cheated!";
            }
        }

        cout << "\n";
    }

    fclose(pFile);

    return 0;
}

