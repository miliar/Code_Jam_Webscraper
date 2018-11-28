//
//  GCJ2015QR1.cpp
//  playground
//
//  Created by Adam Chang on 2015/4/11.
//  Copyright (c) 2015年 Adam Chang. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <cmath>
#include <set>
#include <stack>
#include <cmath>

using namespace std;

string biao = "111011111011011011001011111001101000011011000010";
int main(){
    int caseCnt = 0;
    cin >> caseCnt;
    for (int ci = 1; ci <= caseCnt; ci++) {
        int x,r,c;
        cin >> x >> r >> c;
        if (x == 1) {
            cout << "Case #" << ci << ": " << "GABRIEL" << endl;
        }else{
            if (biao[(r-1)*12+(c-1)*3+x-2] == '1') {
                cout << "Case #" << ci << ": " << "RICHARD" << endl;
            }else{
                cout << "Case #" << ci << ": " << "GABRIEL" << endl;
            }
        }
        
    }
    return 0;
}

/*
int main(){
    int caseCnt = 0;
    cin >> caseCnt;
    for (int ci = 1; ci <= caseCnt; ci++) {
        int n = 0;
        cin >> n;
        string shy;
        cin >> shy;
        int res = 0;
        int sum = 0;
        for (int i = 0;i < shy.size(); i++) {
            int now = shy[i] - '0';
            if (sum < i) {
                res += i-sum;
                sum = i;
            }
            sum += now;
        }
        cout << "Case #" << ci << ": " << res << endl;
    }
    return 0;
}*/

