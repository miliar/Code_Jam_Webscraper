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


char buf[128];

int get_mask(int N) {
    int ret = 0;
    for(; N>0; N/=10) {
        ret |= (1<<(N%10));
    } return ret;
}

const char* calc(int N) {
    if (N == 0) return "INSOMNIA";
    if (N == 1) return "10";
    int v = N;
    int mask = 0;
    for(; mask != (1<<10) -1; v += N) {
        mask |= get_mask(v);
        if (mask == (1<<10) - 1) break;
    }
    sprintf(buf, "%d", v);
    return buf;
}

int main(int argc, char *argv[]) {
    int T; scanf("%d", &T);
    F1(Ti, T) {
        int N;
        scanf("%d", &N);
        printf("Case #%d: %s\n", Ti, calc(N));
    }
    return 0;
}
