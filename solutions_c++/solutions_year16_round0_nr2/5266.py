#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

#include <vector>
#include <utility>
#include <set>
#include <map>
#include <queue>
#include <functional>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <bitset>
using namespace std;

template<typename T>inline string to_str(const T& v) {
    ostringstream os; os << v; return os.str();
}
template<typename T>inline T to_obj(const string& v) {
    istringstream is(v); T r; is>>r; return r;
}
template<class T>inline int cMin(T& a, T b) {return b<a ? a=b,1 : 0;}
template<class T>inline int cMax(T& a, T b) {return a<b ? a=b,1 : 0;}

#define CLR(A,v) memset(A, v, sizeof(A))
#define MP(a,b)  make_pair(a, b)
#define F0(i, n) for(int i=0; i<(n); ++i)
#define F1(i, n) for(int i=1; i<=(n); ++i)

typedef __uint128_t uint128_t;

int calc_(int n, uint128_t m) {
    int extra = 0;
    while(n > 0) {
        if (m&1) {
            --n; m >>= 1;
            continue;
        }
        --n;
        m = (~(m>>1)) & ((((uint128_t)1) << n) - 1);
        ++extra;
    }
    return extra;
}

int main(int argc, char *argv[]) {
    int T;scanf("%d", &T);
    char buf[128];
    F1(Ti, T) {
        scanf("%s", buf);
        uint128_t bit = 0;
        int n = 0;
        for(; buf[n]; ++n)
            bit = (bit << 1) | (buf[n] == '+' ? 1 : 0);
        printf("Case #%d: %d\n", Ti, calc_(n, bit));
    }
    return 0;
}
