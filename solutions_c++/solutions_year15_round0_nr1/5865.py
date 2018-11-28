//
//  Standing Ovation
//  Created by McKrisch on 11.04.15
//

#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <set>
#include <vector>
#include <iostream>
#include <list>

using namespace std;

#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep1(i,m) for(int i=1;i<=(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)

typedef unsigned long long ll;

//#define TEST
//#define SMALL

//#define COUT

#ifdef TEST
const char *kIn  = "A-test.in";
#else
#ifdef SMALL
const char *kIn  = "A-small.in";
const char *kOut = "A-small.out";
#else
const char *kIn  = "A-large.in";
const char *kOut = "A-large.out";
#endif
#endif

inline int readInt() {
    int num, c;
    while ((c = getchar_unlocked()) < '-');
    num = c - '0';
    while ((c = getchar_unlocked()) >= '0') {
        num = (num<<3) + (num<<1) + (c-'0');
    }
    return num;
}

const int kMax = 1004;
char A[kMax];

void workCase() {
    int M = readInt();
    scanf("%s", A);
    ll ret = 0;
    ll cnt = A[0]-'0';
    rep1 (i, M) {
        int v = A[i]-'0';
        if (cnt < i) {
            ll a = ll(i) - cnt;
            ret += a;
            cnt += a;
        }
        cnt += v;
    }
    printf("%lld\n", ret);
}

int main(int argc, const char * argv[]) {
    if (!freopen(kIn, "rt", stdin)) {
        return 1;
    }
#if !defined(COUT) && !defined(TEST)
    if (!freopen(kOut, "wt", stdout)) {
        return 2;
    }
#endif
    int T = readInt();
    rep (i, T) {
        cout << "Case #" << i+1 << ": ";
        workCase();
    }
    return 0;
}
