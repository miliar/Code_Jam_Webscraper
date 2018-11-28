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

// #include <inttypes.h>
// #include <ctype.h>
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
#define FORTESTS(testId) int __T; scanf("%d\n", &__T); _FORN(testId, 0, __T)
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
#define endl '\n'

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

// ... 1
const string ominos_1_1 [4][4][1] = {
    {{"#..."},
     {"...."},
     {"...."},
     {"...."}},

    {{"...."},
     {"...."},
     {"...."},
     {"...."}}, 
     
    {{"...."},
     {"...."},
     {"...."},
     {"...."}}, 
     
    {{"...."},
     {"...."},
     {"...."},
     {"...."}}   
};

// ... 2
const string ominos_2_1 [4][4][1] = {
    {{"##.."},
     {"...."},
     {"...."},
     {"...."}},

    {{"#..."},
     {"#..."},
     {"...."},
     {"...."}},

    {{"...."},
     {"...."},
     {"...."},
     {"...."}}, 
     
    {{"...."},
     {"...."},
     {"...."},
     {"...."}}   
};

// ... 3
const string ominos_3_1 [4][4][1] = {
    {{"###."},
     {"...."},
     {"...."},
     {"...."}},

    {{"#..."},
     {"#..."},
     {"#..."},
     {"...."}},

    {{"...."},
     {"...."},
     {"...."},
     {"...."}}, 
     
    {{"...."},
     {"...."},
     {"...."},
     {"...."}}   
};

const string ominos_3_2 [4][4][1] = {
    {{"##.."},
     {".#.."},
     {"...."},
     {"...."}},

    {{".#.."},
     {"##.."},
     {"...."},
     {"...."}},

    {{"#..."},
     {"##.."},
     {"...."},
     {"...."}},

    {{"##.."},
     {"#..."},
     {"...."},
     {"...."}}    
};

// ... 4
const string ominos_4_1 [4][4][1] = {
    {{"####"},
     {"...."},
     {"...."},
     {"...."}},

    {{"#..."},
     {"#..."},
     {"#..."},
     {"#..."}},

    {{"...."},
     {"...."},
     {"...."},
     {"...."}}, 
     
    {{"...."},
     {"...."},
     {"...."},
     {"...."}}   
};

const string ominos_4_2 [4][4][1] = {
    {{"##.."},
     {"##.."},
     {"...."},
     {"...."}},

    {{"...."},
     {"...."},
     {"...."},
     {"...."}}, 

    {{"...."},
     {"...."},
     {"...."},
     {"...."}}, 
     
    {{"...."},
     {"...."},
     {"...."},
     {"...."}}   
};

const string ominos_4_3 [4][4][1] = {
    {{"##.."},
     {"#..."},
     {"#..."},
     {"...."}},

    {{"#..."},
     {"###."},
     {"...."},
     {"...."}},

    {{"##.."},
     {".#.."},
     {".#.."},
     {"...."}},

    {{"###."},
     {"#..."},
     {"...."},
     {"...."}}
};

const string ominos_4_4 [4][4][1] = {
    {{"#..."},
     {"##.."},
     {"#..."},
     {"...."}},

    {{"###."},
     {".#.."},
     {"...."},
     {"...."}},

    {{".#.."},
     {"##.."},
     {".#.."},
     {"...."}},

    {{".#.."},
     {"###."},
     {"...."},
     {"...."}}
};

const string ominos_4_5 [4][4][1] = {
    {{"#..."},
     {"##.."},
     {".#.."},
     {"...."}},

    {{".##."},
     {"##.."},
     {"...."},
     {"...."}},

    {{"##.."},
     {".##."},
     {"...."},
     {"...."}},

    {{".#.."},
     {"##.."},
     {"#..."},
     {"...."}}
};

// MY
string resultName;
bool resultOk;
bool canFill;
int X, R, C;

int Ko;
string ominos [9][4][4][1];
bool board [4][4];

inline bool applyOmino(int os, int oi, int pX, int pY, bool ov) {
    char omino_part = '#';
    bool hasOmp = false;

    // check
    _FORN(x, 0, 4)
        _FORN(y, 0, 4)
            if (omino_part == ominos [os][oi][x][0][y]) {
                hasOmp = true;
                if (pX + x >= R || pY + y >= C) return false;
                if (board [pX + x][pY + y] != (!ov)) return false;
            }

    if (!hasOmp) return false;

    // apply
    _FORN(x, 0, 4)
        _FORN(y, 0, 4)
            if (omino_part == ominos [os][oi][x][0][y]) {
                board [pX + x][pY + y] = ov;
            }

    return true;
}

void check(int si, bool used) {
    if (canFill) return;

    // Check board
    bool filled = true;
    _FORN(bi, 0, R) {
        _FORN(bj, 0, C)
            if (!board [bi][bj]) {
                filled = false;
                break;
            }

        if (!filled) break;
    }

    if (filled && used) {
        canFill = true;
        return;
    }

    // Itearte through the ominos & board
    _FORN(os, 0, Ko) _FORN(oi, 0, 4) _FORN(i, 0, R) _FORN(j, 0, C) {
        bool ok = applyOmino(os, oi, i, j, true);
        if (ok) {
            check(si, (used || si == os));
            bool okRev = applyOmino(os, oi, i, j, false);
            assert(okRev);
        }
    }
}

// MAIN
int main() {
    // Using cout/printf together can't guarantee the right order
    // ios_base::sync_with_stdio(0);

    freopen(INPUT_FILE.c_str(), "r", stdin);
    freopen(OUTPUT_FILE.c_str(), "w", stdout);

    // CODE AREA =>
    FORTESTS(testId) {
        scanf("%d %d %d", &X, &R, &C);

        resultName = "RICHARD";
        resultOk = false;
        canFill = false;

        if (1 == X) {
            Ko = 1;
            _FORN(i, 0, 4) _FORN(j, 0, 4) _FORN(q, 0, 1) ominos [0][i][j][q] = ominos_1_1 [i][j][q]; 

            canFill = false;
            FILL(board, false);
            if (!resultOk) check(0, false);
            resultOk |= !canFill;
        }

        if (2 == X) {
            Ko = 1;
            _FORN(i, 0, 4) _FORN(j, 0, 4) _FORN(q, 0, 1) ominos [0][i][j][q] = ominos_2_1 [i][j][q]; 
            
            canFill = false;
            FILL(board, false);
            if (!resultOk) check(0, false);
            resultOk |= !canFill;
        }

        if (3 == X) {
            Ko = 2;
            _FORN(i, 0, 4) _FORN(j, 0, 4) _FORN(q, 0, 1) ominos [0][i][j][q] = ominos_3_1 [i][j][q]; 
            _FORN(i, 0, 4) _FORN(j, 0, 4) _FORN(q, 0, 1) ominos [1][i][j][q] = ominos_3_2 [i][j][q]; 

            canFill = false;
            FILL(board, false);
            if (!resultOk) check(0, false);
            resultOk |= !canFill;

            canFill = false;
            FILL(board, false);
            if (!resultOk) check(1, false);
            resultOk |= !canFill;
        }

        if (4 == X) {
            Ko = 5;
            _FORN(i, 0, 4) _FORN(j, 0, 4) _FORN(q, 0, 1) ominos [0][i][j][q] = ominos_4_1 [i][j][q]; 
            _FORN(i, 0, 4) _FORN(j, 0, 4) _FORN(q, 0, 1) ominos [1][i][j][q] = ominos_4_2 [i][j][q]; 
            _FORN(i, 0, 4) _FORN(j, 0, 4) _FORN(q, 0, 1) ominos [2][i][j][q] = ominos_4_3 [i][j][q]; 
            _FORN(i, 0, 4) _FORN(j, 0, 4) _FORN(q, 0, 1) ominos [3][i][j][q] = ominos_4_4 [i][j][q]; 
            _FORN(i, 0, 4) _FORN(j, 0, 4) _FORN(q, 0, 1) ominos [4][i][j][q] = ominos_4_5 [i][j][q]; 

            canFill = false;
            FILL(board, false);
            if (!resultOk) check(0, false);
            resultOk |= !canFill;

            canFill = false;
            FILL(board, false);
            if (!resultOk) check(1, false);
            resultOk |= !canFill;

            canFill = false;
            FILL(board, false);
            if (!resultOk) check(2, false);
            resultOk |= !canFill;

            canFill = false;
            FILL(board, false);
            if (!resultOk) check(3, false);
            resultOk |= !canFill;

            canFill = false;
            FILL(board, false);
            if (!resultOk) check(4, false);
            resultOk |= !canFill;
        }

        if (!resultOk) resultName = "GABRIEL";

        printf("Case #%d: %s", testId + 1, resultName.c_str());
        if (testId + 1 < __T) printf("\n");
    }
    // CODE AREA <=

    return 0;
}