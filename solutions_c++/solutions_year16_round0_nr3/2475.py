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

ll prime (ll x) {
    if (x == 1)
        return 1;
    for (ll i = 2; i * i <= x; ++i)
        if (x % i == 0)
            return i;
    return -1;
}

void Solve(int n, int j) {
    
}

int main() {
    cout << "Case #1:" << endl;
    int values = 0;
    long long x = (1LL << (ll)15) + 1;
    while (true) {
        string s;
        ll temp = x;
        while (temp > 0) {
            s = char('0' + temp % 2) + s;
            temp /= 2;
        }
        
        bool ok = true;
        vector<ll> ans;
        for (int base = 2; base <= 10; ++base) {
            ll cur = 0;
            ll mult_base = 1;
            for (int i = (int)s.length() - 1; i >= 0; --i) {
                cur += (s[i] - '0') * mult_base;
                mult_base *= (ll)base;
            }
            ll is_prime = prime(cur);
            if (is_prime == -1) {
                ok = false;
                break;
            } else {
                ans.push_back(is_prime);
            }
        }
        
        if (ok) {
            values++;
            cout << s;
            for (int i = 0; i < 9; ++i)
                cout << " " << ans[i] ;
            cout << endl;
        }
        
        x += 2;
        if (values == 50) {
            break;
        }
    }
    return 0;
}