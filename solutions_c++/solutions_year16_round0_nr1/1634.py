#include <map>
#include <set>
#include <stack>
#include <cmath>
#include <queue>
#include <vector>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

const int max_n = 11, inf = 1111111111;

int sum, t, n, used[max_n];

void proc(long long x) {
    if (x == 0) {
        used[0] = 1;
    }
    while (x) {
        if (used[x % 10] == 0) {
            used[x % 10] = 1;
            ++sum;
        }
        x /= 10;
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        scanf("%d", &n);
        memset(used, 0, sizeof(used));
        long long x = n;
        sum = 0;
        printf("Case #%d: ", i);
        for (int j = 0; ; ++j) {
            if (n == 0) {
                break;
            }
            proc(x);
            if (sum == 10) {
                printf("%lld\n", x);
                break;
            }
            x += n;
        }
        if (sum != 10) {
            printf("INSOMNIA\n");
        }
    }
    return 0;
}
