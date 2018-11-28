//
//  main.cpp
//  B
//
//  Created by IwfWcf on 13-6-1.
//  Copyright (c) 2013年 IwfWcf. All rights reserved.
//

#include <iostream>
#include <stdio.h>

using namespace std;

typedef long long LL;

int n;

inline LL worst(LL k)
{
    LL ret = 0;
    k--;
    int now = n - 1;
    while (k) {
        ret |= 1LL << now;
        now--;
        k = (k - 1) >> 1;
    }
    return ret;
}

inline LL best(LL k)
{
    LL ret = (1LL << n) - 1;
    k = (1LL << n) - k;
    int now = n - 1;
    while (k) {
        ret ^= 1LL << now;
        now--;
        k = (k - 1) >> 1;
    }
    return ret;
}

int main(int argc, const char * argv[])
{
    freopen("/Users/IwfWcf/Desktop/B/input.txt", "r", stdin);
	freopen("/Users/IwfWcf/Desktop/B/output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases++) {
        LL p;
        cin >> n >> p;
        LL l = 1, r = 1LL << n;
        while (l <= r) {
            LL mid = (l + r) >> 1;
            if (worst(mid) >= p) r = mid - 1;
            else l = mid + 1;
        }
        cout << "Case #" << cases << ": " << r - 1 << " ";
        l = 1, r = 1LL << n;
        while (l <= r) {
            LL mid = (l + r) >> 1;
            if (best(mid) >= p) r = mid - 1;
            else l = mid + 1;
        }
        cout << r - 1 << "\n";
    }
    return 0;
}