//
//  main.cpp
//  HDOJ
//
//  Created by user on 13-4-10.
//  Copyright (c) 2013年 user. All rights reserved.
//

#include <iostream>
#include <string>
#include <map>
#include <cmath>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>

using namespace std;



char judge(char a, char b, char c, char d)
{
    if (a == 'T' && b==c && c==d) {
        return b;
    }
    else if (b == 'T' && a==c && c==d) {
        return a;
    }
    else if (c == 'T' && a==b && b==d) {
        return a;
    }
    else if (d == 'T' && a==b && b==c) {
        return a;
    }
    else if (a==b && b==c && c==d)
    {
        return a;
    }
    else
    {
        return 'D';
    }
}

int main()
{
    int t;
    char sq[5][5];
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        int tx, ty;
        char result = 'D';
        bool full = true;
        sq[0][0] = sq[0][1] = sq[0][2] = sq[0][3] = sq[0][4] = '1';
        sq[1][0] = sq[2][0] = sq[3][0] = sq[4][0] = '1';
        for (int m = 1; m <= 4; m++) {
            for (int n = 1; n <=4; n++) {
                cin >> sq[m][n];
                if (sq[m][n] == 'T') {
                    tx = m;
                    ty = n;
                }
                if (sq[m][n] == '.') {
                    full = false;
                    sq[m][0] = '0';
                    sq[0][n] = '0';
                    if (m == n) {
                        sq[0][0] = '0';
                    }
                }
            }
        }
        for (int j = 1; j <= 4; j++) {
            if (sq[0][j] == '1') {
                result = judge(sq[1][j], sq[2][j], sq[3][j], sq[4][j]);
                if (result == 'O' || result == 'X') {
                    break;
                }
            }
            
            if (sq[j][0] == '1') {
                result = judge(sq[j][1], sq[j][2], sq[j][3], sq[j][4]);
                if (result == 'O' || result == 'X') {
                    break;
                }
            }
        }
        if (result == 'D') {
            result = judge(sq[1][1], sq[2][2], sq[3][3], sq[4][4]);
        }
        
        if (result == 'D' && sq[4][1]!='.' && sq[3][2]!='.' && sq[2][3]!='.' && sq[1][4]!='.') {
            result = judge(sq[4][1], sq[3][2], sq[2][3], sq[1][4]);
        }
        
        if (result == 'O') {
            cout << "Case #" << i << ": O won" << endl;
        }
        else if (result == 'X')
        {
            cout << "Case #" << i << ": X won" << endl;
        }
        else if (result == 'D' && full == true)
        {
            cout << "Case #" << i << ": Draw" << endl;
        }
        else
        {
            cout << "Case #" << i << ": Game has not completed" << endl;
        }
        getchar();// get a line after each test case
    }
    
    return 0;
}

