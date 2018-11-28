//
//  main.cpp
//  GCJ2013
//
//  Created by 菅原 皓 on 13/04/13.
//  Copyright (c) 2013年 Ko Sugawara. All rights reserved.
//

//
//  This code is powered by peroxyacyl's GCJ Template for Xcode.
//  https://github.com/peroxyacyl/gcj-xcode-template
//


#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
using namespace std;



const static string kProblemSet = "A-large";

int main(int argc, const char * argv[]) {
    ifstream ifs( kProblemSet + ".in" );
    ofstream ofs( kProblemSet + ".out" );
	int T = 0;
    
	ifs >> T;
    char matrix[4][4] = {NULL};
    string str, ret;
    
    for (int testCase = 0; testCase < T; testCase++) {
        ret = "Draw";
        //assign values to matrix
        for (int i = 0; i < 4; i++) {
            ifs >> str;
            sscanf(str.data(), "%c%c%c%c", &matrix[i][0], &matrix[i][1], &matrix[i][2], &matrix[i][3]);
            //check rows
            if ((matrix[i][0] == 'X' || matrix[i][0] == 'T') &&
                (matrix[i][1] == 'X' || matrix[i][1] == 'T') &&
                (matrix[i][2] == 'X' || matrix[i][2] == 'T') &&
                (matrix[i][3] == 'X' || matrix[i][3] == 'T')) {
                ret = "X won";
                for (int n = 0; n < 3-i; n++) {
                    ifs >> str;
                }
                break;
            } else if ((matrix[i][0] == 'O' || matrix[i][0] == 'T') &&
                       (matrix[i][1] == 'O' || matrix[i][1] == 'T') &&
                       (matrix[i][2] == 'O' || matrix[i][2] == 'T') &&
                       (matrix[i][3] == 'O' || matrix[i][3] == 'T')) {
                ret = "O won";
                for (int n = 0; n < 3-i; n++) {
                    ifs >> str;
                }
                break;
            }
        }
        //check columns
        if (!ret.compare("Draw")) {
            for (int j = 0; j < 4; j++) {
                if ((matrix[0][j] == 'X' || matrix[0][j] == 'T') &&
                    (matrix[1][j] == 'X' || matrix[1][j] == 'T') &&
                    (matrix[2][j] == 'X' || matrix[2][j] == 'T') &&
                    (matrix[3][j] == 'X' || matrix[3][j] == 'T')) {
                    ret = "X won";
                    break;
                } else if ((matrix[0][j] == 'O' || matrix[0][j] == 'T') &&
                           (matrix[1][j] == 'O' || matrix[1][j] == 'T') &&
                           (matrix[2][j] == 'O' || matrix[2][j] == 'T') &&
                           (matrix[3][j] == 'O' || matrix[3][j] == 'T')) {
                    ret = "O won";
                    break;
                }
            }
        }
        //check diagonals
        if (!ret.compare("Draw")) {
            if ((matrix[0][0] == 'X' || matrix[0][0] == 'T') &&
                (matrix[1][1] == 'X' || matrix[1][1] == 'T') &&
                (matrix[2][2] == 'X' || matrix[2][2] == 'T') &&
                (matrix[3][3] == 'X' || matrix[3][3] == 'T')) {
                ret = "X won";
            } else if ((matrix[0][3] == 'X' || matrix[0][3] == 'T') &&
                       (matrix[1][2] == 'X' || matrix[1][2] == 'T') &&
                       (matrix[2][1] == 'X' || matrix[2][1] == 'T') &&
                       (matrix[3][0] == 'X' || matrix[3][0] == 'T')) {
                ret = "X won";
            } else if ((matrix[0][0] == 'O' || matrix[0][0] == 'T') &&
                       (matrix[1][1] == 'O' || matrix[1][1] == 'T') &&
                       (matrix[2][2] == 'O' || matrix[2][2] == 'T') &&
                       (matrix[3][3] == 'O' || matrix[3][3] == 'T')) {
                ret = "O won";
            } else if ((matrix[0][3] == 'O' || matrix[0][3] == 'T') &&
                       (matrix[1][2] == 'O' || matrix[1][2] == 'T') &&
                       (matrix[2][1] == 'O' || matrix[2][1] == 'T') &&
                       (matrix[3][0] == 'O' || matrix[3][0] == 'T')) {
                ret = "O won";
            }
        }
        //check completed
        if (!ret.compare("Draw")) {
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    if (matrix[i][j] == '.') {
                        ret = "Game has not completed";
                        //out from loop
                        i = 3;
                        j = 3;
                    }
                }
            }
        }
        
        cout << "Case #" << testCase+1 << ": " << ret << endl;
        ofs << "Case #" << testCase+1 << ": " << ret << endl;
    }
    
	return 0;
}
