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


int64_t get(int v, int b) {
    int64_t r = 0;
    int64_t z = 1;
    for(; v>0; v>>=1) {
        r += (v&1) * z;
        z *= b;
    } return r;
}

int Print(int v, int b) {
    int64_t N = get(v, b);
    // printf(" %d[%d]", (int)N, b);
    if(N % 2 == 0) return 2;
    for(int64_t i=3; i*i<=N; i+=2)
        if (N%i == 0) return i;
    return -1;
}

int Print(int v) {
    // char buf[32]; int n = 0;
    // for(int i=v; i>0; i>>=1) buf[n++] = (i&1) + '0';
    // for(int i=n-1; i>=0; --i) printf("%c", buf[i]);
    int A[12];
    for(int b=2; b<=10; ++b) {
        A[b] = Print(v, b);
        if (A[b] < 0) {
            // printf(">>>>>>>\n");
            return 0;
        }
    }
    // printf(">>>>>>>\n");
    {char buf[32]; int n = 0;
    for(int i=v; i>0; i>>=1) buf[n++] = (i&1) + '0';
    for(int i=n-1; i>=0; --i) printf("%c", buf[i]);
    }
    for(int b=2; b<=10; ++b) {
        printf(" %d", A[b]);
    }
    printf("\n");
    return 1;
}

void calc(int N, int J) {
    // printf("N[%d] J[%d]\n", N, J);
    int bitEnd = 1<<(N-2);
    int highBit = 1<<(N-1);
    F0(bit, bitEnd) {
        int v = highBit | (bit<<1) | 1;
        J -= Print(v);
        if (J == 0) break;
    }
}

int main(int argc, char *argv[]) {
    int T;scanf("%d", &T);
    F1(Ti, T) {
        int N, J;
        scanf("%d%d", &N, &J);
        printf("Case #%d:\n", Ti);
        calc(N, J);
    }
    return 0;
}
