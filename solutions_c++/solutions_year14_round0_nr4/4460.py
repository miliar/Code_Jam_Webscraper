/**
 * jerrym
 * D.cpp
 */

#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <algorithm>
#include <bitset>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef long long int lli;
typedef pair<int, int> pii;

int gInt () {
    int i;
    scanf("%d", &i);
    return i;
}

lli gLong () {
    lli i;
    scanf("%lld", &i);
    return i;
}

double gDouble () {
    double i;
    scanf("%lf", &i);
    return i;
}

void quit () {
    fflush(stdout);
    exit(0);
}

int n;
double naomi[1005], ken[1005];

int calcBest (double * n, double * k, int sz, bool deceit) {
    int score = 0;
    set<double> kset;
    for (int i = 0; i < sz; ++i) {
        kset.insert(k[i]);
    }
    for (int i = 0; i < sz; ++i) {
        set<double>::iterator it = kset.upper_bound(n[i]);
        if (it == kset.end()) {
            ++score;
            kset.erase(kset.begin());
        } else if (deceit && n[i] > *kset.begin()) {
            ++score;
            kset.erase(kset.begin());
        } else {
            kset.erase(it);
        }
    }
    return score;
}

int tryTrick (int trick) {
    return calcBest(naomi + trick, ken, n - trick, true);
}

void solve (int nC) {
    n = gInt();
    for (int i = 0; i < n; ++i) naomi[i] = gDouble();
    for (int i = 0; i < n; ++i) ken[i] = gDouble();
    sort(naomi, naomi + n);
    sort(ken, ken + n);
    int opt = 0;
    for (int i = 0; i <= n; ++i) {
//        printf("%.3lf %.3lf\n", naomi[i], ken[i]);
        opt = max(opt, tryTrick(i));
    }
    printf("Case #%d: %d %d\n", nC + 1, opt, calcBest(naomi, ken, n, false));
}

int main (int argc, char ** argv) {
    int nC = gInt();
    for (int i = 0; i < nC; ++i) {
        solve(i);
    }
    quit();
}
