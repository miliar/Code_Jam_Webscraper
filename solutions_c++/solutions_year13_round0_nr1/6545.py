//
//  main.cpp
//  GoogleCodeJamRoundOne
//
//  Created by Matt Slater on 4/12/13.
//  Copyright (c) 2013 Matt Slater. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;


static bool checkWin(int sum) {
    if (sum == 1) {
        cout << "O won";
        return true;
    } else if (sum == 2) {
        cout << "X won";
        return true;
    }
    
    return false;
}

static void solver(int caseNum, const vector< vector<int> > &m) {
    cout<< "Case #" << caseNum << ": ";
    int sum = 1;
    bool complete = true;
    
    for (int i = 0; i < 4; i++) {
        sum = 3;
        for (int j = 0; j < 4; j++) {
            if (m[i][j] == 0) {
                complete = false;
            }
            
            sum &=m[i][j];
        }
        
        if (checkWin(sum)) return;
    }
    
    // check columns
    
    for (int i = 0; i < 4; i++) {
        sum = 3;
        for (int j = 0; j < 4; j++) {
            sum &=m[j][i];
        }
        
        if (checkWin(sum)) return;
    }
    
    //check diagonal from top left to buttom right
    int row = 0;
    sum = 3;
    for (row = 0; row < 4; row++) {
        sum &= m[row][row];
    }
    if (checkWin(sum)) return;
    
    //check other  diagonal
    sum = 3;
    for (row = 0; row < 4; row++) {
        sum &= m[row][3-row];
    }
    if (checkWin(sum)) return;
    
    if (!complete) {
        cout << "Game has not completed";
        return;
    }
    
    cout << "Draw";
}


static int convert(char a) {
    if (a == 'O') {
        return 1;
    } else if (a == 'X') {
        return 2;
    } else if (a == 'T') {
        return 3;
    }
    
    return 0;
}


int main(int argc, const char * argv[])
{
    int testNums = 0;
    cin >> testNums;
    char a;
    char b;
    char c;
    char d;
    
    for(int t = 1; t <= testNums; ++ t) {
        vector<vector<int>> matrix(4, vector<int>(4, 0));
        for (int i = 0; i < 4; i++) {
            cin >> a >> b>> c >> d;
            
            matrix[i][0] = convert(a);
            matrix[i][1] = convert(b);
            matrix[i][2] = convert(c);
            matrix[i][3] = convert(d);
        }

        solver(t, matrix);
        cout << endl;
    }
    
    return 0;
}

