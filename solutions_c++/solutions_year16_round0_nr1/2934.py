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

void Solve(ll n) {
    if (n == 0) {
        cout << "INSOMNIA";
        return;
    }
    vector<bool> used(10, false);
    for (ll i = 1; i <= 1e12; ++i) {
        ll cur = n * i;
        while (cur > 0) {
            used[cur % 10] = true;
            cur /= 10;
        }
        bool done = true;
        for (int i = 0; i < 10; ++i)
            if (!used[i]) {
                done = false;
                break;
            }
        if (done) {
            cout << n * i;
            return;
        }
    }
}

int main() {
    int t;
    scanf ("%d", &t);
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        ll n;
        cin >> n;
        Solve(n);
        cout << endl;
    }
    return 0;
}