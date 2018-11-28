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
//#include "b.h"

using namespace std;

int n, t;
string s;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output2.txt", "w", stdout);
    cin >> t;
    for (int k = 0; k < t; ++k) {
        cin >> n;
        cin >> s;
        int curup = 0;
        int ans = 0;
        for (int i = 0; i < n + 1; ++i) {
            ans += max(0, i - curup);
            curup += max(0, i - curup) + s[i] - '0';
        }
        cerr << "Case #" << k + 1 << ": " << ans << "\n";
    }
    return 0;
}
