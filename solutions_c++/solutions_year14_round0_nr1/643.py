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
#define FORN(i, st, en) for(int i = (int) (st); i <= (int) (en); ++ i)
#define FORDN(i, en, st) for(int i = (int) (en); i >= (int) (st); -- i)
#define FORN_(i, st, en) for(int i = (int) (st); i <= (int) (en); i += 2)
#define FORDN_(i, en, st) for(int i = (int) (en); i >= (int) (st); i -= 2)
#define _FORN(i, st, en) for(int i = (int) (st); i < (int) (en); ++ i)
#define _FORDN(i, en, st) for(int i = (int) (en); i > (int) (st); -- i)
#define _FORN_(i, st, en) for(int i = (int) (st); i < (int) (en); i += 2)
#define _FORDN_(i, en, st) for(int i = (int) (en); i > (int) (st); i -= 2)
#define FILL(a, w) memset(a, w, sizeof(a))
#define ALL(A) A.begin(), A.end()
#define SIZE(X) ((int) (X.size()))
#define LENGTH(X) ((int) (X.length()))
#define MP(X, Y) make_pair(X, Y)
#define TWOP(X) (1<<(X))
#define TWOLP(X) (((LL)(1))<<(X))
#define CONTAINB(MASK, X) (((MASK) & TWOP(X)) != 0)
#define CONTAINLB(MASK, X) (((MASK) & TWOLP(X)) != 0)
#define MSG(X) cout << #X << " = " << X << endl;

// CONSTS
const LD PI = acos(-1.0);
const LD EPS = 1e-7;
const int INF = 1000000000;
const LL INFL = (LL) 1000000000 * (LL) 1000000000;
const string INPUT_FILE = "inputA.txt";
const string OUTPUT_FILE = "outputA.txt";

template<class T> inline T gcd(T A, T B)	{
    if (A < 0) return gcd(-A, B); 
    if (B < 0) return gcd(A, -B);
    return (B == 0) ? A : gcd(B, A % B);
}

template<class T> inline T lcm(T A, T B) {
    if (A < 0) return lcm(-A, B);
    if (B < 0) return lcm(A, -B);
    return A * (B / gcd(A, B));
}

// MY

// MAIN
int main() {
    freopen(INPUT_FILE.c_str(), "r", stdin);
    freopen(OUTPUT_FILE.c_str(), "w", stdout);   
    int T;
    scanf("%d", &T);

    _FORN(test, 0, T) {
        int rowA, rowB;
        set<int> rowSetA, rowSetB, rowSetC;

        scanf("%d", &rowA);
        FORN(i, 1, 4) {
            FORN(j, 1, 4) {
                int X;
                scanf("%d", &X);
                if (rowA == i) rowSetA.insert(X);
            }
        }

        scanf("%d", &rowB);
        FORN(i, 1, 4) {
            FORN(j, 1, 4) {
                int X;
                scanf("%d", &X);
                if (rowB == i) rowSetB.insert(X);
            }
        }

        set_intersection(rowSetA.begin(), rowSetA.end(), rowSetB.begin(), rowSetB.end(), inserter(rowSetC,rowSetC.begin()));
        printf("Case #%d: ", test + 1);
        if (0 == rowSetC.size()) printf("Volunteer cheated!\n"); else
        if (1 == rowSetC.size()) printf("%d\n", *rowSetC.begin()); else
            printf("Bad magician!\n");
    }

    return 0;
}