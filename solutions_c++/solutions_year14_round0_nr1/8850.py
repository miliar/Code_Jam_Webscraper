//
//  main.cpp
//  MagicTrick
//
//  Created by Dmitry Fantastik on 4/12/14.
//  Copyright (c) 2014 funlife. All rights reserved.
//

#include <iostream>

using namespace std;

enum {
    ResultBadMagician = 0,
    ResultVolunteerCheated = -1
};

int main(int argc, const char * argv[])
{
    short sResults[100] = {};
    short sColumn[4] = {};
    short sCount;
    short sAnswer;
    short sTemp;
    short sLastRes;
    
    cin >> sCount;
    
    for (short i = 0; i < sCount; i++) {
        cin >> sAnswer;
        --sAnswer;
        for (short a = 0; a < 4; a++) {
            for (short b = 0; b < 4; b++) {
                cin >> sTemp;
                if (a == sAnswer)
                    sColumn[b] = sTemp;
            }
        }

        cin >> sAnswer;
        --sAnswer;
        short sMatch = 0;
        for (short a = 0; a < 4; a++) {
            for (short b = 0; b < 4; b++) {
                cin >> sTemp;
                if (a == sAnswer) {
                    for (short j = 0; j < 4; j++) {
                        if (sTemp == sColumn[j]) {
                            sLastRes = sTemp;
                            ++sMatch;
                        }
                    }
                }
            }
        }
        
        if (sMatch > 1)
            sLastRes = ResultBadMagician;
        else if (sMatch == 0)
            sLastRes = ResultVolunteerCheated;
        
        sResults[i] = sLastRes;
    }
    
    for (short i = 0; i < sCount; i++) {
        cout << "Case #" << i + 1 << ": ";
        short r = sResults[i];
        if (r == ResultBadMagician)
            cout << "Bad magician!";
        else if (r == ResultVolunteerCheated)
            cout << "Volunteer cheated!";
        else
            cout << r;
        cout << endl;
    }
    
    return 0;
}

