#include <iostream>
#include <sstream>

#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <string>

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>

#include <algorithm>
#include <numeric>

#define foreach(i, x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)
#define sqr(x) ((x) * (x))
#define len(x) ((int64) (x).size())
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define pbk pop_back
#define mp make_pair
#define fs first
#define sc second
#define endl '\n'
#ifdef CUTEBMAING
#include "cutedebug.h"
#else
#define debug(x) ({})
#endif

using namespace std;

typedef long long int64;
typedef unsigned long long lint64;
typedef long double ld;

const int64 inf = ((1 << 30) - 1);
const int64 linf = ((1ll << 62) - 1);
const int64 logmax = 10;
const int64 cmax = 1 << logmax;

int64 n, p;

inline int64 guaranteed(int64 x){
    int64 cnt = x;
    int64 mask = 0;
    for (int64 i = n - 1; i >= 0; i--)
        if (cnt > 0)
            mask = mask * 2 + 1, cnt = (cnt - 1) / 2;
        else
            mask = mask * 2;
    return mask;
}

inline int64 nonguaranteed(int64 x){
    int64 cnt = (1ll << n) - x - 1;
    int64 mask = 0;
    for (int64 i = n - 1; i >= 0; i--)
        if (cnt > 0)
            mask = mask * 2, cnt = (cnt - 1) / 2;
        else
            mask = mask * 2 + 1;
    return mask;
}

void run(){
    assert(scanf("%lld%lld", &n, &p));
    int64 l = -1, r = (1ll << n);
    while (r - l > 1){
        int64 m = (l + r) / 2;
        if (guaranteed(m) < p)
            l = m;
        else
            r = m;
    }
    printf("%lld ", l);
    l = -1, r = (1ll << n);
    while (r - l > 1){
        int64 m = (l + r) / 2;
        if (nonguaranteed(m) < p)
            l = m;
        else
            r = m;
    }
    printf("%lld\n", l);
}

int main(){
    #if defined CUTEBMAING && !defined STRESS
    assert(freopen("input.txt", "r", stdin));
    assert(freopen("output.txt", "w", stdout));
    #endif
    int t; assert(scanf("%d", &t));
    for (int i = 0; i < t; i++){
        printf("Case #%d: ", i + 1);
        run();
    }
    return 0;
}
