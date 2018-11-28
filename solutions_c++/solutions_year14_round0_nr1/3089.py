//
//  main.cpp
//  CodeJam
//
//  Created by Dan on 12/4/14.
//  Copyright (c) 2014年 Dan. All rights reserved.
//

#include <iostream>

using namespace std;

static string BAD_MAGICIAN = "Bad magician!\n";
static string VOLUNTEER_CHEATED = "Volunteer cheated!\n";

int main(int argc, const char * argv[])
{
    freopen("/Users/danmac/Documents/Works/Projects/CodeJam/CodeJam/in.txt", "r", stdin);
    freopen("/Users/danmac/Documents/Works/Projects/CodeJam/CodeJam/out.txt", "w", stdout);

    int numOfTestCase = 0;
    cin >> numOfTestCase;
    
    for (int i=0; i<numOfTestCase; i++) {
        int tmpNum, matchedCount = 0;
        int appearRow, magicNumber = 0;
        int rowNumbers[4];
        int secondRowNumbers[4];
        
        cin >> appearRow;
        for (int j=0; j<4; j++) {
            if (appearRow == j+1)
                cin >> rowNumbers[0] >> rowNumbers[1] >> rowNumbers[2] >> rowNumbers[3];
            else
                cin >> tmpNum >> tmpNum >> tmpNum >> tmpNum;
        }
        
        //cout << "AppearRow: " << appearRow << " Row Numbers: " << rowNumbers[0] << ' ' << rowNumbers[1] << ' ' << rowNumbers[2] << ' ' << rowNumbers[3] << '\n';
        
        cin >> appearRow;
        for (int j=0; j<4; j++) {
            if (appearRow == j+1)
                cin >> secondRowNumbers[0] >> secondRowNumbers[1] >> secondRowNumbers[2] >> secondRowNumbers[3];
            else
                    cin >> tmpNum >> tmpNum >> tmpNum >> tmpNum;
        }
        //cout << "AppearRow: " << appearRow << " Second Row Numbers: " << secondRowNumbers[0] << ' ' << secondRowNumbers[1] << ' ' << secondRowNumbers[2] << ' ' << secondRowNumbers[3] << '\n';
        
        for (int j=0; j<4; j++) {
            for (int k=0; k<4; k++) {
                if (rowNumbers[j] == secondRowNumbers[k]) {
                    magicNumber = rowNumbers[j];
                    matchedCount++;
                }
            }
        }
        
        cout << "Case #" << (i+1) << ": ";
        
        if (magicNumber == 0)
            cout << VOLUNTEER_CHEATED;
        else if (matchedCount > 1)
            cout << BAD_MAGICIAN;
        else
            cout << magicNumber << '\n';
    }
    
    return 0;
}

