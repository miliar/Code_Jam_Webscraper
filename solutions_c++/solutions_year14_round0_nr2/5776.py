/*
 * @author: zhenpeng.fang
 * @nickname: dumpling
 */
#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
#include <time.h>
#include <stdlib.h>
#include <stack>
#include <queue>
using namespace std;

#define mp make_pair

//%llu
typedef unsigned long long uint64;
typedef long long int64;
typedef pair<int, int> pair2;

const double eps = 1e-8;
int T;
double C, F, X;

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        double ans = 0, c = 0, s = 2;
        scanf("%lf%lf%lf", &C, &F, &X);
        double r = X - c;
        bool buy = true;
        while (fabs(r) > eps) {
            if (c + eps > C) {
                if (r * F > s * C + eps) {
                    s += F;
                    c -= C;
                    r += C;
                } else
                    buy = false;
            }
            if (buy && C < r + c + eps) {
                ans += (C - c) / s;
                r -= (C - c);
                c = C;
            } else {
                ans += r / s;
                c += r;
                r = 0;
            }
        }
        printf("Case #%d: %.6lf\n", t, ans);
    }
    return 0;
}