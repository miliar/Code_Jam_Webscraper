//
//  main.cpp
//  Magician
//
//  Created by Eddie Kaiger on 4/12/14.
//  Copyright (c) 2014 Eddie Kaiger. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[])
{
    int numberOfCases;
    cin >> numberOfCases;
    int grid[4][4];
    int possibilities1[4];
    int possibilites2[4];
    int results[100];
    
    for (int i = 0; i < numberOfCases; i++) {
        int rowNumber;
        cin >> rowNumber;
        rowNumber--;
        
        for (int j = 0; j < 4; j++) {
            cin >> grid[j][0] >> grid[j][1] >> grid[j][2] >> grid[j][3];
        }
        
        
        for (int j = 0; j < 4; j++) {
            possibilities1[j] = grid[rowNumber][j];
        }
        
        cin >> rowNumber;
        rowNumber--;
        for (int j = 0; j < 4; j++) {
            cin >> grid[j][0] >> grid[j][1] >> grid[j][2] >> grid[j][3];
        }
        
        
        for (int j = 0; j < 4; j++) {
            possibilites2[j] = grid[rowNumber][j];
        }
        
        int cardNumber = 0;
        int found = 0;
        for (int j = 0; j < 4; j++) {
            for (int k = 0; k < 4; k++) {
                if (possibilities1[j] == possibilites2[k]) {
                    found++;
                    cardNumber = possibilities1[j];
                }
            }
        }
        
        
        if (found == 0) {
            results[i] = 0;
        }
        if(found == 1) {
            results[i] = cardNumber;
        }
        if (found > 1) {
            results[i] = -1;
        }
    }

    for (int k = 0; k < 100; k++) {
        cout << "Case #" << k + 1 << ": ";
        if(results[k] > 0) {
            cout << results[k];
        } 
        if (results[k] == 0)
        {
            cout << "Volunteer cheated!";
        } 
        if (results[k] == -1)
        {
            cout << "Bad magician!";
        }
        cout << endl;
    }
    
    return 0;
}