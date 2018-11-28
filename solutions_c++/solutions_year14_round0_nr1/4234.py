//
//  main.cpp
//  CodeJam - Magic Trick
//
//  Created by Ryan on 4/12/14.
//  Copyright (c) 2014 Ryan. All rights reserved.
//

#include <iostream>

using namespace std;

int numMatches(int *, int *, int &);


int main(int argc, const char * argv[])
{
    
    //string strNumTests;
    //cin >> strNumTests;
    //int numTests = atoi(strNumTest.c_str());
    int numTests;
    cin >> numTests;
    
    int board[16];
    int firstChosenRow[4];
    int secondChosenRow[4];
    int inputRow;
    int matches;
    int answer;
    int caseCounter = 1;
    
    for (int i = 0; i < numTests; i++) {
        
        cin >> inputRow;
        for (int i2 = 0; i2 < 16; i2++) {
            cin >> board[i2];
        }
        for (int i3 = 0; i3 < 4; i3++) {
            firstChosenRow[i3] = board[i3 + (inputRow-1)*4];
        }
        
        cin >> inputRow;
        for (int i4 = 0; i4 < 16; i4++) {
            cin >> board[i4];
        }
        for (int i5 = 0; i5 < 4; i5++) {
            secondChosenRow[i5] = board[i5 + (inputRow-1)*4];
        }
        
        matches = numMatches(firstChosenRow, secondChosenRow, answer);
        if (matches == 1) {
            cout << "Case #" << caseCounter << ": " << answer << "\n";
        }
        else if (matches == 0) {
            cout << "Case #" << caseCounter << ": Volunteer cheated!\n";
        }
        else {
            cout << "Case #" << caseCounter << ": Bad magician!\n";
        }
        caseCounter++;
    }
    
    return 0;
}

int numMatches(int *firstChosenRow, int *secondChosenRow, int &answer) {
    int numMatches = 0;
    
    for (int i = 0; i < 4; i++) {
        for (int i2 = 0; i2 < 4; i2++) {
            if (firstChosenRow[i] == secondChosenRow[i2]) {
                numMatches++;
                answer = firstChosenRow[i];
            }
        }
    }
    
    return numMatches;
}


