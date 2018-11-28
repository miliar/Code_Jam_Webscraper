#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cassert>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <queue>

using namespace std;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back

#define epr(...) fprintf(stderr, __VA_ARGS__)
const int maxn = -1;
const int inf = 1e9;

double c, f, x;

double solve(int n) {
    double t = 0;
    double speed = 2;
    for (int i = 0; i < n; i++) {
        t += c / speed;
        speed += f;
    }
    t += x / speed;
    return t;
}

int main(){
#ifdef DEBUG
    freopen("in", "r", stdin);
     freopen("out", "w", stdout);
#endif
    int t, m1, m2;
    double r1, r2;
    scanf("%d", &t);
    for (int tt = 0; tt < t; tt++) {
        scanf("%lf%lf%lf\n", &c, &f, &x);
        int l = 0;
        int r = x;
        while (r - l > 10) {
            m1 = (l + l + r) / 3;
            m2 = (l + r + r) / 3;
            r1 = solve(m1);
            r2 = solve(m2);
            if (r1 < r2)
                r = m2;
            else
                l = m1;
        }
        double best = solve(l);
        for (int i = l; i <= r; i++)
            best = min(best, solve(i));
        printf("Case #%d: %.8lf\n", tt + 1, best);
    }



    return 0;
}
