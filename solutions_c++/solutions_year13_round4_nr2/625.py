#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <math.h>
#include <numeric>
#include <iostream>
#include <utility>
#include <stack>
using namespace std;



#define TWO(i) (1LL<<(i))

typedef long long i64;

i64  ans_y, ans_z;

i64  N, P;

i64  get_best(i64 a) {
    if(a == 0) return 0;
    i64  rank = 1;
    i64  cc = TWO(N-1);
    i64  tot = cc + 1;
    while(tot <= a) {
        rank = (rank<<1) | 1;
        cc >>= 1;
        tot += cc;
    }
    return rank;
}

i64  get_bad(int idx) {
    if(idx == 0) return 0;
    i64  cc = 2;
    i64  tot = 3;
    i64  rank = TWO(N-1);
    while(tot <= idx) {
        cc <<= 1;
        tot += cc;
        rank = (rank >> 1) | rank;
    }
    return rank;
}

void calc() {
    scanf("%lld%lld", &N, &P);
    --P;
    i64 lo=0, hi=(1LL<<N), mi;
    while(lo+1 < hi) {
        mi = (lo + hi) >> 1;
        if(get_bad(mi) <= P)
            lo = mi;
        else
            hi = mi;
    }
    ans_y = lo;
    lo = 0;
    hi = 1LL<<N;
    while(lo+1 < hi) {
        mi = (lo + hi) >> 1;
        if(get_best(mi) <= P)
            lo = mi;
        else
            hi = mi;
    }
    ans_z = lo;
}

int main(int argc, char* argv[]) {
    int  T;
    scanf("%d", &T);
    for(int it=1; it<=T; ++it) {
        calc();
        printf("Case #%d: %lld %lld\n", it, ans_y, ans_z);
    }
    return 0;
}

