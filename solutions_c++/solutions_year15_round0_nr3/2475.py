#include <cassert>
#include <cstdio>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;
#define For(i,x) for (int i=0; i<(int)(x); i++)
// #define PI (2 * acos(0))

char s[20000];

enum {
    PONE = 0, // +1
    PI, // +i
    PJ, // +j
    PK, // +k

    NONE, // -1
    NI, // -i
    NJ, // -j
    NK, // -k
};

bool isneg(int a) {
    switch (a) {
    case NONE:
    case NI:
    case NJ:
    case NK:
        return true;
    }
    return false;
}

int inverse(int a) {
    switch (a) {
    case PONE: return NONE;
    case PI: return NI;
    case PJ: return NJ;
    case PK: return NK;
    case NONE: return PONE;
    case NI: return PI;
    case NJ: return PJ;
    case NK: return PK;
    default:
        assert(false);
    }
    return a;
}

int mul(int a, int b) { // a * b
    const int N = 5;
    int none = -100;
    int mat[N][N] = {
        { none, PONE,   PI,   PJ,   PK },
        { PONE, PONE,   PI,   PJ,   PK },
        {   PI,   PI, NONE,   PK,   NJ },
        {   PJ,   PJ,   NK, NONE,   PI },
        {   PK,   PK,   PJ,   NI, NONE },
    };

    int inv = 0;
    if (isneg(a)) {
        inv++;
        a = inverse(a);
    }
    if (isneg(b)) {
        inv++;
        b = inverse(b);
    }

    int row = 0;
    for (int i = 1; i < N; i++) {
        if (a == mat[i][0]) {
            row = i;
            break;
        }
    }
    int col = 0;
    for (int i = 1; i < N; i++) {
        if (b == mat[0][i]) {
            col = i;
            break;
        }
    }

    int ret = mat[row][col];
    for (int i = 0; i < inv; i++) {
        ret = inverse(ret);
    }
    return ret;
}

int toi(char c) {
    switch (c) {
    case 'i': return PI;
    case 'j': return PJ;
    case 'k': return PK;
    }
    assert(false);
    return 0;
}

bool calc(int L, int X, char* s) {
    assert(L == strlen(s));
    vector<int> v;
    for (int i = 0; i < X; i++) {
        for (int j = 0; s[j] != '\0'; j++) {
            v.push_back(toi(s[j]));
        }
    }

    if (v.size() < 3) return false;

    const int n = v.size();
    vector<int> precalc(n);
    precalc[n-1] = v[n-1];
    for (int i = n-2; i >= 0; i--) {
        precalc[i] = mul(v[i], precalc[i+1]);
    }
    
    int p = PONE;
    for (int i = 0; i < v.size(); i++) {
        p = mul(p, v[i]);
        if (p == PI) {
            int q = PONE;
            for (int j = i+1; j < v.size(); j++) {
                q = mul(q, v[j]);
                if (q == PJ) {
#if 0
                    int r = PONE;
                    for (int k = j+1; k < v.size(); k++) {
                        r = mul(r, v[k]);
                    }
                    if (r == PK) {
//                        printf("found: i:%d j:%d\n", i, j);
                        return true;
                    }
#else
                    if (j+1 < v.size() && PK == precalc[j+1]) {
                        return true;
                    }
#endif                    
                }
            }
        }
    }
    return false;
}

int main() {
    int ncases;
    scanf("%d", &ncases);
    For(cc, ncases) {
        int L, X;
        scanf("%d %d", &L, &X);
        scanf("%s", s);
        printf("Case #%d: %s\n", cc+1, calc(L, X, s) ? "YES" : "NO");
    }
}
