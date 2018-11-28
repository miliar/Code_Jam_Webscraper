//
//  main.cpp
//  round4
//
//  Created by wangdongfang on 15/4/11.
//  Copyright (c) 2015年 _. All rights reserved.
//

#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::string;

string map [65][65][65];


void create() {
    map[2][1][1] = "r";
    map[2][1][2] = "g";
    map[2][1][3] = "r";
    map[2][1][4] = "g";
    map[2][2][1] = "g";
    map[2][2][2] = "g";
    map[2][2][3] = "g";
    map[2][2][4] = "g";
    map[2][3][3] = "r";
    map[2][3][4] = "g";
    map[2][4][4] = "g";
    
    map[3][1][1] = "r";
    map[3][1][2] = "r";
    map[3][1][3] = "r";
    map[3][1][4] = "r";
    map[3][2][1] = "r";
    map[3][2][2] = "r";
    map[3][2][3] = "g";
    map[3][2][4] = "r";
    map[3][3][3] = "g";
    map[3][3][4] = "g";
    map[3][4][4] = "r";
    
    map[4][1][1] = "r";
    map[4][1][2] = "r";
    map[4][1][3] = "r";
    map[4][1][4] = "r";
    map[4][2][1] = "r";
    map[4][2][2] = "r";
    map[4][2][3] = "r";
    map[4][2][4] = "r";
    map[4][3][3] = "r";
    map[4][3][4] = "g";
    map[4][4][4] = "g";

    
}


int main() {

    int T;
 //   freopen("/Users/wangdongfang/Myprogram/codejam2015/round4/round4/round4/smalldata", "r",stdin);
    cin >> T;
    int X;
    int R;
    int C;
    create();
    for (int i = 0; i < T; i++) {
        cin >> X >> R >> C;
        if (X == 1) {
            cout << "Case #" << i+1 << ": " << "GABRIEL" << endl;
            continue;
        }
        if ( R > C) {
            int tmp = R;
            R = C;
            C = tmp;
            
        }
        if (map[X][R][C] == "g") {
            cout << "Case #" << i+1 << ": " << "GABRIEL" << endl;
        }
        else if (map[X][R][C] == "r") {
            cout << "Case #" << i+1 << ": " << "RICHARD" << endl;
            
        }
       
    }
    return 0;
}
