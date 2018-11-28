//
//  main.cpp
//  gcj2015
//
//  Created by Даня on 12.04.15.
//  Copyright (c) 2015 mipt. All rights reserved.
//

#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
//#include "b.h"

using namespace std;
//
//int n, t;
//string s;
//
//int main() {
//    freopen("input.txt", "r", stdin);
//    freopen("output2.txt", "w", stdout);
//    cin >> t;
//    for (int k = 0; k < t; ++k) {
//        cin >> n;
//        cin >> s;
//        int curup = 0;
//        int ans = 0;
//        for (int i = 0; i < n + 1; ++i) {
//            ans += max(0, i - curup);
//            curup += max(0, i - curup) + s[i] - '0';
//        }
//        cerr << "Case #" << k + 1 << ": " << ans << "\n";
//    }
//    return 0;
//}


int t;
int d;
vector <int> a;
int pows[2000];

int getans(int x, int y) {
    if (x <= y) return 0;
    if (x % 2) {
        return getans(x/2, y) + getans((x/2) + 1, y) + 1;
    }
    return 2 * getans(x/2, y) + 1;
}

int main() {
    freopen("input.txt", "r", stdin);
    int curx = 0;
    int curpow = 1;
    for (int i = 1; i < 1100; ++i) {
        pows[i] = curx;
        if (i == curpow) {
            curpow *= 2;
            curx++;
        }
    }
    cin >> t;
    for (int k = 0; k < t; ++k) {
        cin >> d;
        a.resize(d);
        int mini = 1000;
        for (int i = 0; i < d; ++i) {
            cin >> a[i];
        }
        for (int j = 1; j <= 1000; ++j) {
            int curspec = 0;
            for (int i = 0; i < a.size(); ++i) {
                int tmp = a[i];
                if (tmp % j) {
                    curspec += tmp / j;
                } else {
                    curspec += tmp / j - 1;
                }
            }
            mini = min(mini, curspec + j);
        }
        cout << "Case #" << k + 1 << ": " << mini << "\n";
    }
}