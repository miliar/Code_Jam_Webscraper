#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int seen = 0;

void set(int i) {
    seen |= (1 << i);
}

void set_all(int n) {
    while(n > 0) {
        set(n % 10);
        n /= 10;
    }
}

int main() {
    int t;
    cin >> t;
    for (int kase = 1; kase <= t; ++kase) {
        int n;
        cin >> n;
        if(n == 0) {
            printf("Case #%d: INSOMNIA\n", kase);
        } else {
            seen = 0;
            int m = 0;
            while(seen != 1023) {
                ++m;
                set_all(n*m);
            }
            printf("Case #%d: %d\n", kase, n*m);
        }
    }
    return 0;
}