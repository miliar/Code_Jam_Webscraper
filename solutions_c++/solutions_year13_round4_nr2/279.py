#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <utility>
#include <memory.h>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

int n;
LL p;

LL best_pos(LL k, LL m) {
    if (k == 0)
        return m;
    if (m == 0)
        return 0;
    if ((k + 1) & 1)
        return best_pos(k / 2 - 1, (m + 1) / 2);
    else
        return best_pos((k - 1) / 2, m / 2);
}

int main() {
    int tt;
    scanf("%d", &tt);
    for (int t = 1; t <= tt; ++t) {
        cin >> n >> p;

        LL cnt = LL(1) << n;
        LL L = 0, R = cnt;
        while (L + 1 < R) {
            LL M = (L + R) / 2;
            if (cnt - best_pos(M, cnt - M - 1) - 1 < p)
                L = M;
            else
                R = M;
        }

        cout << "Case #" << t << ": " << L << ' ';

        L = 0, R = cnt;
        while (L + 1 < R) {
            LL M = (L + R) / 2;
            if (best_pos(cnt - M - 1, M) < p)
                L = M;
            else
                R = M;
        }

        cout << L << '\n';
    }

    return 0;
}

