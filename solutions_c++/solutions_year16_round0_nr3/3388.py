//
//  main.cpp
//  C
//
//  Created by Andrey Cherevko on 4/9/16.
//  Copyright © 2016 Andrey Cherevko. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <vector>

typedef long long ll;

using namespace std;

bool prime (ll x, ll &divisor) {
    bool f = true;
    for (ll i = 2; i * i <= x; i++) {
        if (x % i == 0) {
            f = false;
            divisor = i;
        }
    }
    return f;
}

bool jamcoin (ll x) {
    bool f = true;
    if (x % 10 != 1)
        f = false;
    while (x > 0) {
        if (x % 10 > 1)
            f = false;
        x /= 10;
    }
    return f;
}

ll translateNumberToBase (ll x, ll base) {
    vector <ll> zeros;
    while (x > 0) {
        zeros.push_back(x % 10);
        x /= 10;
    }
    ll cur = 1;
    ll ans = 0;
    for (int i = 0; i < (int)zeros.size(); i++) {
        ans += zeros[i] * cur;
        cur *= base;
    }
    return ans;
}

bool check (ll x) {
    bool f = true;
    ll divisor = 0;
    for (ll i = 2; i <= 10; i++) {
        ll num = translateNumberToBase (x, i);
        if (prime (num, divisor))
            f = false;
    }
    return f;
}

void calculate (ll x) {
    cout << x << " ";
    ll divisor = 0;
    for (ll i = 2; i <= 10; i++) {
        ll num = translateNumberToBase(x, i);
        if (!prime(num, divisor)) {
            cout << divisor << " ";
        }
    }
    cout << endl;
}



int main(int argc, const char * argv[]) {
    ll t;
    cin >> t;
    ll n, j;
    cin >> n >> j;
    ll goodnum = 0;
    ll startNumber = pow (10, n - 1);
    ll finishNumber = pow (10, n);
    cout << "Case #1:" << endl;
    for (ll i = startNumber + 1; i != finishNumber; i++) {
        if (jamcoin(i))
            if (check (i)) {
                calculate (i);
                goodnum++;
                if (goodnum == j)
                    break;
            }
    }
    return 0;
}
