#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cstdio>
#include <queue>
#include <vector>
#include <ctime>
#include <cmath>

#define mid ((l+r)>>1)
using namespace std;
int T, tag;
bool use[15];

int calc(int n) {
    int k = 1;
    while (n / 10) {
        k *= 10;
        n /= 10;
    }
    return k * 10;
}

void check(int n) {
    while (n) {
        if (!use[n % 10]) {
            tag++;
            use[n % 10] = true;
        }
        n /= 10;
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> T;
    int n;
    for (int i = 1; i <= T; ++i) {
        cin >> n;
        tag = 0;
        memset(use, 0, sizeof(use));
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", i);
            continue;
        }
        for (int temp = n; temp <= 2000000000; temp += n) {
            check(temp);
            if (tag == 10) {
                printf("Case #%d: %d\n", i, temp);
                break;
            }
        }
        if (tag != 10)
            printf("Case #%d: INSOMNIA\n", i);
    }
    return 0;
}