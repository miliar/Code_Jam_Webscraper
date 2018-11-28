//
//  main.cpp
//  A
//
//  Created by Misha Babenko on 3/28/15.
//  Copyright (c) 2015 Misha Babenko. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <ctime>
#include <cmath>
#include <cstdlib>
#include <map>
#include <set>
#include <cassert>
#include <unordered_set>

using namespace std;

typedef long long ll;

void Solve(string s) {
    int minus = 0;
    int plus = 0;
    for (int i = 0; i < (int)s.length(); ++i) {
        if (s[i] == '-') {
            minus = min(minus, plus + 1);
            plus = min(minus + 1, plus + 3);
        } else {
            plus = min(plus, minus + 1);
            minus = min(plus + 1, minus + 3);
        }
    }
    cout << plus;
}

int main() {
    int t;
    scanf ("%d", &t);
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        string s;
        cin >> s;
        Solve(s);
        cout << endl;
    }
    return 0;
}