//
//  main.cpp
//  acm
//
//  Created by JackieZhu on 14-4-12.
//  Copyright (c) 2014年 JackieZhu. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <stack>
#include <sstream>
#include <cmath>
#include <queue>
#include <memory.h>
using namespace std;

int main()
{
    freopen("/Users/JackieZhu/Documents/work/Job hunting/prectise/acm/A-small-attempt2.in", "r", stdin);
    //freopen("/Users/JackieZhu/Documents/work/Job hunting/prectise/acm/output.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas=1; cas<=T; cas++) {
        int n, m;
        cin >> n;
        int state1 = 0;
        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++) {
                cin >> m;
                if (i+1 == n) {
                    state1 |= 1<<m;
                }
            }
        }
        cin >> n;
        int state2 = 0;
        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++) {
                cin >> m;
                if (i+1 == n) {
                    state2 |= 1<<m;
                }
            }
        }
        int final = state1 & state2;
        int cnt = 0, y = 0, res = 0;
        while (final) {
            if(final&1) {
                cnt ++;
                res = y;
            }
            y ++;
            final >>= 1;
        }
        cout << "Case #" << cas << ": ";
        if (cnt == 1) {
            cout << res << endl;
        } else if(cnt > 1) {
            cout << "Bad magician!" << endl;
        } else {
            cout << "Volunteer cheated!" << endl;
        }
    }
    return 0;
}