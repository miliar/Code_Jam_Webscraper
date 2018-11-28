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

// typedefs
typedef long long LL;
typedef long double LD;
typedef vector < int > VI;
typedef vector < string > VS;
typedef vector < long long > VLL;
typedef vector < long double > VLD;
typedef vector < vector < int > > VVI;
typedef vector < vector < string > > VVS;
typedef vector < vector < long long > > VVLL;
typedef vector < vector < long double > > VVLD;

// defines
#define FOREACH(it, v, type) for( type::iterator it = v.begin(); it != v.end() ; ++ it )
#define FORN(i, st, en) for( int i = (int)(st); i <= (int)(en); ++ i )
#define FORDN(i, en, st) for( int i = (int)(en); i >= (int)(st); -- i )
#define ZERO(a, w) memset(a, w, sizeof(a))
#define ALL(A) A.begin(), A.end()
#define SIZE(X) ((int) (X.size()))
#define LENGTH(X) ((int) (X.length()))
#define MP(X, Y) make_pair(X, Y)
#define TWOP(X) (1<<(X))
#define TWOLP(X) (((LL)(1))<<(X))
#define CONTAINB(MASK, X) (((MASK) & TWOP(X)) != 0)
#define CONTAINLB(MASK, X) (((MASK) & TWOLP(X)) != 0)
#define MSG(X) cout << #X << " = " << X << endl;

// templates
template<class T> inline void checkMin(T A, T & B) { if(A < B) B = A; }
template<class T> inline void checkMax(T A, T & B) { if(B > A) B = A; }
template<class T> inline T sqr(T X) { return X * X; }

template<class T> inline T GCD(T A,T B)	{
    if(A < 0) return GCD(-A, B); 
    if(B < 0) return GCD(A, -B);
    return (B == 0) ? A : GCD(B, A % B);
}

template<class T> inline T LCM(T A, T B) {
    if(A < 0) return LCM(-A, B);
    if(B < 0) return LCM(A, -B);
    return A * (B / GCD(A, B));
}

template<class T> inline T euclideExt(T A, T B, T & X, T & Y) {
    if(A < 0) {
        T D = euclideExt(-A, B, X, Y);
        X = -X; 
        return D;
    }
    if(B < 0) {
        T D = euclideExt(A, -B, X, Y);
        Y = -Y;
        return D;
    }
    if(B == 0) {
        X = 1, Y = 0;
        return A;
    } else {
        T D = euclideExt(B, A % B, X, Y);
        T Z = X; 
        X = Y, Y = Z - (A / B) * Y;
        return D;
    }
}

template<class T> string toString(T N) {
    ostringstream oSS;
    oSS << N; 
    oSS.flush();
    return oSS.str();
}

// pre functions
bool isUpperCase(char C) { return C >= 'A' && C <= 'Z'; }
bool isLowerCase(char C) { return C >= 'a' && C <= 'z'; }
bool isLetter(char C) { return (C >= 'A' && C <= 'Z') || (C >= 'a' && C <= 'z'); }
bool isDigit(char C) { return C >= '0' && C <= '9'; }
char toLowerCase(char C) { return (isUpperCase(C)) ? (C + 32) : C; }
char toUpperCase(char C) { return (isLowerCase(C)) ? (C - 32) : C; }
double toDouble(string S) { double N = 0; istringstream iSS(S); iSS >> N; return N; }
long long toLongLong(string S) { LL N = 0; istringstream iSS(S); iSS >> N; return N; }
long double toLongDouble(string S) { LD N = 0; istringstream iSS(S); iSS >> N; return N; }
int toInt(string S) { int N = 0; istringstream iSS(S); iSS >> N; return N; }

// consts
const string inputFileName = "input.txt";
const string outputFileName = "output_C.txt";

const LD PI = acos(-1.0);
const LD EPS = 1e-7;

int digits[25];

// variables
bool isPalindrome(LL X) {
    int V_LEN = 0;
    while (X > 0) {
        digits[V_LEN ++] = X % 10;
        X /= 10;
    }

    for (int index = 0; index < V_LEN / 2; ++ index)
        if (digits[index] != digits[V_LEN - index - 1]) {
            return false;
        }

    return true;
}

vector<LL> fair;

int main() {
    freopen(inputFileName.c_str(), "r", stdin);
    freopen(outputFileName.c_str(), "w", stdout);

    // Main soultion :: begin

    int nTest;

    LL A, B;

    fair.clear();
    LL UP = 10000000;
    UP *= (LL) 10000000;

    for (LL val = 1; val * val <= UP; ++ val) 
        if (val * val >= 1 && val * val <= UP) {
            if (isPalindrome(val) && isPalindrome(val * val)) {
                fair.push_back(val * val);
            }
        }

    scanf("%d\n", &nTest);

    for (int iTest = 1; iTest <= nTest; ++ iTest) {

        cin >> A >> B;

        LL result = 0;

        for (int i = 0; i < fair.size(); ++ i)
            if (fair[i] >= A && fair[i] <= B) {
                ++ result;
            }

        cout << "Case #" << iTest << ": " << result;

        printf("\n");                        
    }

    // Main solution :: end

    return 0;
}

