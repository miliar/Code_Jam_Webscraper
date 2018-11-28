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

void Solve(int k, int c, int s) {
    for (int i = 0; i < k; ++i) {
        cout << i + 1;
        if (i != k - 1)
            cout << " ";
    }
}

int main() {
    int t;
    scanf ("%d", &t);
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        int k, c, s;
        cin >> k >> c >> s;
        Solve(k, c, s);
        cout << endl;
    }
    return 0;
}