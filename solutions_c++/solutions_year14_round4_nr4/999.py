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
typedef pair < int, int > PII;
typedef pair < string, string > PSS;
typedef vector < pair < int, int > > VPII; 
typedef vector < pair < string, string > > VPSS;
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
template<class T> inline int CMPF(T X, T Y = 0, T EPS_DIST = EPS) { return (X <= Y + EPS_DIST) ? ((X + EPS_DIST < Y) ? -1 : 0) : +1; }
template<class T> inline T GCD(T A, T B) { return (A < 0) ? GCD(-A, B) : ((B < 0) ? GCD(A, -B) : ((0 == B) ? A : GCD(B, A % B))); }
template<class T> inline T LCM(T A, T B) { return (A < 0) ? LCM(-A, B) : ((B < 0) ? LCM(A, -B) : (A * (B / GCD(A, B)))); }
template<class T> inline string TO_STRING(T X) { ostringstream oss; oss << X; oss.flush(); return oss.str(); }
template<class T> inline void FIX_MIN(T A, T & B) { if (A < B) B = A; }
template<class T> inline void FIX_MAX(T A, T & B) { if (A > B) B = A; }
template<class T> inline T SQR(T X) { return X * X; }

// INLINES
inline bool IS_UPPERCH(char C) { return C >= 'A' && C <= 'Z'; }
inline bool IS_LOWERCH(char C) { return C >= 'a' && C <= 'z'; }
inline bool IS_LETTERCH(char C) { return IS_UPPERCH(C) || IS_LOWERCH(C); }
inline bool IS_DIGITCH(char C) { return C >= '0' && C <= '9'; }
inline char TO_LOWERCH(char C) { return (IS_UPPERCH(C)) ? (C + 32) : C; }
inline char TO_UPPERCH(char C) { return (IS_LOWERCH(C)) ? (C - 32) : C; }
inline int TO_INTS(string S) { int value; istringstream iss(S); iss >> value; return value; }
inline double TO_DOUBLES(string S) { double value; istringstream iss(S); iss >> value; return value; }

// MY
int Nw, Ns;
vector< string > As;
vector< int > Ws;
int tree [100 + 10][26 + 3];
int result, resultf;

int calcv() {
    int rlv = 0;

    _FORN(i, 0, Ns) {
        bool ok = false;
        _FORN(j, 0, Nw)
            if (Ws [j] == i) {
                ok = true;
                break;
            }

        if (!ok) continue;

        FILL(tree, -1);
        int kv = 0;

        _FORN(j, 0, Nw)
            if (Ws [j] == i) {
                int cv = 0;

                _FORN(t, 0, LENGTH(As [j])) {
                    if (tree [cv][(int) (As [j][t] - 'A')] < 0) {
                        ++ kv;
                        tree [cv][(int) (As [j][t] - 'A')] = kv;
                    }

                    cv = tree [cv][(int) (As [j][t] - 'A')];
                }
            }

        rlv += (kv + 1);
    }

    return rlv;
}

void calc(int pos) {
    if (pos == Nw) {
        int rv = calcv();
        
        if (rv > result) {
            result = rv;
            resultf = 0;
        }

        if (rv == result) ++ resultf;

        return;
    }

    _FORN(i, 0, Ns) {
        Ws [pos] = i;
        calc (pos + 1);
        Ws [pos] = -1;
    }
}

// MAIN
int main() {
    freopen(INPUT_FILE.c_str(), "r", stdin);
    freopen(OUTPUT_FILE.c_str(), "w", stdout);  

    // CODE AREA =>
    int T;
    scanf("%d\n", &T);

    FORN(testId, 1, T) {
        scanf("%d %d\n", &Nw, &Ns);

        As.resize(Nw);
        Ws.resize(Nw, -1);

        _FORN(i, 0, Nw) {
            getline(cin, As [i]);
        }

        result = resultf = 0;

        calc(0);

        printf("Case #%d: %d %d\n", testId, result, resultf);
    }
    // CODE AREA <=

    return 0;
}