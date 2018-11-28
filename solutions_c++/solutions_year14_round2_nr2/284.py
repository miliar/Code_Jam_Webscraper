// INCLUDES
#include <functional>
#include <algorithm>
#include <utility>
#include <cassert>
#include <cmath>
#include <ctime>

#include <numeric>
#include <iomanip>
#include <complex>
#include <float.h>
#include <cfloat>

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <cstdio>

#include <cstring>
#include <string>

#include <iterator>
#include <vector>
#include <bitset>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>

#include <inttypes.h>
#include <ctype.h>
using namespace std;

// TYPEDEFS
typedef long long LL;
typedef long double LD;         
typedef unsigned long UL;
typedef vector < int > VI;
typedef vector < string > VS;
typedef vector < long long > VLL;
typedef vector < long double > VLD;

// DEFINES
#define FORN(index, start, end) for (int index = (int) (start); index <= (int) (end); ++ index)
#define FORDN(index, end, start) for (int index = (int) (end); index >= (int) (start); -- index)
#define _FORN(index, start, end) for (int index = (int) (start); index < (int) (end); ++ index)
#define _FORDN(index, end, start) for (int index = (int) (end); index > (int) (start); -- index)
#define SFORN(index, start, end, shift) for (int index = (int) (start); index <= (int) (end); index += shift)
#define SFORDN(index, end, start, shift) for (int index = (int) (end); index >= (int) (start); index -= shift)
#define _SFORN(index, start, end, shift) for (int index = (int) (start); index < (int) (end); index += shift)
#define _SFORDN(index, end, start, shift) for (int index = (int) (end); index > (int) (start); index -= shift)
#define FORIT(itIndex, container) for (typeof(container.begin()) itIndex = container.begin(); itIndex != container.end(); ++ itIndex)
#define FILL(box, value) memset(box, value, sizeof(box))
#define ALL(box) box.begin(), box.end()
#define RALL(box) box.rbegin(), box.rend()
#define SIZE(box) ((int) (box.size()))
#define LENGTH(box) ((int) (box.length()))
#define MP(firstItem, secondItem) make_pair(firstItem, secondItem)
#define PB(value) push_back(value)
#define TWOP(power) (1 << (power))
#define TWOLP(power) (((LL) (1)) << (power))
#define CONTAINB(mask, index) (((mask) & TWOP(index)) != 0)
#define CONTAINLB(mask, index) (((mask) & TWOLP(index)) != 0)
#define ONEBITN(value) (__builtin_popcount(value))
#define ALLBSETS(maskIndex, length) for (int maskIndex = 0; maskIndex < TWOP(length); ++ maskIndex)
#define ALLBSUBSETS(maskIndex, mask) for (int maskIndex = mask; ; maskIndex = ((maskIndex - 1) & mask))
#define CONTAINS(container, key) (container.find(key) != container.end())
#define MSG(who) cout << #who << " = " << who << endl;

// CONSTS
const LD PI = acos(-1.0);
const LD EPS = 1e-9;
const int INF = 1000000000;
const LL INFL = (LL) 1000000000 * (LL) 1000000000;
const int NULO = -1;
const string INPUT_FILE = "input.txt";
const string OUTPUT_FILE = "output.txt";

// TEMPLATES
template<class T> inline string TO_STRING(T X) { ostringstream oss; oss << X; oss.flush(); return oss.str(); }
template<class T> inline void FIX_MIN(T A, T & B) { if (A < B) B = A; }
template<class T> inline void FIX_MAX(T A, T & B) { if (A > B) B = A; }
template<class T> inline T SQR(T X) { return X * X; }

template<class T> inline T GCD(T A, T B)    {
    if (A < 0) return GCD(-A, B); 
    if (B < 0) return GCD(A, -B);
    return (B == 0) ? A : GCD(B, A % B);
}

template<class T> inline T LCM(T A, T B) {
    if (A < 0) return LCM(-A, B);
    if (B < 0) return LCM(A, -B);
    return A * (B / GCD(A, B));
}

template<class T> inline int CMPF(T X, T Y = 0, T EPS_DIST = EPS) {
  return (X <= Y + EPS_DIST) ? ((X + EPS_DIST < Y) ? -1 : 0) : +1; 
}

// INLINES
inline bool IS_UPPERCH(char C) { return C >= 'A' && C <= 'Z'; }
inline bool IS_LOWERCH(char C) { return C >= 'a' && C <= 'z'; }
inline bool IS_LETTERCH(char C) { return IS_UPPERCH(C) || IS_LOWERCH(C); }
inline bool IS_DIGITCH(char C) { return C >= '0' && C <= '9'; }
inline char TO_LOWERCH(char C) { return (IS_UPPERCH(C)) ? (C + 32) : C; }
inline char TO_UPPERCH(char C) { return (IS_LOWERCH(C)) ? (C - 32) : C; }
inline double TO_DOUBLES(string S) { double value; istringstream iss(S); iss >> value; return value; }
inline int TO_INTS(string S) { int value; istringstream iss(S); iss >> value; return value; }

// MY
int A, B, K;
LL dp [32][2][2][2];

VI toBits(int X) {
    VI bits;
    bits.clear();

    while (X) {
        bits.PB(X % 2);
        X /= 2;
    }

    return bits;
}

LL calc(int A, int B, int K) {
    VI bitsA = toBits(A), bitsB = toBits(B), bitsC = toBits(K);
    int bitsN = max(SIZE(bitsA), max(SIZE(bitsB), SIZE(bitsC)));
    bitsA.resize(bitsN, 0), bitsB.resize(bitsN, 0), bitsC.resize(bitsN, 0);
    reverse(ALL(bitsA)), reverse(ALL(bitsB)), reverse(ALL(bitsC));

    FILL(dp, 0);
    dp [0][0][0][0] = 1;

    _FORN(i, 0, bitsN)
        _FORN(lA, 0, 2)
            _FORN(lB, 0, 2)
                _FORN(lC, 0, 2)
                    if (dp [i][lA][lB][lC]) {
                        _FORN(bA, 0, 2)
                            _FORN(bB, 0, 2) {
                                bool okBitsAB = true;
                                if (bA > bitsA [i] && !lA) okBitsAB = false;
                                if (bB > bitsB [i] && !lB) okBitsAB = false;

                                if (okBitsAB) {
                                    int bC = bA & bB;

                                    bool okBitsC = true;
                                    if (bC > bitsC [i] && !lC) okBitsC = false;

                                    if (okBitsC) {
                                        int nlA = lA, nlB = lB, nlC = lC;
                                        if (!lA && bA < bitsA [i]) nlA = 1;
                                        if (!lB && bB < bitsB [i]) nlB = 1;
                                        if (!lC && bC < bitsC [i]) nlC = 1;

                                        dp [i + 1][nlA][nlB][nlC] += dp [i][lA][lB][lC];
                                    }
                                }
                            }
                    }

    return dp [bitsN][1][1][1];
}

// MAIN
int main() {
    freopen(INPUT_FILE.c_str(), "r", stdin);
    freopen(OUTPUT_FILE.c_str(), "w", stdout);  

    int nTest;
    scanf("%d\n", &nTest);

    FORN(testIndex, 1, nTest) {
        scanf("%d %d %d", &A, &B, &K);  
        printf("Case #%d: %lld\n", testIndex, calc(A, B, K));  
    }

    return 0;
}