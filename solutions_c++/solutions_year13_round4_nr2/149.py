#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>
#include <deque>
#include <string>
#include <string.h>
#include <queue>
#include <stdlib.h>
#include <set>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);

    int _T;
    scanf("%d\n", &_T);

    for (int __test = 1; __test <= _T; ++__test) {
        ll n, p;
        cin >> n >> p;

        ll l = 0, r = (1LL << n);
        while (l < r) {
            ll c = (l + r) >> 1;

            ll rest = c;
            ll ans = 0;
            ll cadd = (1LL << (n - 1));
            while (rest > 0) {
                ans += cadd;
                cadd >>= 1;
                rest = (rest - 1) / 2;
            }

            if (ans < p) {
                l = c + 1;
            } else {
                r = c;
            }
        }
        ll ans1 = l - 1;

        l = 0, r = (1LL << n) - 1;
        while (l < r) {
            ll c = (l + r + 1) >> 1;

            ll rest = (1LL << n) - 1 - c;
            ll ans = 0;
            ll cadd = (1LL << (n - 1));
            while (rest > 0) {
                ans += cadd;
                cadd >>= 1;
                rest = (rest - 1) / 2;
            }

            if ((1LL << n) - ans - 1 < p) {
                l = c;
            } else {
                r = c - 1;
            }
        }
        ll ans2 = l;

        printf("Case #%d: ", __test);
        cout << ans1 << " " << ans2 << endl;
    }


    return 0;
}

