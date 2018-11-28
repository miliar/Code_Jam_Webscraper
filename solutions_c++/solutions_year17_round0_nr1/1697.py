//
//  main.cpp
//  Oversized Pancake Flipper
//
//  Created by 王越 on 17/4/8.
//  Copyright © 2017年 王越. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int main(int argc, const char * argv[]) {
    ofstream cout("/Users/xidui/Documents/xidui/practices/gcj/Oversized Pancake Flipper/Oversized Pancake Flipper/output2.txt");
    ifstream cin("/Users/xidui/Documents/xidui/practices/gcj/Oversized Pancake Flipper/Oversized Pancake Flipper/A-large.in");
    
    int T, t = 0;
    cin >> T;
    while (t++ != T){
        string s; int k;
        cin >> s >> k;
        int count = 0;
        bool possible = true;
        for (int i = 0; i < s.length() && possible; ++i) {
            if (s[i] == '+') continue;
            count++;
            for (int j = 0; j < k; ++j) {
                if (i + j >= s.length()) {
                    possible = false;
                    break;
                }
                if (s[i + j] == '-') s[i + j] = '+';
                else s[i + j] = '-';
            }
        }
        cout << "Case #" << t << ": ";
        if (possible) cout << count << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}

